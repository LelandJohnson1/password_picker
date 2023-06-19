import random
import string


adj = [
    "crispy",
    "blue",
    "spicy",
    "funny",
    "powerful",
    "faithful",
    "happy",
    "sad",
    "excited",
    "timid",
    "wild",
]
noun = [
    "man",
    "dog",
    "house",
    "car",
    "movie",
    "team",
    "shoe",
    "sock",
    "fan",
    "computer",
    "tile",
    "whopper",
    "cop",
    "warrior",
]


restart = "y"

while restart == "y":
    print("I will make a password for you!")

    num = random.randrange(0, 1000)
    punc = random.choice(string.punctuation)
    password = random.choice(adj) + random.choice(noun) + str(num) + str(punc)

    print("Your Password is " + password)
    restart = input("Would you like to change password? (y/n)")
