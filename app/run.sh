#!/bin/bash

pip3 install -r ./backend/requirements.txt
npm install --prefix ./trip_calc_app
npm run dev --prefix ./trip_calc_app | uvicorn --port 3000 --app-dir ./backend main:app