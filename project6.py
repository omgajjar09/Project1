import datetime

print("\n--- Welcome to Personal Journal Manager! ---\n")

class journal:
    def __init__(self,filename="journal.txt"):
        self.filename=filename

    def add_entry(self,entry):
        self.entry=entry
        now=datetime.datetime.now()
        timestamp=now.strftime("%d-%m-%Y %H:%M:%S")

        try:
            with open(self.filename,"a") as file:
                file.write(f"[{timestamp}]\n{entry}\n")
                file.write("\n")

            print("\nEntry added Successfully!\n")

        except PermissionError:
            print("\nError : permissionError denied while writing to file.\n")

    def view_entry(self):
        
        try:
            with open(self.filename,"r") as file:
                data=file.read()
                if data.strip():
                    print("\nYour Journal Entries:")
                    print("-"*30)
                    print(data.strip(),"\n")
                else:
                    print("\nNo journal entries found. Start by adding a new entry!\n")

        except FileNotFoundError:
            print("\nError : The journal file does not exist. Plese add a new  entry first.\n")

    def search_entry(self,search):
        self.search = search

        try:
            with open(self.filename, "r") as file:
                content = file.read()

            entries = content.strip().split("\n\n")  
            found = False

            print("\nMatching Entries:")
            print("-" * 30)

            for entry in entries:
                if self.search in entry:
                    print(entry)
                    print()
                    found = True

            if not found:
                print(f"\nNo entries were found for the keyword: {self.search}\n")

        except FileNotFoundError:
            print("\nError: The journal file does not exist. Please add a new entry first.\n")


    def delete_entry(self,confirm):
        self.confirm=confirm

        try:
            if self.confirm=="yes":
                with open(self.filename,"w") as file:
                    content=file.write(" ")
                    print("\nAll journal entry have been deleted.\n")

            else:
                print("\nNo Journal entries to delete.\n")

        except FileNotFoundError:
            print("\nError : File Not Found.\n")


jobj=journal()

while True:
    print("please select an option:")
    print("1. Add a New Entry")
    print("2. View All Entries")
    print("3. Search for an Entry")
    print("4. Delete All Entries")
    print("5. Exit")

    choice=int(input("Enter Your Choice :"))

    if choice==1:
        entry=input("\nEnter Journal Entry :\n")
        jobj.add_entry(entry)

    elif choice==2:
        jobj.view_entry()

    elif choice==3:
        search=input("\nEnter a keyword to search :")
        jobj.search_entry(search)

    elif choice==4:
        confirm=input("\nAre you sure you want to delete all entries? (yes/no) :")
        jobj.delete_entry(confirm)

    elif choice==5:
        print("\n Thank you for using Personal Journal Manager. Goodbye!\n")
        break

    else:
        print("\nInvalid option. Please select a valid option from the menu.\n")
