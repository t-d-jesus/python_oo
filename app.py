from models.restaurant import Restaurant

def main():
    # Create restaurant objects
    restaurant1 = Restaurant('Taco Bell', 'Fast Food')
    restaurant2 = Restaurant('McDonald\'s', 'Fast Food')
    restaurant3 = Restaurant('Pizza Hut', 'Fast Food')


    # Print the list of restaurants
    print('List of Restaurants:')

    restaurant1.receive_rating('Customer1',1)
    print('\n','-'*5,'First run','-'*5,'\n')
    Restaurant.list_restaurants()


    restaurant2.receive_rating('Customer1',1)
    restaurant2.receive_rating('Customer2',2)
    print('\n','-'*5,'Second run','-'*5,'\n')
    Restaurant.list_restaurants()


    restaurant3.receive_rating('Customer1',1)
    restaurant3.receive_rating('Customer2',2)
    restaurant3.receive_rating('Customer3',3)
    print('\n','-'*5,'Third run','-'*5,'\n')    
    Restaurant.list_restaurants()




if __name__ == "__main__":
    main()