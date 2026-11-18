# Run Ribbon

Browse the latest Garmin run and its measured kilometer splits or recorded laps.

The last run stays on your desk after the watch comes off. The rear screen pairs the overall moving pace with the elapsed splits, which is handy when a stop at a crossing made one kilometer look unusually slow.

## Read your latest running session

1. Export the original FIT file into the configured folder and click the wheel to refresh.
2. Check the distance on **LAST RUN** and the date and moving pace on the rear. A cycling file in the same folder does not take over this view.
3. Turn the wheel to read the first available detail. The sample has a recorded lap at 5:18 per kilometer.

![The 10.00 km session gives way to LAP 1 at 5:18.](media/guide/inspect-recorded-lap.gif)

## Go back to the whole run

1. Turn back to **LAST RUN** to compare the lap with the overall effort.
2. For a file with a suitable distance trace, browse **SLOWEST KM** and the individual kilometer pages. Those splits use elapsed time and include stops.
3. Press **Start** to pin the page you want to keep after your debrief.

![Lap pace gives way to the 10.00 km session overview.](media/guide/return-to-last-run.gif)

## Example from the emulator

The recorded test used ten kilometers in 53 minutes. That works out to five minutes and eighteen seconds per kilometer. For this file the detail came from a recorded lap. A trace with kilometer crossings can give a different picture, especially on a run with pauses. The companion read synthetic FIT files with Garmin’s official decoder.

## Set up the source

Export original FIT activities from Garmin Connect or your watch to one directory. Install the official decoder with python3 -m pip install -r companion/requirements.txt in a virtual environment. Set folder to your local directory. The first page reports moving pace. Distance traces yield elapsed one-kilometer splits, including pauses. Files without a distance trace show recorded lap pace instead. Duplicate exports count once.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run in the emulator

Open BUSY Bar Emulator. From this repository, run:

```sh
~/.busy-emulator/bin/busy-emulator dev --once
```

Press **Back** to exit.

The GIFs are excerpts from the emulator recording. Each front-display pixel is shown at 9× its original width and height. The end frames pause for reading.

[Full recording](media/controls.mp4) · [Rear display](screenshots/back-1.png) · [Firmware test](EMULATOR-QA.md) · [MIT license](LICENSE)
