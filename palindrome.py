string = input ("Enter a String: ")
list = list(string)

copy_list = list.copy()
copy_list.reverse()

if (copy_list==list):
    print("Plindrome")

else:
    print("Not Palindrome")
    

