
date_us = (input('Please enter date in MM/DD/YYYY format: '))

if len(date_us) == 10:
    date_world = date_us[3:5]+'.'+date_us[0:2]+'.'+date_us[6:]
    print('Here is the formatted date:',date_world)

elif len(date_us) == 9 and date_us[2] != '/':
    date_world = date_us[2:4]+'.'+'0'+date_us[0]+'.'+date_us[5:]
    print('Here is the formatted date:',date_world)

elif len(date_us) == 9 and date_us[1] != '/':
    date_world = '0'+date_us[3]+'.'+date_us[0:2]+'.'+date_us[5:]
    print('Here is the formatted date:',date_world)

else:
    date_world = '0'+date_us[2]+'.'+'0'+date_us[0]+'.'+date_us[4:]
    print('Here is the formatted date:',date_world)
