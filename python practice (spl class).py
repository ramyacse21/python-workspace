# #1
# name="ramya"
# #i want to print my name 1st letter in uppercase 2nd letter in lowercase 3rd letter in uppercase and so on
# result = 0
# for i in range(len(name)):
#     if i % 2 == 0:
#         result += name[i].upper()
#     else:
#         result += name[i].lower()
# print(result)                       #Output: RaMyA

# #2
# text = "ramya123"
# result = ""

# for mi in text:
#     if 'a' <= mi <= 'z':          # check lowercase
#         result += chr(ord(mi) - 32)  # convert to uppercase
#     else:
#         result += mi               # keep numbers same

# print(result)   #Output: RAMYA123

# #3 # Password validation
# password = input("Enter password: ")

# has_upper = False
# has_lower = False
# has_digit = False
# has_special = False

# # Check each character
# for ch in password:
#     if 'A' <= ch <= 'Z':
#         has_upper = True
#     elif 'a' <= ch <= 'z':
#         has_lower = True
#     elif '0' <= ch <= '9':
#         has_digit = True
#     else:
#         has_special = True

# # Final validation
# if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
#     print("Valid Password")
# else:
#     print("Invalid Password")

# #4 Square pattern
# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print()

#import random
# for i in range(5):
#     a = random.randint(1, 100)
# print(a)             #Output: 42 (example output, will vary each time)


# email=input("Enter your email: ")
# at_count=0
# ap_count=0
# for i in email:
#     if i=='@':
#         at_count+=1
#     elif i=='.':
#         ap_count+=1
# if at_count==1 and ap_count==1:
#     print("Valid email")
# else:
#     print("Invalid email")
    

#with open(r"C:/Users/admin/Downloads/Ramya_Resume.docx", "rb") as file:
 #   content = file.read()
  #  print(content)
 
 
# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(i, end=" ")
#     print()
#output
#     5 
#     4 4 
#     3 3 3
#     2 2 2 2
#     1 1 1 1 1

# for i in range(5,0,-1):
#     for j in range(5,0,-1):
#         print(j, end=" ")
#     print()
#output
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1
# 5 4 3 2 1

# for i in range(5,0,-1):
#     for j in range(5,i-1,-1):
#         print(j, end=" ")
#     print()
#output
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

#now i want inverse of thiss output
# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print(j, end=" ")
#     print()
#output
# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()            
#output
#1
#1 2 
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1,6):
#     for j in range(1,6):
#         print(i, end=" ")
#     print()
#output
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5

# for i in range(5,0,-1):
#     for j in range(1,i+1):
#          print(i*j, end=" ")
#     print()
#output
# 5 10 15 20 25 
# 4 8 12 16  
# 3 6 9 
# 2 4 
# 1 

# for i in range(1,6):
#     for j in range(1,i+1):
#          print(i*j, end=" ")
#     print()
#output
# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25

# for i in range(1,6):
#     for j in range(5,i-1,-1):
#             print(i*j, end=" ")
#     print()
#output
# 5 4 3 2 1 
# 10 8 6 4 
# 15 12 9
# 20 16
# 25 


# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         if j==i:
#             print("*", end=" ")
#         else:
#             print(j, end=" ")
#     print()
#output
# 1 2 3 4 *
# 1 2 3 *
# 1 2 *
# 1 *
# *


# for i in range(5,0,-1):
#     for j in range(1,6):
#         if j<i:
#             print(" ", end=" ")
#         else:
#             print("*", end=" ")
#     print()
#output
#         *
#       * *
#     * * *
#   * * * *
# * * * * *

name="ramya"
length=len(name)
for i in range(length,0,-1):
    for j in range(0,i):
        print(name[j], end=" ")
    print()
#output
# r a m y a
# r a m y
# r a m
# r a
# r