#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 13:58:47 2017
Loop weighted sum in every position
@author: aaron
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import os
import csv
import matplotlib as mpl
from scipy.fftpack import fft,ifft,rfft
%matplotlib inline 
import sys
# from pylab import *  
# mpl.rcParams['font.sans-serif'] = ['SimHei'] 
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
from scipy import  stats,signal
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题