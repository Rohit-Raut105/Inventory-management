import read 
import Write
import Operation
import datetime
import random

def option_for_users():
    """This function ask user to sell, buy or purches ."""
    lopp = True
    while lopp == True:
        print("Select your Options to continue")
        print("press 1 to Purchase ")
        print("print 2 for Sell ")
        print("Press 3 for Exit ")
        numberloop= True
        while numberloop:
            try:#Applying Exception Handeling to handel error.
                input_from_user = int(input("Enter the option to Continue: "))
            #Except Value Error and suitable message .
            except ValueError as e: 
                print("Enter a numeric value")
            else:
                numberloop=False
        print("\n")
        #This loop is for purchase.
        if input_from_user == 1:
            read.display()
            print("------------------------------------------------------------------------------------------------------------------")
            stringloop=True
            while stringloop:
                user_name = str(input("Enter your Name : "))
                try:
                    if user_name.isalpha():
                        break
                    else:
                        raise ValueError("please give string value to continue")
                except ValueError as f:
                    print(f"error:{f}")
                else:
                    stringloop = False
            dict = read.myfun1()
            list=[]# A list is decleared to store values .
            loop = True
            while loop == True:
                test= True
                while test:
                    try:
                        laptop_id=int(input("Which Id laptop do you want to buy :  "))
                    except ValueError:
                        print("Enter a numeric value")
                    else:
                        if 0<laptop_id<len(dict):
                            test=False
                
                quantity_of_laptop=Operation.quantity_validation(dict,laptop_id,input_from_user)
                dict=Operation.dictonary_update_purchase(quantity_of_laptop,list,laptop_id)                             
                Write.update_text(dict)
                loop_1 = True
                while loop_1:
                    ask_again= str(input("Do you want to buy again : "))
                    print("-----------------------------------------------------------------------")
                    if ask_again =='y':
                        loop_1=False
                        loop = True
                    elif ask_again == 'n':
                        loop_1= False
                        loop= False
                    else:
                        print("Inappropriate value")
            bill_no= random.randint(0,500)
            date=datetime.datetime.now().strftime("%d/%m/%Y")
            time=datetime.datetime.now().strftime("%H:%M:%S")
            Write.biil_for_purches(time,list,date,bill_no,user_name)
            Write.bill_text_purches(date,time,user_name,bill_no,list)
            print("\n")
            print("Thankyou for you colobration.")

        #This loop is for sell.    
        elif input_from_user==2:
            read.display()
            print("---------------------------------------------------------------------------------------------------------------------------------------")
            loop = True
            stringloop=True
            while stringloop:
                user_name = str(input("Enter your Name : "))
                try:
                    if user_name.isalpha():
                        break
                    else:
                        raise ValueError("please give string value to continue")
                except ValueError as f:
                    print(f"error:{f}")
                else:
                    stringloop = False
            stringloop1=True
            while stringloop1:
                address = str(input("Enter your address: "))
                try:        
                    if address.isalpha():
                        break
                    else:
                        raise ValueError("The string contains non-alphabetical characters.")
                except ValueError as f:
                    print(f"error:{f}")
                else:
                    stringloop1 = False
            numloop= True
            while numloop:
                    try:
                        contact_num=int(input("enter your contact number: "))
                    except ValueError:
                        print("Enter a numeric value")
                    else:
                        numloop=False
            #Create list to store value 
            list = []
            while loop:
                check = True
                valid_id= True
                dict=read.myfun1()
                while valid_id:
                    laptop_id=Operation.validation_lp_num(dict)
                    print(f"Available stocks {dict[laptop_id][3]} only")
                    if int(dict[laptop_id][3]) == 0 :
                        print("No stocks")
                        loop_1= True
                        while loop_1:
                            ask_again= str(input("Do you want to buy again : "))
                            if ask_again =='y':
                                loop_1=False
                                valid_id = True
                            elif ask_again == 'n':
                                loop_1= False
                                valid_id= False
                                a= False
                            else:
                                print("Inappropriate value")
                    else:
                        valid_id=False
                if check == False:
                    break
                else:  
                    quantity_of_laptop =Operation.quantity_validation(dict,laptop_id,input_from_user)
                    dict=Operation.dictonary_update_sell(laptop_id,list,quantity_of_laptop)
                    Write.update_text(dict)
                    loop_1= True
                    while loop_1:
                        ask_again= str(input("Do you want to buy again : "))
                        if ask_again =='y':
                            loop_1=False
                            loop = True
                        elif ask_again == 'n':
                            loop_1= False
                            loop= False
                        else:
                            print("Inappropriate value")
            if len(dict)!=0:
                bill_no= random.randint(0,500)
                date=datetime.datetime.now().strftime("%d/%m/%Y")
                time=datetime.datetime.now().strftime("%H:%M:%S")
                Write.bill_for_sell(list,address,contact_num,bill_no,date,time,user_name)
                Write.bill_text_for_sell(list,bill_no,date,address,contact_num,time,user_name)
                print("\n")
                print("Thankyou for you colobration.") 

        elif input_from_user== 3:
            loop = False
            print("Thankyou for you valuable Time ")
            print("\n")
        else:
            print("The option you entered",input_from_user,"do not match our system")
            print("\n")
    return input_from_user
option_for_users() 