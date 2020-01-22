# 1
def halved(arr):
    filteredList = []
    
    for num in arr:
        filteredList.append(num/2)
    
    return filteredList
    
# 2 
def only_positive(arr):
    filteredList = []
    
    for num in arr:
        if num > 1:
            filteredList.append(num)
    return filteredList

# 3
def Sum(arr):
    ourSum = 0
    for num in arr:
        ourSum += num
    
    return ourSum

# 4
# def stripped_strings(arr):
#     for letter in arr
#         #use charCode




#5 
def find_special(arr):
    for word in arr:
        if word == 'special':
            return arr.index(word)

# 6
def valid_contacts(contacts):
    for contact in contacts:
        