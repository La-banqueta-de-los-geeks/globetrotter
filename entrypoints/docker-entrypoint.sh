#!/bin/sh

set -e
pip install -r requirements.txt
python ./app/subscriber.py