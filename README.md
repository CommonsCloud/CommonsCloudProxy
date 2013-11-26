# CommonsCloudProxy

A proxy server for interacting with the CommonsCloud Javascript API

Using this proxy server is based on the assumption that you have an Intermediate knowledge of setting up basic Python applications and are comfortable installing packages and virtual enviornments from the command line.

## Getting Started

1. Download or Fork the repository

2. Install a Virtual Environment

    virtualenv venv

3. Start the virtual enviornment

    source venv/bin/active

4. Install the system dependencies

    pip install flask
    pip install -r requirements.txt

5. Start CommonsCloudProxy

    python runserver.py

6. Your demonstration proxy server is now available at http://127.0.0.1:5000/ by default