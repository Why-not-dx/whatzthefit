import os
from dotenv import load_dotenv
load_dotenv()

command = "/home/ubuntu/.venv/bin/gunicorn"
pythonpath = "/home/ubuntu/fitweb"
bind = "178.16.128.64:8000"
workers = 3