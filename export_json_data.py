"""
Script to export results data of the UKB PheWAS-SensR study to a
JSON format for easy loading in the webpage version.
"""

import pathlib
import json

import pandas

data_dir = pathlib.Path("../data/ukbb/global_phewas/cohort2/")
out_dir = pathlib.Path("data/")


files = [
    dict(filename = "phecodes.three_components", index_col = "phenotype"),
    dict(filename = "predictive_tests.cox", index_col="meaning"),
]
for file in files:
    index_col = file["index_col"]
    in_file = data_dir / f"{file['filename']}.txt"
    out_file = out_dir / f"{file['filename']}.json"
    df = pandas.read_csv(in_file, sep="\t", index_col=index_col)
    df.to_json(out_file, orient="index")
