#@Author : Sudip Mitra
#Email : sudipmitraonline@gmail.com

def swap_case(s):
    a = ""
    for let in s:
        if let.isupper() == True:
            a+=(let.lower())
        else:
            a+=(let.upper())
    return a
    
s = input("Enter the string :")
result = swap_case(s)
print("You Entered : {0}".format(s))
print("Revised String : ",result)
