# CCL-NMF loading estimation from structural MRI data and basic demographics

This repository provides a lightweight and practical solution for estimating **Coupled Cross-sectional and Longitudinal Non-negative Matrix Factorization (CCL-NMF)** loading coefficients in new datasets, without the need to re-run the full CCL-NMF pipeline.
We provide **pre-trained regression models** that approximate the subject-level cross-sectional CCL-NMF loading coefficients using **regional brain volumes derived from T1-weightet MRI and basic demographic information (age, sex, intracranial volume)** to make CCL-NMF loadings more accessible for downstream research.
The regional volumes used in these models are **not harmonized**. This design choice eliminates the need for users to perform data harmonization, which is often impractical in small or single-site datasets.  
