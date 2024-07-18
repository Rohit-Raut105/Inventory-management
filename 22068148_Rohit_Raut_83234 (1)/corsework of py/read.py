
def my_header(): 
    '''this function shows the header part of gui'''
    print("\n")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("\t \t \t \t \t \t \t \t \t  Famous Laptop Store")
    print("\n")
    print("\t \t \t \t \t \t \t \t  Hatiban , kathmandu  | 9821108680")
    print("-----------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    

def myfun1():
    """function to show the values present in the dictonary"""
    dictonary = {}
    file = open("abc.txt", "r")
    id_of_laptop = 1
    for data in file:
        data = data.replace("\n", "")
        dictonary.update({id_of_laptop : data.split(",")})
        id_of_laptop += 1
    file.close()
    #print(dictonary)
    return dictonary

def display():
    a=1
    """This function help to show laptops details in a table."""
    text= open("abc.txt","r")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("SN"'\t\t',"Name"'\t\t\t',"Brand"'\t\t\t',"price"'\t\t',"Quantity available ",'\t'"Processor"'\t\t',"Graphic Card")
    print("------------------------------------------------------------------------------------------------------------------------------------")
    for value in text:
        print(a, "\t\t"+value.replace(",","\t\t"))
        a= a+1
    return value