
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
