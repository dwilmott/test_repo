# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 08:44:14 2022

@author: rodjw
"""
import pandas as pd
import numpy as np

# Set how many iterations to run, & size of ID sample in each iteration
n_iters = 10000
smpl_sz = 25000

# Create a sample df with 10MM unique IDs
# - Generate some dummy sales data to play with later
id_samp = pd.DataFrame(range(10000000,20000000))
id_samp.columns = ['Customer_ID']
id_samp['Sales_Per_ID'] = np.random.normal(loc = 1000, scale = 150, size = len(id_samp))
print(id_samp.head())

# Create a random sample of integers for use as ID sample random state seed
# - Here, we pull a sequence of numbers 50x greater than num iterations to sample from
rndm_st_sd_pop = pd.Series(range(0,n_iters*50))
rndm_st_sd_samp = rndm_st_sd_pop.sample(n = 1429, axis = 'rows')
del(rndm_st_sd_pop)
print(rndm_st_sd_samp.head())

# Initialize data object(s) to store info for each iteration's sample
metric_of_interest = []

# In the loop, use the random state seed to produce a sample you can easily reproduce later
for i in rndm_st_sd_samp:
    samp = id_samp.sample(n = smpl_sz, axis = 'rows', random_state = i)
    # Do something with the sample & record add'l info as necessary
    metric_of_interest.append(samp['Sales_Per_ID'].mean())

# Bind the info you save for each iteration to resp. seed value for easy lookup
sample_data = pd.DataFrame(
    {'Avg_Sales_Per_ID': metric_of_interest,
     'Smpl_Rndm_St_Seed': rndm_st_sd_samp })
sample_data.reset_index(inplace = True)
print(sample_data.head())


sample_data = sample_data[['Avg_Sales_Per_ID','Smpl_Rndm_St_Seed']]
# Original version
# Initialize data objects to store sample, info for each iteration's sample
metric_of_interest = []
samples = []

# In the loop, use the random state seed to produce a sample you can easily reproduce later
for i in range(n_iters):
    samp = id_samp.sample(n = smpl_sz, axis = 'rows', random_state = i)
    samples.append(samp)
    # Do something with the sample & record add'l info as necessary
    metric_of_interest.append(samp['Sales_Per_ID'].mean())



