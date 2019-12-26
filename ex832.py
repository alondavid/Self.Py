#EX 8.3.2

ex_dict = {'first_name': 'Mariah', 'last_name':'Carey',
           'Birth_date':'27.03.1970','hobbies':['Sing','Compose','Act']}
print(ex_dict['first_name'])
print(ex_dict['Birth_date'][3:5])
print(len(ex_dict['hobbies']))
print(ex_dict['hobbies'][-1])
ex_dict['hobbies'].append('Cooking')
ex_dict['Birth_date'] = tuple(ex_dict['Birth_date'].split('.'))

from datetime import date
today = date.today()
isodate = today.strftime('%d.%m.%Y')
iso_date_tuple = tuple(isodate.split('.'))
ex_dict['age'] = (int(iso_date_tuple[2]) - int(ex_dict['Birth_date'][2]) +
       (int(iso_date_tuple[1]) - int(ex_dict['Birth_date'][1])) / 12
        + (int(iso_date_tuple[0]) - int(ex_dict['Birth_date'][0])) / 365)
print('{:5.2f}'.format(ex_dict['age']))
