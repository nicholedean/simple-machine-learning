'''Thompson Sampling'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import random

dataset = pd.read_csv('') # your data file, rows of boolean array

# Implementing Thompson Sampling
N = 10000 # arbitrary
d = 10 # number of arms
arm_selected = []
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d
total_reward = 0
for n in range(0, N):
    arm = 0
    max_random = 0
    for i in range(0, d):
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)
        if random_beta > max_random:
            max_random = random_beta
            arm = i
    arm_selected.append(arm)
    reward = dataset.values[n, arm]
    if reward == 1:
        numbers_of_rewards_1[arm] = numbers_of_rewards_1[arm] + 1
    else:
        numbers_of_rewards_0[arm] = numbers_of_rewards_0[arm] + 1
    total_reward = total_reward + reward
