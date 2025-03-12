import argparse
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import StratifiedKFold
import pickle # for model loading
import warnings

from .utils import get_data, predict_ccl_nmf

warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.simplefilter(action="ignore", category=UserWarning)

def load_data(muse_csv_path, covar_csv_path):
    # Standardize the MUSE CSV

    # Combine the covar csv with the MUSE ROI Volumes

    # return a consolidated df
    pass

def train_ccl_nmf_prediction_models(consolidated_df):
    pass

def predict_ccl_nmf(consolidated_df):
    pass