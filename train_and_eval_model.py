import os
from os.path import join
import logging
import numpy as np
exp_dir = os.environ['EXP_DIR']
logging.basicConfig(filename=join(exp_dir, "log.txt"), level=logging.INFO)
logger = logging.getLogger("sred_demo")
logger.addHandler(logging.StreamHandler())

with open(join(exp_dir, "model.txt"), "w") as f:
    f.write("this model has no params\n")

logger.warn("Result: %2.3f", np.random.uniform())
