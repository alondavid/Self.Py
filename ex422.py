#ex 422
# כתבו תוכנית שקולטת מהמשתמש מחרוזת ומדפיסה 'OK' אם היא פלינדרום, אחרת 'NOT'
from_user = input('What will you like to test: ')
from_user = from_user.lower().replace(' ','')
revers_from_user = from_user[-1::-1]
if from_user == revers_from_user:
    print('OK')
else:
    print('NOT')
