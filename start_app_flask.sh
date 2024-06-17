#!/bin/bash

cd /home/omcloudops/flask-ml

if [ ! -d "myenv" ]; then
        python3.10 -m venv myenv
fi

source myenv/bin/activate

pip3 install -r requirements.txt

python3.10 app.py --host=0.0.0.0