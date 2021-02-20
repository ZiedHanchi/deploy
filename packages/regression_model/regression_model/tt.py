import os, sys 
from pathlib import Path

if os.path.abspath(os.pardir) not in sys.path :
    sys.path.append(os.pardir)
if Path(os.path.dirname(os.path.realpath(__file__))).parent not in sys.path :
    sys.path.append(str(Path(os.path.dirname(os.path.realpath(__file__))).parent))   
if os.path.dirname(os.path.realpath(__file__)) not in sys.path :
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))