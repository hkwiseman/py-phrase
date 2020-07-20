__author__ = "H. Kyle Wiseman"
__copyright__ = "Copyright 2020"
__credits__ = ["H. Kyle Wiseman"]
__license__ = "GPLv3"
__version__ = "0.1.0"
__maintainer__ = "H. Kyle Wiseman"
__email__ = "kwiseman@highpoint.edu"
__status__ = "Development"

from flask import Flask

app = Flask(__name__)

from app import routes
