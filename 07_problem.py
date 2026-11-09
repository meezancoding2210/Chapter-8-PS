#Write a Python function to remove a given word from a list and strip it from other words at the same time. 



def remove(list, word):
    n = []
    for item in list:
        if not(item == word): # if an item from the list is not equal to the word ie "ry" then,
            n.append(item.strip(word)) #strip "ry" from the item and add it to the new list
    return n #we have to return a new list
                



list = ["apple", "cherry", "kiwi", "berry", "ry"]


print(remove(list, "ry"))
