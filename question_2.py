def phone_book(names, location, phone_numbers):
    my_dict = {}
    name_lengh = len(names)
    for i in range(0, name_lengh):
        #print(x)
        my_dict[names[i]] = {'location': location[i], 'phone_numbers': phone_numbers[i]}
    print(my_dict)
    #z = dict(my_list)
    #print(z)


names = ['Jane', 'Mary', 'Paul']
location = ['Stockholm', 'Upsala', 'Malmo']
phone_numbers = ['0725364205', '0785001465', '0744628794']
phone_book(names, location, phone_numbers)
