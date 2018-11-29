
def getChange(cost, amount):
    cost = input("Enter the cost: ")
    amount = input("Enter the amount: ")
    change = float(amount) - float(cost)
    print("the change is: ", float(change))
    if change >= 10:
        get_ten = change / 10
    print("the number of coin of ten sek is : ", int(get_ten))

    #get_five = (change - (get_ten * 10)) / 5
    #get_two = (change - (get_ten * 10) - (get_five * 5)) / 2
    #get_one = (change) - (get_ten *10) - (get_five *5) -(get_two *2) / 1)

getChange(cost, amount)
