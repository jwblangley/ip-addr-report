# ip-addr-report
Simple python script to report when the machine's public IP address is changed. Ideal for use with a home server where a public static IP address has not been obtained from the ISP.

Recommended to use with `cron`

## Installation
This repository uses python virtual environments

First, if you have not already, install `virtualenv`
```bash
python3 -m pip install --user virtualenv
```

Create a virtual environment
```bash
python3 -m venv env
```

Activate the virtual environment
```bash
source env/bin/activate
```

Install required packages
```bash
pip install -r requirements.txt
```

**N.B.: `requirements.txt` can be updated from within the virtual environment with `pip freeze > requirements.txt`**

When you are finished, to close the virtual environment
```bash
deactivate
```

## Configuration
This repository uses `dotenv` to manage private configuration variables. Create a `.env` file in the root directory to utilise this.

To use [Pushbullet](https://pushbullet.com) reporting, add your Pushbullet API key to the `.env` file:
```
PUSHBULLET_API_KEY=<your_key_here>
```

## Running
With the virtual environment activated run the following:
```bash
python reportIp.py <method1> <method2> <...>
```

e.g.1 To just show updates to the terminal screen
```bash
python reportIp.py
```

e.g.2 To send updates to the linked Pushbullet account
```bash
python reportIp.py pushbullet
```

Current supported methods:
* `pushbullet`
