#Compares the numbers in list1 and list2
#return the number that is not in list1
  
def missing_number(alist1, alist2):

    if alist1 == alist2:
        return 0
    else:
        #Looking if a number is not in both list
        for number in alist2:
            if number not in alist1:
                return number

print(missing_number([1,2], [1,2]))
print(missing_number([1,2], [1,2,3]))

