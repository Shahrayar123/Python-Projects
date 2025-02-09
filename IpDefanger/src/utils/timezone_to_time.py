def timeZoneToTime(timezone):
    """
    Returns the time of some timezone
    """

    import pytz
    import datetime

    tz = pytz.timezone(timezone)  
    time = datetime.datetime.now(tz)
    return time.strftime("%Y-%m-%d %H:%M:%S %Z%z")