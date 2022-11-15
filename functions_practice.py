#function to greet the user with no parameters
def hello():
    print('Hello and Welcome')
hello()

#function that accepts three arguments and returns a single list with elements insidet
def pack(arg1,arg2,arg3):
    return(f"['{arg1}','{arg2}','{arg3}']")

single_list=pack("Bacon","Lettuce","Tomatoes")
print(single_list)

#function to accept a list of any length and return comments based on elements passed
def eat_lunch(food_items):
    if not food_items:

        print("My lunchbox is empty")
    else:
        print(f"First I eat {food_items[0]}")
        if len(food_items)>1:
            for i in range(1,len(food_items),1):
                print(f"Next I eat {food_items[i]}")
# an empty list
food0=[] 
eat_lunch(food0)

# a list with only 1 item
food1=["Ham and Eggs"]
eat_lunch(food1)

# a list with two items
food2=["Ham and Eggs","Cheese and Grapes"]
eat_lunch(food2)

# a list with three items
food3=["Ham and Eggs","Cheese and Grapes","A Beefy Burrito"]
eat_lunch(food3)