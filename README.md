# CCL-NMF loading estimation from structural MRI data and basic demographics

This repository provides a lightweight and practical solution for estimating **Coupled Cross-sectional and Longitudinal Non-negative Matrix Factorization (CCL-NMF)** loading coefficients in new datasets, without the need to re-run the full CCL-NMF pipeline.
We provide **pre-trained regression models** that approximate the subject-level cross-sectional CCL-NMF loading coefficients using **regional brain volumes derived from T1-weighted MRI and basic demographic information (age, sex, intracranial volume)** to make CCL-NMF loadings more accessible for downstream research.
The regional volumes used in these models are **not harmonized**. This design choice eliminates the need for users to perform data harmonization, which is often impractical in small or single-site datasets.  

## Installation
It is strongly recommended to install the application in a new virtual environment, such as via [Miniconda](https://www.anaconda.com/docs/getting-started/miniconda/main) or [venv](https://docs.python.org/3/library/venv.html).
Please see the respective pages to learn how to set up a virtual environment for python 3.10 on your system and activate it.

When your desired environment is active:
```
git clone https://github.com/CBICA/CCL_NMF_Prediction.git
cd CCL_NMF_Prediction
pip install -e .
```

## Usage
CCL_NMF_Prediction requires 3 arguments:

- -i : The input DLMUSE ROI CSV. This is a comma-separated tabular data containing volumes for ROIs with columns matching the DLMUSE ROI indices. This should be the output of the [NiChart_DLMUSE](https://github.com/CBICA/NiChart_DLMUSE) tool.
- -d : The demographics CSV containing at least MRID (string, the subject identifier), Age (integer), Sex ("M"/"F").
- -o : The path to the output CSV file containing CCL-NMF component predictions. Must be writable.

An example command is:
```
CCL_NMF_Prediction -i /path/to/input.csv -d /path/to/demographics.csv -o /path/to/output.csv
```
