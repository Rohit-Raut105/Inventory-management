import read


def dictonary_update_sell(pc_id,list,laptop_quantity):
    """This function help to update dictionary on sell """
    file=read.myfun1()
    for a in file.keys():
        if pc_id== a:
            quantity= int(file[pc_id][3])
            if  laptop_quantity<= quantity:
                file[pc_id][3] = str(quantity - laptop_quantity)#quantity update in dectonary
                price =  laptop_quantity* int(file[pc_id][2].replace("$",""))
                list.append([file[pc_id][0],file[pc_id][1],file[pc_id][2],price,laptop_quantity])

    return file

def dictonary_update_purchase(laptop_quantity,list,pc_id):
    """This function help to update dictionary on sell """
    file=read.myfun1()
    for a in file.keys():
        if pc_id== a:
            quantity= int(file[pc_id][3])
            print('your values have been update to :',quantity + laptop_quantity)
            file[pc_id][3] = str(quantity + laptop_quantity)#quantity update in dectonary
                
            price =  laptop_quantity* int(file[pc_id][2].replace("$",""))
            list.append([file[pc_id][0],file[pc_id][1],file[pc_id][2],price,laptop_quantity])
    return file

def validation_lp_num(dict):
    """This  function checks validaton of laptop id input by user"""
    vaidation_loop = True
    v_values= list(dict.keys())
    pause= v_values[-1]
    while vaidation_loop:
        try:
            laptop_id= int(input("which id laptop you want to buy: "))
        except ValueError as num:
            print("please give integer value.")
        else:
            if laptop_id <= 0:
                print("please give us valid id! ")
            elif 0<= laptop_id<=pause:
                vaidation_loop= False
            else :
                print("please give us valid input")
    return laptop_id

def quantity_validation(dict,laptop_id,input_from_user):
    """ this function is checks validation of quantity"""
    word_loop = True
    while word_loop:
        try:
            quantity_of_laptop= int(input("Enter the quantity of laptops you want to purchase: "))
        except ValueError as a:
            print("please give valid id")
        else:
            quantity_avaiable = int(dict[laptop_id][3])
            if input_from_user  ==1:
                if quantity_of_laptop <=0:
                    print("Sorry but this stock can't be updated!!!!!")
                else:
                    word_loop=False
            elif input_from_user ==2:
                if quantity_avaiable >= quantity_of_laptop:
                    word_loop = False
                else:
                    print("There is only ",quantity_avaiable, " stocks available. ")
    return quantity_of_laptop
            
def loop(loop):        
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




        

