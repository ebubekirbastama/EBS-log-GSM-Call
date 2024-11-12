# ADB Logcat Viewer

This Python application captures and filters logs from an Android device using `adb logcat`, and displays filtered logs in a GUI window. It specifically filters logs that contain the term "Telephony:", while excluding logs that contain "OllieTelephony".

## Features
- Captures logs from an Android device using `adb logcat`.
- Filters logs to display only those containing "Telephony:".
- Excludes logs that contain the term "OllieTelephony".
- Real-time log display in a scrollable window.
- Easy to use GUI with a start button to begin capturing logs.

## Requirements

Before using the application, you need to have the following installed:

- **Python 3.x**: Install Python from [python.org](https://www.python.org/downloads/).
- **ADB**: Android Debug Bridge is required to communicate with the Android device. You can install it via Android Studio or by downloading the platform tools [here](https://developer.android.com/studio#downloads).
- **Python libraries**:
  - `tkinter`: For creating the graphical user interface (GUI).
  - `subprocess`: For executing ADB commands from within Python.

You can install the necessary Python libraries via pip (if they are not installed by default):

```bash
pip install tk
```
