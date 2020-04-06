# issue-reporter
Uses the github API to watch for new issues in the repo https://api.github.com/repos/omxhealth/a-a-interview/issues

- watches for new issues and reports them (with title, id, other info if you like, but fairly compact)
- reports issues being closed (with same info as above)
- whenever an issue is added/closed, reports the number of total existing/closed issues, but does not show details of the other issues


## Setup
Requests module is required for script to run. To install this module issue the following command:

    pip install requests

To run the script issue the command:

    python3 reporter.py
