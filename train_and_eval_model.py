import os
from os.path import join
import logging
import numpy as np
exp_dir = os.environ['EXP_DIR']
logging.basicConfig(filename=join(exp_dir, "log.txt"), level=logging.INFO)

with open(join(exp_dir, "model.txt")) as f:
    f.write("this model has no params\n")

logging.warn("Result: %2.3f", np.random.uniform())
