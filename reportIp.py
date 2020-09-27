import os
from requests import get
from dotenv import load_dotenv

load_dotenv()

STORE_FILE = 'ip-address.txt'

def getIp():
    return get('https://api.ipify.org').text

def reportEmail(currIp):
    print('sending email')


def reportUpdate(currIp, *methods):
    methods = list(methods)
    print('Reporting via: ' + ', '.join(methods))

    for method in methods:
        if method == 'email':
            reportEmail(currIp)
        else:
            print('Unknown report method: \'' + method + '\'')


if __name__ == "__main__":
    # Open file and create if it does not exist
    store = open(STORE_FILE, 'a+')
    store.seek(0)

    # Read existing and move cursor to end. Trim trailing new line
    prevIps = store.read().split('\n')[:-1]

    currIp = getIp()
    print('Current public IP address: ' + currIp)

    if (len(prevIps) == 0):
        print('No known previous public IP addresses')
    else:
        lastIp = prevIps[-1]
        print('Last known public IP address: ' + lastIp)
        if (lastIp == currIp):
            print('Current public IP address matches last known public IP address')
            print('Nothing to do  - exiting')
            exit()

    print('Recording current public IP address')
    store.write(getIp() + '\n')

    print('Reporting update')
    reportUpdate(currIp, 'email')
