name = "Chon"
print(name)

def say_hello():
    print("Hello")
    print("I'm inside")





# call the fn
say_hello()


# data structures -> 114

# array js -> list python
prices = [2, 5, 12, 67, 14]
prices.append(9)

# sum all the prices
print(prices)

total = 0
for price in prices:
    total += price

    print(total)
    

    # dictionary
    me = {
        "name": "James",
        "age": 30,
        "hobbies": [],
        "address": {
            "street": "Sin City",
            "city": "Las Vegas"
        }
    }

    print(me)

    # read
    print(me["name"])

    # warning: reading a key that does not exist
    if "last" in me:
        print(me["last"])


    # modify
    me["age"] = 99

    # add keys
    me["last"] = "Chon"

    print("THE END!")