"""
a calculator for computing z-scores

requirements:
the incoming dataframe is expected to have at least the following columns

 'sex': 1 or male and 2 for female
 'age': a float between 3 and 90
 'height': in cm
 'ethnicity': a categorical meaning

    | ethnicity | meaning |
    |:-:|:-:|
    | 1 | Caucasian |
    | 2 | African American |
    | 3 | North East Asian |
    | 4 | South East Asian |
    | 5 | Other/mixed |

 plus one or several columns, named e.g.
 `FEV1`: measured on that individual

"""

from pkg_resources import resource_filename

import numpy as np
import pandas as pd



# the required incoming field (may be renamed, but are required
# even for special measurements, which is suboptimal..)
REQUIRED = ('sex', 'age', 'height', 'ethnicity')

# supported measurements; again these can be renamed,
# but the measurement name  must be among these (ignoring case)
# regular means the tables are age-dependant
REGULAR_MEASUREMENTS = {'FEF2575', 'FEF75', 'FEV1', 'FEV1FVC', 'FVC'}
# special means the tables are age-independant
SPECIAL_MEASUREMENTS = {'FEV075', 'FEV075FVC'}
ALL_MEASUREMENTS = REGULAR_MEASUREMENTS | SPECIAL_MEASUREMENTS

# zscore, percent_predicted, and LLN (lower limits of normal)
DEFAULT_OUTPUTS = ('Z', 'PP', 'LLN')


# fetch the tables as packages in setup.py
LOOKUP_PATH = resource_filename('spiro_zscore', "tables/spiro-zscore-lookup.csv")


# pylint: disable=invalid-name

# cache the lookup tables
_lookup = None

def _load_lookup_tables():
    global _lookup                                      # pylint: disable=global-statement
    if _lookup is None:
        _lookup = pd.read_csv(LOOKUP_PATH)
    return _lookup


def _missing_requirements(df) -> list:
    """
    check for the presence of the required input
    """
    return [required for required in REQUIRED if required not in df.columns]


def _process_renamings(**kwds) -> dict[str, str]:
    # all keyword args should be part of REQUIRED
    foreign = [k for k in kwds if k not in REQUIRED]
    if foreign:
        raise ValueError(f"Unknown keyword arg {foreign}, must be in {REQUIRED}")
    # when saying sex='sexe', we need to rename 'sexe' into 'sex'
    return {v: k for k, v in kwds.items()}


def zscore(df,
           column,
           measurement=None,
           merge=False,
           outputs=None,
           **kwds):
    """
    computes the zscore of one column in the dataframe

    Parameters:
      df: the input data, as described above
      column: the column on which we compute z-score
      measurement: if None, use column instead; in any case, must be
        one of the 5 predefined constants that define the regular measurement;
        this is case-insensitive
      kwds:
        by default the incoming table must have the 4 required columns 'sex',
        'age', 'height' and 'ethnicity'; you can redefine any of these 4
        parameters to refer to another column name instead; for example if your
        table has the `height` information in a column named `taille`, then you
        can pass `height='taille'`
      merge:
        changes the way the function behaves, either by returning a separate
        dataframe with only the computed information (merge=False), or by
        returning a merge of the incoming dataframe with that information
        (merge==True)

    the function computes 3 columns, containing: the resulting z-score,
    percent_predicted and LLN named; they are named after the original column
    name like so: Z_{{column}}, PP_{{column}} and LLN_{{column}} respectively

    as described above, it will return
      if merge==False:
        the 3 columns in a standalone dataframe, with the same index as df; it
        can thus be merged easily with `pd.merge` using `left_index=True` and
        `right_index=True`
      if merge==True: returns a copy of the incoming dataframe with the 3
        resulting columns added

    caveat: as of 0.3, this tool does not behave properly if the incoming dataframe
    has a MultiIndex
    """
    if column not in df.columns:
        raise ValueError(f"{column} not in input dataframe")
    if measurement is None:
        measurement = column
    measurement = measurement.upper()
    if measurement not in ALL_MEASUREMENTS:
        raise ValueError(f"{measurement} not among {REGULAR_MEASUREMENTS}")

    if outputs is None:
        outputs = DEFAULT_OUTPUTS
    else:
        outputs = [o.upper() for o in outputs]
    foreign = [o for o in outputs if o not in DEFAULT_OUTPUTS]
    if foreign:
        raise ValueError(f"Unknown output arg(s) {foreign}, must be in {DEFAULT_OUTPUTS}")

    if df.index.nlevels != 1:
        raise ValueError(f"zscore: does not support MultiIndexes")


    # we need to deal separately with
    # either a 'regular' measurement that has age-dependant tables
    # or a 'special' measurement that has a flat table for all ages

    # create a copy of the incoming df
    # w stands for 'working-copy'
    w = df.copy()                                       # pylint: disable=
    # rename incoming columns to match the required names
    w.rename(columns = _process_renamings(**kwds), inplace=True)

    if (missing := _missing_requirements(w)):
        raise ValueError(f"not all required fields are present, {missing}")

    # we have two ways to compute the LMS columns:

    if measurement in REGULAR_MEASUREMENTS:
        w = _compute_regular_lms(w, measurement)
    else:
        w = _compute_special_lms(w, measurement)

    # once LMS are known, the same formulas apply:
    return _finish(df, w, column, merge, outputs)



def _compute_regular_lms(w, measurement):

    """
    the regular scheme is to use the lookup tables
    according to the individual's age
    """

    # sanity check
    nb_incoming_lines = len(w)

    # add a column with the rounded age
    w['agebound'] = np.floor(w['age']*4)/4
    # this is needed because we need to join on this criteria as well
    w['_f'] = measurement

    lookup = _load_lookup_tables()

    # and now we can do the JOIN so that each row (each individual)
    # has all the relevant coefficients in the same line as its input data
    # the reset_index / set_index is a trick needed to preserve the initial df index
    # it is fragile with multi-indexes, so avoid that !
    w = (w
        .reset_index(names='__index__')
        .merge(lookup, how='left', left_on=['sex', 'agebound', '_f'], right_on=['sex', 'agebound', 'f'])
        .set_index('__index__'))

    # sanity check
    if (len(w)) != nb_incoming_lines:
        raise ValueError(f"zscore: lookup returned {len(w)} lines,"
                         f" was expecting {nb_incoming_lines}")

    # store intermediate results as new columns
    # age interpolation
    w['l'] = w.l0 + (w.age-w.agebound)/0.25 * (w.l1-w.l0)
    w['m'] = w.m0 + (w.age-w.agebound)/0.25 * (w.m1-w.m0)
    w['s'] = w.s0 + (w.age-w.agebound)/0.25 * (w.s1-w.s0)

    # ethnicity
    w['a'] = (   (w.ethnicity == 1) * 0
               + (w.ethnicity == 2) * w.a3
               + (w.ethnicity == 3) * w.a4
               + (w.ethnicity == 4) * w.a5
               + (w.ethnicity == 5) * w.a6)
    w['p'] = (   (w.ethnicity == 1) * 0
               + (w.ethnicity == 2) * w.p2
               + (w.ethnicity == 3) * w.p3
               + (w.ethnicity == 4) * w.p4
               + (w.ethnicity == 5) * w.p5)

    w['L'] = w.q0 + w.q1 * np.log(w.age) + w.l
    w['M'] = np.exp(w.a0 + w.a1*np.log(w.height) +w.a2*np.log(w.age) + w.a + w.m)
    w['S'] = np.exp(w.p0 + w.p1*np.log(w.age) + w.p + w.s)
    return w



def _compute_special_lms(w, measurement):

    """
    the special scheme performs a simpler lookup, depending just on sex and measurement
    also the ethnicity does matter here
    """

    # sanity check
    nb_incoming_lines = len(w)

    # this is needed because we need to join on this criteria as well
    w['_f'] = measurement

    lookup = _load_lookup_tables()

    # and now we can do the JOIN so that each row (each individual)
    # has all the relevant coefficients in the same line as its input data
    # ditto
    w =(w
        .reset_index(names='__index__')
        .merge(lookup, how='left', left_on=['sex', '_f'], right_on=['sex', 'f'])
        .set_index('__index__'))

    # sanity check
    if (len(w)) != nb_incoming_lines:
        raise ValueError(f"zscore: lookup returned {len(w)} lines,"
                         f" was expecting {nb_incoming_lines}")

    w['L'] = w.q0
    # note: here the formulas use 'age' instead of 'log(age)'
    w['M'] = np.exp(w.a0 + w.a1*np.log(w.height) +w.a2*w.age)
    w['S'] = np.exp(w.p0 + w.p1*w.age)
    return w



def _finish(df, w, column, merge, outputs):
    """
    the incoming w dataframe has the L M and S columns, and from there
    we perform final computations as requested by outputs and merge
    """

    news = []
    for output in outputs:
        news.append(new := f"{output}-{column}")
        match output:
            case 'Z':
                w[new] = (((w[column] / w.M)**w.L)-1) / (w.L * w.S)
            case 'PP':
                w[new] = 100 * w[column] / w.M
            case 'LLN':
                w[new] = w.M * (((-1.645*w.S*w.L)+1)**(1/w.L))

    result = w[news]
    if not merge:
        return result
    else:
        return df.merge(result, left_index=True, right_index=True)
