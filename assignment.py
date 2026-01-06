lst = [10, 20, 30, 40]
total = sum(lst)
print(total)

lst = ["apple", "banana", "guava"]
lst.reverse()
print(lst)

# if 2 functions have common element then return true 
func1 = [1, 2, 3, 4]
func2 = [5, 3, 8, 9]


def have_comman_element(func1, func2):
    for element in func1:
        if element in func2:
            return True
    return False
    
result = have_comman_element(func1, func2)
print(result)    

#

