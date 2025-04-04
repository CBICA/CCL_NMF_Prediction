import argparse
import numpy
import pandas as pd
# from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import StratifiedKFold
import pickle # for model loading
import warnings

from .utils import consolidate_data, predict_ccl_nmf

warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.simplefilter(action="ignore", category=UserWarning)

# VERSION = pkg_resources.require("NiChart_DLMUSE")[0].version
VERSION = 0.1


def main() -> None:
    prog = "CCL_NMF_Predict"
    parser = argparse.ArgumentParser(
        prog=prog,
        description="CCL_NMF component (7) Prediction Tool",
        usage="""
        CCL_NMF_Predict v{VERSION}
        
        Prediction of 7 ccl_nmf components.

        Required arguments:
            [-i, --in_dir]   The filepath of an input CSV containing DLMUSE ROI Volumes (including 702 ICV Volume)
            [-d, --demog]    The filepath of an input CSV containing ID (str), Age (float), and Sex (str: "M" or "F") covariate information
            [-o, --out_dir]  The filepath of an output CSV file containing the predicted CCL_NMF components.
        Optional arguments:
            [-h, --help]    Show this help message and exit.
            [-V, --version] Show program's version number and exit.
        EXAMPLE USAGE:
            ccl_mnf_prediction  -i           /path/to/input_dlmuse_roi_volumes.csv \
                                -d           /path/to/input_demog.csv            \
                                -o           /path/to/output.csv

        """.format(
            VERSION=VERSION
        ),
    )

    # Required Arguments
    parser.add_argument(
        "-i",
        "--in_dir",
        type=str,
        required=True,
        help="[REQUIRED] Input folder with T1 sMRI images (csv).",
    )
    parser.add_argument(
        "-d",
        "--demog",
        type=str,
        required=True,
        help="[REQUIRED] Input folder with T1 sMRI images (csv).",
    )
    parser.add_argument(
        "-o",
        "--out_dir",
        type=str,
        required=True,
        help="[REQUIRED] Output CSV path.",
    )

    args = parser.parse_args()
    if not args.in_dir or not args.demog:
        parser.error("The following arguments are required: -i / --in_dir, -d / --demog")

    df = consolidate_data(args.in_dir,args.demog)
    predict_ccl_nmf(df, args.out_dir)

if __name__ == "__main__":
    main()
    
