# Design a phone book program. In this program, we can think of a phone book as a collection of friends,
#associates, family with their information such as a telephone number, email address, name and location.
#Design a simple program that gets the names from a random list like:

#names = [‘peter’, ‘mary’, ‘jane’] location = [‘stockholm’, ‘goteborg’, ‘helsingborg’] 

#This is my answer:
#                 def phoneBook(names, location):    
#                       return dict(zip(names, location)) 

#Please design an algorithm, that will create key value pairs of name and location at the end, use constructs like for-loops.
#(Optional) Extra credit: You can make your application return data or output that looks fancier:

#{‘peter’: { ‘location’: ‘stockholm’}, ‘mary’: { ‘location’: ‘goteborg’}, ‘jane’: { ‘location’: ‘helsingborg’}


def phone_book(names, location, phone_numbers):
    
    my_dict = {} # create an empty dictionairy
    name_lengh = len(names) # lengh of the liste <name>
    
    # the dictionary  my_dict take name[i] as a key 
    for i in range(0, name_lengh):
        my_dict[names[i]] = {'location': location[i], 'phone_numbers': phone_numbers[i]}
    print(my_dict)
    
    


names = ['Jane', 'Mary', 'Paul'] #liste of name
location = ['Stockholm', 'Upsala', 'Malmo'] #liste of location
phone_numbers = ['0725364205', '0785001465', '0744628794'] #liste of phone number
phone_book(names, location, phone_numbers) #call the function
