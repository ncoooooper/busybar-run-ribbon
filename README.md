# Run Ribbon

Browse the latest Garmin run and its measured kilometer splits or recorded laps.

Export original FIT activities from Garmin Connect or your watch to one directory. Install the official decoder with python3 -m pip install -r companion/requirements.txt in a virtual environment. Set folder to your local directory. The first page reports moving pace. Distance traces yield elapsed one-kilometer splits, including pauses. Files without a distance trace show recorded lap pace instead. Duplicate exports count once.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run locally

From this folder, run `~/.busy-emulator/bin/busy-emulator dev --once` with BUSY Bar Emulator open. Back exits.

![BUSY Bar front display](screenshots/front-1.png)
