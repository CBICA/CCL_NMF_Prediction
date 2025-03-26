# import argparse
import numpy as np
import pandas as pd
# from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import StratifiedKFold
import pickle # for model loading
import warnings

#from .utils import get_data, predict_ccl_nmf

warnings.simplefilter(action="ignore", category=FutureWarning)
warnings.simplefilter(action="ignore", category=UserWarning)

def consolidate_data(dlmuse_csv_path, demog_csv_path):
    list_roi = ['23', '30', '31', '32', '36', '37', '38', '39', '47', '48', '55', '56', '57', '58', '59', '60', 
                '71', '72', '73', '75', '76', '100', '101', '102', '103', '104', '105', '106', '107', '108', 
                '109', '112', '113', '114', '115', '116', '117', '118', '119', '120', '121', '122', '123', '124', 
                '125', '128', '129', '132', '133', '134', '135', '136', '137', '138', '139', '140', '141', '142', 
                '143', '144', '145', '146', '147', '148', '149', '150', '151', '152', '153', '154', '155', '156', 
                '157', '160', '161', '162', '163', '164', '165', '166', '167', '168', '169', '170', '171', '172', 
                '173', '174', '175', '176', '177', '178', '179', '180', '181', '182', '183', '184', '185', '186', 
                '187', '190', '191', '192', '193', '194', '195', '196', '197', '198', '199', '200', '201', '202', 
                '203', '204', '205', '206', '207']
    df_dlmuse = pd.read_csv(dlmuse_csv_path)
    dlmuse_roi = sorted([i for i in range(23,208) if str(i) in df_dlmuse.columns])
    df_dlicv_baseline = df_dlmuse[['MRID','702']]
    df_dlmuse = df_dlmuse[['MRID']+list_roi]

    df_demographics = pd.read_csv(demog_csv_path)
    if 'M' in df_demographics.Sex or 'F' in df_demographics.Sex:
        df_demographics.Sex = df_demographics.Sex.apply(lambda x: 1 if x=='M' else 0)
    
    return df_dlmuse.merge(df_demographics,on='MRID',how='inner').merge(df_dlicv_baseline,on='MRID',how='inner').rename(columns={'702':'dlicv_baseline'})


# def train_ccl_nmf_prediction_models(consolidated_df):
#     pass

def predict_ccl_nmf(consolidated_df, out_csv_path):
    X = consolidated_df.drop('MRID',axis=1).to_numpy()
    ccl_nmf_components = [f"CCL_NMF{i}" for i in range(1, 8)]
    all_result = pd.DataFrame()
    all_result['MRID'] = consolidated_df.MRID
    for ccl_nmf in ccl_nmf_components:
        print(f'Processing {ccl_nmf}')
        with open(f"../models/model_{ccl_nmf}.pkl", 'rb') as f:
            model = pickle.load(f)
        all_result[ccl_nmf] = model.predict(X)[0]
    all_result.to_csv(out_csv_path,index=False)
