import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import StratifiedKFold
import pickle # for model saving

from .utils import get_data, predict_ccl_nmf

warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.simplefilter(action="ignore", category=UserWarning)

# VERSION = pkg_resources.require("NiChart_DLMUSE")[0].version
VERSION = 0.1


def main() -> None:
    pass