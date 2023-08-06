# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # test notebook

# %% trusted=true
import pandas as pd

# %% trusted=true
from spiro_zscore import zscore

# %% [markdown]
# ## loading data

# %% trusted=true
oneline = pd.read_csv("../data/oneline.csv")
oneline

# %% trusted=true
multiline = pd.read_csv("../data/multiline.csv")
multiline

# %% [markdown]
# ## working

# %% [markdown]
# ### one line

# %% trusted=true scrolled=false
z = zscore(oneline, 'fev1')

# %% trusted=true
z

# %% trusted=true
# the input has not changed
oneline

# %% [markdown]
# ## a few lines

# %% trusted=true
z = zscore(multiline, 'fev1')
multiline_fev1 = pd.merge(multiline, z, left_index=True, right_index=True)
multiline_fev1

# %% trusted=true
multiline_fvc = pd.merge(multiline, zscore(multiline, 'fvc'), left_index=True, right_index=True)
multiline_fvc

# %% trusted=true
# multiline_fev1.to_csv("../data/multiline+fev1.csv")
# multiline_fvc.to_csv("../data/multiline+fvc.csv")

# %% [markdown]
# ***

# %% [markdown]
# ## a more complete test

# %% [markdown]
# ### std names - merge or not

# %% trusted=true
test1_std = pd.read_csv("../data/test1-std.csv")
test1_std.head(2)

# %% trusted=true
# with no argument, returns only the 3 measurements
zscore(test1_std, 'fev1').head(2)

# %% trusted=true
# ask for a merge
zscore(test1_std, 'fev1', merge=True).head(2)

# %% [markdown]
# ### custom names - merge or not

# %% trusted=true
test1_fr = pd.read_csv("../data/test1-fr.csv")
test1_fr.head(2)

# %% trusted=true
# here's how to redefine the required column names
renamings = dict(sex='sexe', height='taille', ethnicity='ethnic')

# %% trusted=true
# we want to compute the zscore on column 'vems'
# and so we need to tell that it is in fact a 'fev1' data

zscore(test1_fr, 'vems', 'fev1', **renamings).head(2)

# %% trusted=true
# same, but ask for a merge
zscore(test1_fr, 'vems', 'fev1', merge=True, **renamings).head(2)

# %% [markdown]
# ### selecting outputs

# %% trusted=true
zscore(test1_fr, 'vems', 'fev1', merge=True, outputs=['Z'], **renamings).head(2)

# %% trusted=true
s1 = zscore(test1_fr, 'vems', 'fev1', merge=True, outputs=['Z'], **renamings)
s2 = zscore(s1, 'cvf', 'fvc', merge=True, outputs=['PP'], **renamings)
s2.head(2)

# %% [markdown]
# ### compare with stored results

# %% trusted=true
import os

def compare_test(filename, extra, measurement, *args, index=None, **renamings):
    out = filename.replace(".csv", f"+{measurement}{extra}.csv")
    data = pd.read_csv(filename)
    if index:
        data = data.set_index(index)
    zscore(data, measurement, *args, **renamings, merge=True).to_csv(out)
    print(f"{out} created or overwitten")
    ref = out.replace("/data/", "/data/ref/")
    command = f"cmp {out} {ref}"
    retcod = os.system(command)
    print(f"{command} -> {'OK' if retcod == 0 else 'OOOPS!!'}")


# %% trusted=true
compare_test("../data/test1-std.csv", "", "fev1")

# %% trusted=true
compare_test("../data/test1-std.csv", "", "fvc")

# %% trusted=true
compare_test("../data/test1-fr.csv", "", "vems", "fev1", **renamings)

# %% trusted=true
compare_test("../data/test1-fr.csv", "", "cvf", "fvc", **renamings)

# %% trusted=true
compare_test("../data/test1-fr.csv", "-zonly", "cvf", "fvc", outputs=['z'], **renamings)

# %% [markdown] trusted=true
# ### using odd indexes

# %% [markdown]
# here we use the 'id' column as the index of the incoming dataframe

# %% trusted=true
compare_test("../data/test1-std.csv", "-id", "fev1", index='id')

# %% trusted=true
compare_test("../data/test1-fr.csv", "-zonly-id", "cvf", "fvc", index='id', outputs=['z'], **renamings)

# %% [markdown]
# ## comparing with the SAS version

# %% trusted=true
# this lib works better than plain sas7bdat - fewer warnings issued
from sas7bdat_converter import to_dataframe

test1_sas = to_dataframe('../data/ref/test1-std-spirosas.sas7bdat')
#test1_sas.columns

# %% trusted=true
focus = 'id+sex+age+height+fev1+ethnicity+FEV1_z_score+fvc_z_score'.split('+')

# %% trusted=true
test1_sas[focus].head(2)

# %% [markdown]
# ### obsolete: using sas calculator output from csv

# %% trusted=true
# no longer used
#test1_sas_csv = pd.read_csv("../data/ref/test1-std-spirosas.csv")
#test1_sas_csv.columns

# %% trusted=true
# they are really close enough -- not the reason for our 0.1% discrepancy
# np.isclose(test1_sas.FEV1_z_score, test1_sas_csv.FEV1_z_score, rtol=1e-16)

# %% trusted=true
# test1_sas.FEV1_z_score - test1_sas_csv.FEV1_z_score

# %% [markdown]
# ### fvc

# %% [markdown]
# let's start with a couple helper functions that gather and compare the outputs of 
# * the sas calculator
# * our Python implementation

# %% trusted=true
import numpy as np


# %% trusted=true
def build_sas_compare(in_csv, sasb7dat, measurement, ourcols, sascols):
    our = (zscore(pd.read_csv(in_csv), measurement, merge=True, outputs=['z'])
           [['id'] + ourcols]
          )
    sas = (to_dataframe(sasb7dat)
               [['id'] + sascols])
    return pd.merge(our, sas, on='id').sort_values(by='id')



# %% trusted=true
def build_sas_compare_and_stats(
    in_csv, sasb7dat, measurement, our_z, sas_z):
    
    df = build_sas_compare(in_csv, sasb7dat, measurement, [our_z], [sas_z])
    df['diff'] = df[our_z] - df[sas_z]
    s1 = (df[our_z] / df[sas_z])
    s2 = 1/s1
    df['percent'] = 100*s1.combine(s2, np.maximum)
    return df


# %% trusted=true
fvc = build_sas_compare_and_stats(
    "../data/test1-std.csv", 
    '../data/ref/test1-std-spirosas.sas7bdat', 
    'fvc', 'Z-fvc', 'fvc_z_score')
fvc

# %% trusted=true
# the largest relative error on this sample is 
fvc.percent.max()

# %% [markdown]
# ### fev1

# %% trusted=true
fev1 = build_sas_compare_and_stats(
    "../data/test1-std.csv", 
    "../data/ref/test1-std-spirosas.sas7bdat", 
    'fev1', "Z-fev1", "FEV1_z_score")
fev1

# %% trusted=true
fev1.percent.max()

# %% [markdown]
# ### dem2575

# %% trusted=true
#test1_sas.columns

# %% trusted=true
fef2575 = build_sas_compare_and_stats(
    "../data/test1-std.csv", 
    "../data/ref/test1-std-spirosas.sas7bdat", 
    'fef2575', "Z-fef2575", "fef2575_z_score")
fef2575

# %% trusted=true
fef2575.percent.max()

# %% [markdown]
# ***
