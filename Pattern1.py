"""
Pattern 1
* 
* * 
* * * 
* * * * 
* * * * * 
(n times)
"""

n = input("Enter the number of rows you want to print.\n")
for i in range(int(n)):
    for j in range(i + 1):
        print("* ", end="")
    print("\r")
