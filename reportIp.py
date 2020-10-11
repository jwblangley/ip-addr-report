import os
import sys

from requests import get
from dotenv import load_dotenv
from pushbullet import Pushbullet

load_dotenv()

STORE_FILE = "ip-address.txt"


def getIp():
    return get("https://api.ipify.org").text


def reportPushBullet(title, body):
    apiKey = os.getenv("PUSHBULLET_API_KEY")
    if apiKey is None:
        print("Could not locate PUSHBULLET_API_KEY")
        return

    print("Pushing to Pushbullet...", end=" ")
    pb = Pushbullet(apiKey)
    pb.push_note(title, body)
    print("DONE")


def report(title, body, *methods):
    methods = list(methods)
    print("Reporting via: " + ", ".join(methods))

    for method in methods:
        if method == "pushbullet":
            reportPushBullet(title, body)
        else:
            print("Unknown report method: '" + method + "'")


def reportUpdate(currIp, *methods):
    title = "Public IP address of your machine has changed"
    body = "New public IP address: " + currIp

    report(title, body, *methods)


def reportUnchanged(currIp, *methods):
    title = "Machine online"
    body = "Public IP address unchanged: " + currIp

    report(title, body, *methods)


def recordIpInStore(store):
    print("Recording current public IP address")
    store.write(getIp() + "\n")


if __name__ == "__main__":
    # Handle args
    flags = list(filter(lambda s: s.startswith("-"), sys.argv[1:]))
    reportingMethods = list(filter(lambda s: not s.startswith("-"), sys.argv[1:]))

    if len(reportingMethods) == 0:
        print("No reporting methods specified")
        exit(1)

    reportIfUnchanged = "-u" in flags

    # Open file and create if it does not exist
    store = open(STORE_FILE, "a+")
    store.seek(0)

    # Read existing and move cursor to end. Trim trailing new line
    prevIps = store.read().split("\n")[:-1]

    currIp = getIp()
    print("Current public IP address: " + currIp)

    if len(prevIps) == 0:
        print("No known previous public IP addresses")
        recordIpInStore(store)
        reportUpdate(currIp, *reportingMethods)
    else:
        lastIp = prevIps[-1]
        print("Last known public IP address: " + lastIp)

        if lastIp == currIp:
            print("Current public IP address matches last known public IP address")
            if reportIfUnchanged:
                reportUnchanged(currIp, *reportingMethods)
            else:
                print("Nothing to do - exiting")
        else:
            recordIpInStore(store)
            reportUpdate(currIp, *reportingMethods)

    store.close()
