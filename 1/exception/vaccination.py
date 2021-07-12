age=int(input('ENTER YOUR AGE '))
if age<=18:
    raise Exception('NOT ELIGIBLE FOR VACCINATION ')
else:
    print('ELIGIBLE FOR VACCINATION ')