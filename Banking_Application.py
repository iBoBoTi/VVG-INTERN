customer_acc = {'user1@gmail.com':{'password':'theophilus1','balance':70000}, 'user2@gmail.com':{
    'password':'michael1','balance':200000}}

def home():

    '''Function to get the banking app running'''

    display = input('WELCOME DEAR CUSTOMER...\nPress 1: Create Account\nPress 2: Transaction\n')
    try:
       choice = int(display)
    except:
        choice = -1
        print('wrong input')
    if choice == 1:
        create_acc()
    elif choice == 2:
        make_transc()
    else:
        print('Error')
        home()

def create_acc():

    '''Function to create account as well as test registered email and password'''

    global customer_acc
    print('''creating account...\nNote:\n\tEmail should be of format(name@email.com)
    Password should be more than 6 and, consist of alphabeths and numbers''')
    email = input('register your email: ')
    password = input('register your password: ')
    def email_test():

        '''Fuction to test email structure'''

        if '@' in email and '.com' in email:
            print('done')
        else:
            print('Ensure your email is of format(name@email.com)')
            create_acc()
    def password_test():

        '''Function to test password structure'''

        if password.isalnum() and len(password)>=6:
            print('done')
        else:
            print('Ensure password consist alphabeth and numbers and it not less than 6 characters')
            create_acc()
    email_test()
    password_test()
    if email in customer_acc:       #testing if user already exist
        print('customer already exist')
        home()
    else:
        customer_acc[email] = {'password':password,'balance':0.0}
        print(customer_acc)
        make_transc()



def make_transc():
    global auth_user
    auth_user = input('enter email: ')
    auth_password = input('enter password: ')
    #Authenticating user
    if auth_user in customer_acc and auth_password == customer_acc[auth_user]['password']:
        print('Successfully Logged in')
        display = input('Press 1: Check Balance\nPress 2: Deposit\nPress 3: Withdraw\nPress 4: Transfer\nPress 0: Make '
                            'Transaction\n')
        #testing transaction input
        try:
            transc_option = int(display)
        except:
            transc_option = -1
            print('wrong input')
        if transc_option == 1:
            print(check_bal())
        elif transc_option == 2:
            make_deposit()
            print('deposit made')
        elif transc_option == 3:
            withdraw()
            print('please take your money')
        elif transc_option == 4:
            transfer()
            print('transaction made')
        elif transc_option == 0:
            make_transc()
        else:
            print('Error')
            home()
    else:
        print('Unsuccessful!, Data does not exist! Create Account')
        create_acc()

def check_bal():
    '''Balance Check of a logged in customer or authorised customer'''
    print('checking balance')
    return customer_acc[auth_user]['balance']
def make_deposit():
    display = input('enter deposit amount: ')
    try:
       deposit = int(display)
       # creating new balance
       customer_acc[auth_user]['balance'] = int(customer_acc[auth_user]['balance']) + deposit
       print(check_bal())   # print new balance
    except:
        deposit = -1
        print('wrong input')
        make_deposit()
def withdraw():
    display = input('enter withdrawal amount: ')
    try:
       withdrawal = int(display)
       # creating new balance
       if withdrawal <= customer_acc[auth_user]['balance']:
           customer_acc[auth_user]['balance'] = int(customer_acc[auth_user]['balance']) - withdrawal
           print('total money withdrawn: ' + str(withdrawal))    # print money withdrawn
           print('Your new balance is: ')
           print(check_bal())   # print new balance
       else:
           print('insufficient balance')
           make_deposit()    #take us to make deposit
    except:
        withdrawal = -1
        print('wrong input')
        withdraw()   # in the case of wrong input, request for another input
def transfer():
    user_destination = input('enter email destination: ')
    if user_destination in customer_acc and user_destination != auth_user:
        display = input('enter transfer amount: ')
        try:
            transfer_amount = int(display)
            if transfer_amount <= customer_acc[auth_user]['balance']:
                # change the account balance of the user
                customer_acc[auth_user]['balance'] = customer_acc[auth_user]['balance'] - transfer_amount
                # add the money transferred to the destination user
                customer_acc[user_destination]['balance'] = int(customer_acc[user_destination]['balance']) + transfer_amount
                print('changing user from 70000 to ')
                print(check_bal())
                print('changing destination from 200000 to ')
                print(customer_acc[user_destination]['balance'])
            else:
                print('insufficient fund')
                make_deposit()    #take us to make deposit
        except:
            deposit = -1
            print('wrong input')
            transfer()
    else:
        print('Account does not exist')
        transfer() # when account does not exist request for another input


# while True:  #this loop ensures that when a transaction is made it stays like that still the program exits and begins
#     # again from where it returns to its original state
#     start_up_code = input('enter 1 to start operation: ')
#     if start_up_code == '1':
#         print('Loading...')
#         home()
#     else:
#         print('Sorry enter 1 to start operation')
#         break
# OR
home()
