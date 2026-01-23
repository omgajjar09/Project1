print("Wlecome to the pattern generator and number Analyzer\n\n")

while True:
    print("Select an option")
    print("1.Generate a Patten")
    print("2.Analyzer a Range of Numbers")
    print("3.Exit")
    choice=int(input("Enter the your choice :"))
    print()

    if choice==1:
        row=int(input("Enter the number of Rows for the Patten :"))
        print()
        print("pattern :")
        for i in range(1,row+1):
                print("*"*i)
        print()

    elif choice==2:
        start=int(input("Enter the start of the range :"))
        end=int(input("Enter the end of the range :"))
        for i in range(start,end+1):
            if i%2==0:
                print("Numbre ",i,"is Even")
            else:
                print("Numbre ",i,"is Odd")
        sum=0
        num=start
        while num<=end:
            sum +=num
            num += 1
        print("Sum of all number from ",start," to ",end," is :",sum,"\n\n")
    
    elif choice==3:
        print("Exiting the program. Goodbye")
        break
    else:
        print("Enter only 1 to 3")