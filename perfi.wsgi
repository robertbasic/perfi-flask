import os,sys

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from perfi import app as application
