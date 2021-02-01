import sys
import os
from os.path import dirname, realpath, sep, pardir

if dirname(realpath(__file__)) not in sys.path :
    sys.path.append(dirname(realpath(__file__)))
if dirname(os.getcwd()) not in sys.path :
    sys.path.append(os.getcwd())
if sep.join(dirname(realpath(__file__)).split("/")[:-2]) + sep + "regression_model" not in sys.path :
    sys.path.append(sep.join(dirname(realpath(__file__)).split("/")[:-2]) + sep + "regression_model")
if sep.join(dirname(realpath(__file__)).split("/")[:-2]) + sep + "regression_model" + sep + "regression_model" not in sys.path :
    sys.path.append(sep.join(dirname(realpath(__file__)).split("/")[:-2]) + sep + "regression_model" + sep + "regression_model")

from api.config import PACKAGE_ROOT

with open(PACKAGE_ROOT / 'VERSION') as version_file:
    __version__ = version_file.read().strip()
