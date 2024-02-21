import os
from dotenv import load_dotenv
load_dotenv()

command = "/home/ynot/fitweb/.venv/bin/gunicorn"
pythonpath = "/home/ynot/fitweb/whatzthefit"
bind = "0.0.0.0:8080"
workers = 3