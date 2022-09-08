import numpy as np
import os, math
# Load matlab file
from scipy.io import loadmat
from collections import Counter
import g_var

class ds_loaded:
    def __init__(self, path):
        self.data = self.load_ds(path)
        pass

    def load_ds(self, fn:str ):
        # Can return many kind of results (dicts, arrays, sequences?)
        if fn.endswith('mat'):
            data = load_mat(fn)
            # loadmat return dicts, might need to
        else:
            data = []
        return data
    
def load_mat(fn):
    if os.path.exists(fn):
        return loadmat(fn)