# Emulator verification

Synthetic Garmin FIT files generated and decoded with Garmin's official SDK.

Selected the latest running session of 10 km in 53 minutes, excluding a cycling session, then opened its recorded lap.

13 distinct frames were recorded on firmware 1.3.1. App io.ncoooooper.runribbon exited: finished; heap peak 81.5 of 128 KiB. Screenshots are in screenshots/ and the recording is in media/.

## Display capture

Firmware 1.3.1 rendered both README examples. The display run replayed sample inputs in a separate emulator project. The source test above describes how those readings were obtained. Each square in a guide GIF is one front-display pixel enlarged to 9 × 9. The production archive was built from the source in this repository.
