#converts user input in seconds to hrs/min/sec


sec = int(input("Please enter the number of seconds:"))
min = 0
hour = 0

#assigns string values
secStr = 'seconds'
minStr = 'minutes'
hourStr = 'hours'


if (sec >= 3600):
    hour = sec // 3600
    sec = sec % 3600
if sec >= 60:
    min = sec // 60
    sec = sec % 60

if sec == 1:
    secStr = 'second'
if min == 1:
    minStr = 'minute'
if hour == 1:
    hourStr = 'hour'

if hour > 0 and min == 0 and sec == 0:
    print(hour, hourStr, end = '\n')
elif hour > 0:
    print(hour, hourStr, end = ' ')
if min > 0 and sec == 0:
    print(min, minStr, end = '\n')
elif min > 0:
    print(min, minStr, end = ' ')
if sec > 0:
    print(sec, secStr, end = '\n')
if (hour == 0 and min == 0 and sec == 0):
    print('0 seconds')


                



