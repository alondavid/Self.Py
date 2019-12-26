#ex422
#כתבו תוכנית שמקבלת מהמשתמש תאריך במבנה dd/mm/yyyy ומדפיסה את היום בשבוע עבור התאריך שהוזן

import calendar
calendar.setfirstweekday(calendar.SUNDAY)
days_dict = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
user_date = input(' Enter a date: ')
year = int(user_date[6:])
month = int(user_date[3:5])
day = int(user_date[0:2])
#asked_day = calendar.weekday(year, month, day)
print(days_dict[calendar.weekday(year, month, day)])
