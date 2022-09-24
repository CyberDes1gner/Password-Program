realPassword = 'Password123'
realUserName = 'Cyber'
userName = input('Please Enter User Name to Gain Access: ')
userPassword = input('Please Enter Password To Gain Access: ')

while realPassword != userPassword and realUserName != userName:
    userName = input('Wrong Username please retry: ' )
    userPassword = input('Wrong password. Please Retry: ')
print('You Have Been Given Access')
