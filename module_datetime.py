import datetime
import pytz

# datetime only includes year, month & day
print(f"datetime: {datetime.date(2021, 8, 25)}\n")

tday = datetime.date.today()

print(f"datetime today: {tday}\n")  # print current date

# access attributes of datetime instance possible
print(f"datetime today the year: {tday.year}\n")

tdelta = datetime.timedelta(days=7)
# operations with datetime & timedelta equals a datetime
print(f"datetime + 7 days: {tday + tdelta}\n")

bday = datetime.date(2021, 10, 25)
till_bday = bday - tday  # operations with datetime & datetime equals a timedelta
print(f"timedelta till bday: {till_bday}\n")
print(f"timedelta days till bday: {till_bday.days}\n")
print(f"timedelta total seconds till bday: {till_bday.total_seconds()}\n")

# time only includes in this order hours, minutes, seconds & microseconds
print(f"time: {datetime.time(9, 45, 30, 100000)}\n")

dt = datetime.datetime(2021, 8, 25, 9, 45, 30, 100000)
print(f"datetime: {dt}\n")  # combines date & time
print(f"datetime get date: {dt.date()}\n")  # get date from datetime
print(f"datetime get date: {dt.time()}\n")  # get time from datetime
print(f"datetime get year: {dt.year}\n")  # get attributes possible
print(f"datetime + 7 days: {dt - tdelta}\n")  # operations possible

print(f"datetime today: {datetime.datetime.today()}")  # no timezone specified
# timezone possible, default is None then identical to today
print(f"datetime now: {datetime.datetime.now()}")
# unlike the name suggest timezone is None
print(f"datetime utcnow: {datetime.datetime.utcnow()}\n")

dt = datetime.datetime(2021, 8, 26, 9, 30, 45, tzinfo=pytz.UTC)  # utc enabled
print(f"datetime with utc: {dt}\n")

# get todays date with utc
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(f"dt now: {dt_now}\n")

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(f"dt utcnow: {dt_utcnow}\n")

dt_berlin = dt_utcnow.astimezone(pytz.timezone("Europe/Berlin"))
print(f"dt berlin: {dt_berlin}\n")

# print all possible timezones
# for tz in pytz.all_timezones():
#     print(tz)

# convert naive datetime to utc datetime
dt_berlin = datetime.datetime.now()
# Note: only works if naive instance is system local time
dt_berlin_utc = dt_berlin.astimezone(pytz.timezone("Europe/Berlin"))
print(f"1. naive datetime to utc: {dt_berlin_utc}")

# otherwise localize needed
dt_berlin_utc = pytz.timezone("Europe/Berlin").localize(dt_berlin)
print(f"2. naive datetime to utc: {dt_berlin_utc}\n")

# formatting
print("formatting:")
print(dt.strftime("%B %d, %Y"))
print("the month {0:%B} in the year {0:%Y}\n".format(dt))

# parse string to datetime
dt_str = "August 26, 2021"
dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print(f"parse string to datetime {dt}")

dt_str = "the month August in the year 2021"
dt = datetime.datetime.strptime(dt_str, "the month %B in the year %Y")
print(f"parse string to datetime {dt}")
