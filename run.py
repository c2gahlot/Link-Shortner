import os
from app import create_app
from json import load

with open('config.json') as f:
    config = load(f)
app = create_app(config)

if __name__ == '__main__':
    app.run()
