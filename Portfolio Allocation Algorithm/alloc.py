from venv import create
import numpy as np
import pandas as pd
import scipy

#########################################################################
## Change this code to take in all asset price data and predictions    ##
## for one day and allocate your portfolio accordingly.                ##
#########################################################################

df = pd.DataFrame(columns=["A", "B", "C", "D", "E", "F", "G", "H", "I"])

def create_percent(asset_prices):
    returns = asset_prices.pct_change().iloc[1:,:]
    return returns

def mean_variance(data):
    mu = data.mean()
    Sigma = data.cov()

    # Diagonalizing
    sig_d = np.zeros(Sigma.shape)
    np.fill_diagonal(sig_d,Sigma.to_numpy().diagonal())
    Sigma = sig_d

    Sigma_inv = np.linalg.inv(Sigma)
    weights = mu @ Sigma_inv
    weights = weights / weights.sum()
    wts_tan = pd.Series(weights, index = mu.index)

    return wts_tan

def allocate_portfolio(asset_prices, asset_price_predictions_1,\
                       asset_price_predictions_2,\
                       asset_price_predictions_3):
    
    df.loc[len(df)] = asset_prices
    wts =[]
    if (len(df) > 2):
        returns = create_percent(df)
        wts = mean_variance(returns)
        wts = wts.to_numpy()
    return wts
