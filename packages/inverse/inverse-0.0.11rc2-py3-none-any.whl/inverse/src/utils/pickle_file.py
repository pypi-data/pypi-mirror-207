

import pickle

pickle_folder = "pickles"
from inverse.src.utils.inverse_typings import *

import os
if not os.path.exists(pickle_folder):
    os.makedirs(pickle_folder)

def save_pickle(name, data):
    with open(Path(pickle_folder) / (str(name) + '.pickle'), 'wb') as f:
        pickle.dump(data, f)
def read_pickle(name):
    new_data = False
    with open(Path(pickle_folder) / (str(name) + '.pickle'), 'rb') as f:
        new_data = pickle.load(f)
    return new_data
