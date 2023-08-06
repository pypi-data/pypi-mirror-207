# a z-score calculator for spirometry measurements

## references

This is a port of a calculator written in SAS, named `GLI_macro_code_V1_04_07_13.sas`
which references the following paper

> "Multi-ethnic reference values for spirometry for the 3-95-yr age range: the global lung function 2012 equations"

  as published here <https://pubmed.ncbi.nlm.nih.gov/22743675/>

  which in turn mentions the following that sheds some light on this LMS method

  <https://pubmed.ncbi.nlm.nih.gov/34732174/>

## measurements

| english | french | text | texte |
|:-:|:-:|:-:|:-:|
| FEV1 | VEMS | forced expiratory volume 1s | volume expiratoire maximal seconde |
| FVC | CVF | forced vital capacity | capacité vitale forcée |
| FEV1/FVC | VEMS/CVF | ratio between the 2 above |
| FEF2575 | DEM25-75 | forced expiratory flow | débit expiratoire maximal médian entre 25% et 75% de la CVF
| FEF75 | DEM75 | | débit expiratoire maximal au point 75 de la cvf
|
| FEV075 | ? | xxx need clarification
| FEV75FVC | ? | xxx need clarification

## what it does

the calculator is able to compute z-scores on the following spirometric measurements:

- FEV1
- FVC
- FEV1FVC
- FEF2575
- FEF75
- FEV075 (**)
- FEV75FVC (**)

  **NOTE** the last 2 measurements (**) rely on age-independant lookup

in order to do this, each individual needs to be characterized with their

- sex (1=male, 2=female)
- age (in years, between 3 and 90)
- height (in cm)
- ethnicity (see below)

### the ethnicity coding

| ethnicity | meaning |
|:-:|:-:|
| 1 | Caucasian |
| 2 | African American |
| 3 | North East Asian |
| 4 | South East Asian |
| 5 | Other/mixed |

## installation

```bash
pip install spiro-zscore
```

and then

```python
from spiro_zscore import zscore

help(zscore)
```

## examples

see data files in the `data/` folder

### using well-known names

if your input data contains only names known to the library

```python

test1_std = pd.read_csv("../data/test1-stdnames.csv")
test_std.head(2)

      id  sex   age  height   dem   fvc  fev1  ethnicity
0  19106    2  3.84   105.0  0.90  0.79  0.77          1
1  18331    2  5.72   108.0  0.94  0.94  0.82          2

# compute zscore on the 'fev1' column
# this is a known name, so this call is enough
zscore(test1_std, 'fev1').head(2)

     Z-fev1    PP-fev1  LLN-fev1
0 -1.757611  81.104454  0.781674
1 -0.686230  91.585948  0.712902

# if you want this merged into the incoming data
# (in a copied dataframe)

# ask for a merge
zscore(test1_std, 'fev1', merge=True).columns

Index(['id', 'sex', 'age', 'height', 'dem', 'fvc', 'fev1', 'ethnicity',
       'Z-fev1', 'PP-fev1', 'LLN-fev1'],
      dtype='object')

```

### using your own names

you can also use your own names, with a little help on your end

```python

test1_fr = pd.read_csv("../data/test1-french.csv")
print(test1_fr.head(2))

      id  sexe   age  taille   dem   cvf  vems  ethnic
0  19106     2  3.84   105.0  0.90  0.79  0.77       1
1  18331     2  5.72   108.0  0.94  0.94  0.82       2

# we want to compute the zscore on column 'vems'
# and so we need to tell that it is in fact a 'fev1' data
# also, we are using custom names for the input columns, so:

print(zscore(test1_fr, 'vems', 'fev1', sex='sexe',
             height='taille', ethnicity='ethnic').head(2))

     Z-vems    PP-vems  LLN-vems
0 -1.757611  81.104454  0.781674
1 -0.686230  91.585948  0.712902

# of course we could have added 'merge=True' to get merged data
...
```

### selecting the outcoming outputs

by default the calculator outputs 3 statistics, which are labeled

| label | meaning |
|-:|:-|
| Z | z-score |
| PP | percent predicted |
| LLN | lower limits of normal |

you can select a subset of these, with the `outputs=` parameter to `zscore`;
you must mention an iterable of strings that are among the 3 codes above, case being ignored; for instance

```python
zscore(test1_fr, 'vems', 'fev1', merge=True, outputs=['z'], **renamings).head(2)

      id  sexe   age  taille   dem   cvf  vems  ethnic    Z-vems
0  19106     2  3.84   105.0  0.90  0.79  0.77       1 -1.757611
1  18331     2  5.72   108.0  0.94  0.94  0.82       2 -0.686230

```
