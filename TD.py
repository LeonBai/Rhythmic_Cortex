## The source code for temporal de-correlation and intrinsic frequency 

import numpy as np

power = '../../dataset/HCP_1_power.npy'

data_power = np.load(power)

mean_power = np.mean(data_power, axis = 0)  ## Average across 400 subj

##### Temporal de-correlation 

import scipy as sp
from scipy.linalg import eig, eigh
import numpy as np


X = np.array(mean_power.T)
m = np.mean(X, axis=1) 
m = np.expand_dims(m, axis=1)
X -= m #zero mean constraint
std = np.expand_dims(np.std(X, axis=1), axis=1)
X = X/std

L=X.shape[1]
dt = 1
C = np.cov(X) 
dX = np.diff(X)/dt
dC = np.dot(dX, dX.T)/(L-1)
value, W = eig(dC, C)

sort_idx = np.argsort(value)
W_inverse = np.linalg.inv(W)
Y = np.dot(W.T,np.dot(W_inverse.T,X))
Y =  Y.real   ## For sanity, we only keep the real part

##### Intrinsic frequency (dominate frequency)

from nitime.timeseries import TimeSeries
from nitime.analysis import SpectralAnalyzer, FilterAnalyzer


ts_power = TimeSeries(Y, sampling_rate=0.72) ## ONLY FOR hcp data

F_power = FilterAnalyzer(ts_power, ub=0.2, lb = 0.01)  ## Confine power within 0.01 to 0.2Hz as higher ones not meaningful

s_power = SpectralAnalyzer(F_power.fir)

IF_power = []

for i in range(264):## over 264 nodes across the cortex
    index = np.where(s_power.spectrum_multi_taper[1][i] == np.amax(s_power.spectrum_multi_taper[1][i]))
    tem = s_power.spectrum_multi_taper[0][index]
    IF_power.append(tem)
    
IF_power = np.squeeze(np.asarray(IF_power))  ## Intrinsic frequency 

