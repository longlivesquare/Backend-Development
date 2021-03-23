# Input: a list
# Output: The list with all duplicates removed
# remove_duplicate will remove any duplicates in a passed in list
def remove_duplicate(myList):
    # A dictionary is used to keep track of when we encounter an item in the list
    # Since keys are not duplicated, this means it will do our job for us
    myDict = {}
    for name in myList:
        # Set the key 'name' to True. The value it is assigned is somewhat arbitrary
        # I just needed it so the dictionary would have the key
        myDict[name] = True
        # The keys function returns just the (unique) keys of the dictionary. The list function makes
        # it a true list
    return list(myDict.keys())

names = ['Tom', 'Jerry', 'Francine', 'Tom', 'Bob', 'Smith', 'Mary', 'Mary', 'John', 'Tom']
print(remove_duplicate(names))