#!/bin/bash

pip3 install -r ./backend/requirements.txt
npm install --prefix ./trip_calc_app
python3 -m uvicorn --port 3000 --app-dir ./backend main:app | wait | npm run dev --prefix ./trip_calc_app