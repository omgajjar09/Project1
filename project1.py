print("Welcome to the Interactive Personal Data Collector!\n")

name=input("Please Enter Your Name :")
age=int(input("Please Enter Your Age :"))
height=float(input("Please Enter Your Height in meters :"))
fnum=int(input("Please Enter Your Favourite Number :\n"))

print("Thank you! Here is the information we collected:")

print(f"Name : {name}  (Type: {type(name)} Memory Address: {id(name)}")
print(f"Age : {age}  (Type: {type(age)} Memory Address: {id(age)}")
print(f"Height : {height}  (Type: {type(height)} Memory Address: {id(height)}")
print(f"Favourite Number : {fnum}  (Type: {type(fnum)} Memory Address: {id(fnum)}\n")

print(f"Your birth year is approximately :{2025-age} (based on your age of {age} )\n")
print("Thank you for using the personal Date Collector. Goodbye")
