#ex 423

temparture = input('Insert the temperature you would like to convert: ')
sign = temparture[-1].lower()
if len(temparture) > 2:
    temparture_number = float(temparture[:-1])
    if sign == 'c':
        final_calc = ((9 * temparture_number) + 160) / 5
        print(str(final_calc) + 'F')
    else:
        final_calc = ((5 * temparture_number) - 160) / 9
        print(str(final_calc) + 'C')
    
else:
    print('Error')
