
import datetime
#import pyt

d = datetime.date(2016, 7, 24)
print(d)

tday = datetime.date.today()
print(tday.year)
print(tday.weekday())
print(tday.isoweekday())

tdelta = datetime.timedelta(days=7)

print(tday + tdelta)

bday = datetime.date(2021, 11, 30)

t_b = bday - tday

print(t_b.days, t_b.total_seconds())

t = datetime.time(9, 30, 45, 100000)

print(t)

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)

#dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000, tzinfo=pytz.UTC)

print(dt.time(), dt.date())
print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
#dt_now = datetime.datetime.now(tz=pytz.UTC)
dt_utcnow = datetime.datetime.utcnow()
#dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
#dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Montain'))

# for tz in pytz.all_timezones:
#     print(tz)

#dt_mtn = datetime.datetime.now()
# mnt_tz = pytz.timezone('US/Mountain')
# dt_mtn = mtn_tz.localize(dt_mtn)
# dt_east = dt_mnt.astimezone(pytz.timezone('US/East'))
#print(dt_east)
#print(dt_mtn.isoformat())
#print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 26, 2016'
dt1 = datetime.datetime.strptime(dt_str, '%B %d, %Y')

print(dt_today)
print(dt_now)
print(dt_utcnow)

print(dt1)
