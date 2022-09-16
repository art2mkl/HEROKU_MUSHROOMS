import os
from dotenv import load_dotenv
#Load ENV variables
load_dotenv('.env')
import urllib.parse


APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
params = urllib.parse.quote_plus(os.environ.get('DB_STRING'))

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True   
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_STRING')    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Create the testing config
class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_STRING')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Create the prod config
class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_STRING')    
    SQLALCHEMY_TRACK_MODIFICATIONS = False