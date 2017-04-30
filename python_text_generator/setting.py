#!/usr/bin/env python
import os

# base setting
version = "1.0"
config_var = "PYTHON_TEXT_GENERATOR_CONFIG"

# configuration path
config_path = os.getenv(config_var)
if config_path is None or not os.path.exists(config_path):
    config_path = "{HOME}/.config/python-text-generator".format(HOME = os.getenv('HOME'))

# the path of init.py
init_pyfile = "{PATH}/init.py".format(PATH = config_path)
