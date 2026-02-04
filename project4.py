print("Welcome to The Data Analyzer and Transformer Program\n")

while True:
    print("Main Menu:")
    print("1. Input Data ")
    print("2. Display Data Summary (Built-in Functions)")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Functions)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics (Return Multiple Values)")
    print("7. Exit Program")

    choice=int(input("Please enter your choice :"))
    if choice==1:
        data=input("\nEnter data for a 1D array (Separated by spaces) :\n").split(" ")
        arr=[int(i) for i in data]
        print("\nData has been stored successfully\n")

    elif choice==2:
        print("\nData Summary")
        print(f"-Total elements: {len(arr)}")
        print(f"-Minimum Value: {min(arr)}")
        print(f"-Maximum Value: {max(arr)}")
        print(f"-Sum of all Data: {sum(arr)}")
        print(f"-Average Value: {sum(arr) / len(arr)}\n")

    elif choice==3:
        num=int(input("\nEnter a number to calculate it's factorial :"))
        print()
        fact=1
        for i in range(1, num+1):
            fact=fact*i
        print(f"Factorial of {num} is: {fact}\n")

    elif choice==4:
        a=int(input("Enter a threshold value to filter out data above this value :"))
        filter_data=list(filter(lambda x: x>=a, arr))
        filter_data.sort()
        print(f"Filtered Data (values >= {a}): \n{filter_data} \n")

    elif choice==5:
        print("\nChoose Sorting option:")
        print("1. Ascending")
        print("2. Descending\n")

        choice=int(input("Enter your Choice: "))

        if choice==1:
            arr.sort()
            print(f"Sorted Data in Ascending Order:\n{arr} \n")

        elif choice==2:
            arr.sort(reverse=True)
            print(f"Sorted Data in Descending Order:\n{arr}\n")

    elif choice==6: 
        print("\nDataset Statistics")
        print(f"-Minimum Value: {min(arr)}")
        print(f"-Maximum Value: {max(arr)}")
        print(f"-Sum of all Data: {sum(arr)}")
        print(f"-Average Value: {sum(arr) / len(arr)}\n")

    elif choice==7:
        print("\nThank you for using the Data Analyzer and Tranformer program. Goodbye!")
        break

    else:
        print("Enter only 1 to 7")

