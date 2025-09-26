#!/bin/bash

# activate the virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
    echo "Virtual environment activated"
else
    echo "No virtual environment found, using system Python"
fi

# lucn the FastAPI application
# we are using uvicorn to serve our FastAPI app 

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
