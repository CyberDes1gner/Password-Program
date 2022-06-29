realPassword = 'Password123'
userPassword = input('Please Enter Password To Gain Access: ')

while realPassword != userPassword:
    password = input('Wrong password. Please Retry: ')
    if password == 'Password123':
        print('You Have Been Given Access')
