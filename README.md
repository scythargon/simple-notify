## Simplest free hard drive space notifier.

**Periodically checks root (/) free space and notifies your Slack channel.**

Run options:

```
SPACE_LIMIT - int (GB)
PERIOD_UNITS - str (seconds/minutes/hours/days)
CHECK_PERIOD - int
DRYRUN - if set - skip slack credentials check and don't really
    send out anything, just print to stdout.
```

### Run example:

`docker run -e SLACK_BOT_TOKEN=... -e SLACK_CHANNEL=... -e SPACE_LIMIT=... -e CHECK_PERIOD=... -e PERIOD_UNITS=... -e DRYRUN=true scythargon/simple-notify`

### Run locally after git clone:
(install python requirements)

(tested on Python 3.6.9)

`SLACK_BOT_TOKEN=... SLACK_CHANNEL=... SPACE_LIMIT=... CHECK_PERIOD=... PERIOD_UNITS=... DRYRUN=true ./main.py`

