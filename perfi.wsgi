import os,sys,logging

logging.basicConfig(stream=sys.stderr)

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

activate_this = os.path.join(PROJECT_DIR, 'venv/bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

from perfi import setup,app as application

setup(application)
