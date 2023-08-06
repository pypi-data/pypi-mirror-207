import time, asyncio, pytz, datetime
from datetime import datetime

def tgap(t):
    time.sleep(t)

def agap(t):
    asyncio.sleep(t)

def currenttime():
    now = datetime.now()
    currenttime = now.strftime("%H:%M:%S")
    return currenttime

def _m(timezone):
    chennai_tz = pytz.timezone(timezone)
    now = datetime.datetime.now(chennai_tz)
    am_pm = now.strftime("%p")
    return am_pm

def zonetime(timezone):
    tz = pytz.timezone(timezone)
    current_time = datetime.now(tz)
    time_12hr_format = current_time.strftime("%I:%M:%S %p")
    return time_12hr_format
