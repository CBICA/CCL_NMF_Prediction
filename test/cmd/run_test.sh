#! /bin/bash

cmd='ccl_nmf_prediction -i ../input/IXI/dlmuse/IXI_dlmuse.csv -d ../input/IXI/lists/IXI_demog_n10.csv -o ../output/IXI/IXI_CCL-NMF_Scores.csv'

echo "About to run: $cmd"
$cmd

