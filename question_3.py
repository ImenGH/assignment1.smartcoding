#An ICA supermarket attendant works every day selling to customers. 
#They have a business where each item you buy,
#mjolk, Pannkakor, Bröd, Paj, and everything there costs a positive number of Kroner (integers).
#If bröd costs 22 kroner. There is no item in ICA that costs a decimal value like 10.13 kr 
#(VAT tax is included in the amount already).
#Kroner change can be provide in 1 kr, 2kr, 5kr and 10kr. 


def getChange(cost, amount):
    change = amount - cost
    print("the change is: ", change)
    coins_of_10 = int(change / 10)
    print("the number of coin of ten sek is : ", coins_of_10)
    change = change - (10 * coins_of_10)
    if change >= 0:
        coins_of_5 =  int(change / 5)
        print("the number of coin of five sek is : ", coins_of_5)
        change =  change - (5 * coins_of_5)
        if change >= 0:
            coins_of_2 =  int(change / 2)
            print("the number of coin of two sek is : ", coins_of_2)
            change =  change - (2 * coins_of_2)
            if change >= 0:
                coins_of_1 = int(change / 1)
            print("the number of coin of one sek is : ", coins_of_1)
            change = change - (1 * coins_of_1)



getChange(10, 100)
getChange(15, 50)
getChange(13, 50)
getChange(5, 8)
