##what is list in python
my_list = [10, "apple", 3.14, True]

##how do you create a empty list
empty1 = []  
empty2 = list()

##how do you acces list elament
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
print(fruits[-1])  # cherry (last element)

##how do you update value in a list
nums = [1, 2, 3, 4]
nums[1] = 20
print(nums)  # [1, 20, 3, 4]

##how do you add a element to a list (append,insert)
nums = [1, 2]
nums.append(3)        # [1, 2, 3]
nums.insert(1, 5)     # [1, 5, 2, 3]

##how to remove elament from a list (remove(value),pop(index),del)
nums = [1, 2, 3, 2]
nums.remove(2)    # removes first 2 → [1, 3, 2]
nums.pop(1)       # removes index 1 → [1, 2]
del nums[0]       # removes index 0 → [2]

##how to check if the element if an item exist in a list
fruits = ["apple", "banana"]
print("apple" in fruits)   # True
print("grape" not in fruits) # True

##how do you loop through a list
fruits = ["apple", "banana", "cherry"]

for f in fruits:
    print(f)
    
##list slicing
    nums = [10, 20, 30, 40, 50]
print(nums[1:4])   # [20, 30, 40]
print(nums[:3])    # [10, 20, 30]
print(nums[-2:])   # [40, 50]

##how do you sort a list
nums = [3, 1, 4, 2]
nums.sort()
print(nums)  # [1, 2, 3, 4]

nums.sort(reverse=True)
print(nums)  # [4, 3, 2, 1]

##how copy a list
list1 = [1, 2, 3]
list2 = list1.copy()
print(list2)  # [1, 2, 3]

##what is a list comprehension
squares = [x*x for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]



