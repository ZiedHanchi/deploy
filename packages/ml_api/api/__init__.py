import sys
import os
from os.path import dirname, realpath, sep, pardir
from pathlib import Path



if dirname(realpath(__file__)) not in sys.path :
    sys.path.append(dirname(realpath(__file__)))
if dirname(os.getcwd()) not in sys.path :
    sys.path.append(os.getcwd())
if sep.join(dirname(realpath(__file__)).split("/")[:-2]) + sep + "regression_model" not in sys.path :
    sys.path.append(sep.join(dirname(realpath(__file__)).split("/")[:-2]) + sep + "regression_model")
if sep.join(dirname(realpath(__file__)).split("/")[:-2]) + sep + "regression_model" + sep + "regression_model" not in sys.path :
    sys.path.append(sep.join(dirname(realpath(__file__)).split("/")[:-2]) + sep + "regression_model" + sep + "regression_model")
if Path(os.path.dirname(os.path.realpath(__file__))).parent not in sys.path :
    sys.path.append(str(Path(os.path.dirname(os.path.realpath(__file__))).parent))  
if Path(os.path.dirname(os.path.realpath(__file__))).parent.parent not in sys.path :
    sys.path.append(str(Path(os.path.dirname(os.path.realpath(__file__))).parent.parent))  

from api.config import PACKAGE_ROOT

with open(PACKAGE_ROOT / 'VERSION') as version_file:
    __version__ = version_file.read().strip()