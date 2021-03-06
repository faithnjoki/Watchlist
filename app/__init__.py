from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__,instance_relative_config=True)

# Setting up configuration
app.config.from_object(DevConfig)
# The app.config.from_pyfile('config.py') connects to the config.py file and all its contents are appended to the app.config.
app.config.from_pyfile('config.py')



from app import views