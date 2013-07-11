#!/bin/bash

source venv/bin/activate

HOST_BIND=127.0.0.1:9000
WORKERS=2

gunicorn -w $WORKERS -b $HOST_BIND qgic13:app
