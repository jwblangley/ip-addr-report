# ip-addr-report
Simple python script to report when the machine's public IP address is changed

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
