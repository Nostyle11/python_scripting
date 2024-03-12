# we declare a dictionary for flowers
flowersDict = {}

global fname

# we create a function to open flowers.txt
# and put alphabets as key and flower names as values
# in the dictionary declared
def flowerListing(flower):
    with open(flower) as f:
        for line in f:
            
            sep = line.split(": ")
            flowersDict.update({sep[0]:sep[1].split("\n")[0]})
            
    return  flowersDict

# calling flower function with the text file as an arguement
flowerListing("flowers.txt")

# we create a function to ask for user's first and last name
def userReq():
    global fname
    firstname = input("Input your first name : ")
    lastname = input("Input your last name : ")

    # assigning users first name to variable fname
    fname = firstname

# calling user request function   
userReq()

# assigning first letter of user firstname to fletter
fletter = fname[0]

# a for loop to print out the matching flower to the username
for key, value in flowersDict.items():
    if fletter.upper() == key :
        print(f"Unique flower name with the first letter: {value}")
