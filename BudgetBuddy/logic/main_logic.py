from pyfiglet import Figlet
from termcolor import colored
import time
from tqdm import tqdm
from logic import encrypt_decrypt as ed
import csv
from tabulate import tabulate
import re

class expense:
    def __init__(self):
        f = Figlet()
        ascii_text = f.renderText("WELCOME TO BUDGET BUDDY")

        print(colored(ascii_text,"red"))

    def generate_ascii_text(self,text,color):
        f = Figlet()
        ascii_text = f.renderText(text)

        return colored(ascii_text,color)
    
    def functions(self):
        functons = [
            "1. Add Expense(ae)",
            "2. View Expense(ve)",
            "3. Create Budget(cb)",
            "4. View Budget(vb)",
            "5. Exit(e)"
        ]
        colors = [
            'green',
            'blue',
            'yellow',
            'cyan',
            "red",
        ]
        for data,color in zip(functons,colors):
            print(colored(data,color))

    def todo(self):
        self.isOkay = True
        while self.isOkay:
            ask = str(input(colored("\nEnter what you want to do: ","grey")))
            if (ask == "ae"):
                self.__addExpense__()
            elif (ask == "cb"):
                self.__createBudget__()
            elif (ask =="vb"):
                self.__viewBudget__()
            elif (ask == "e"):
                print(self.generate_ascii_text("Thanks For Using BUDGET BUDDY", "green"))
                exit()
            elif (ask == "ve"):
                self.__viewExpense__()
                
                
    def __createBudget__(self):
        with open("budget.txt","r") as file:
            data = file.read()
            decrypt = ed.decrypt()
            key = decrypt.get_key()
            data = decrypt.read_encrypted_file("budget.txt")
            data = str(decrypt.decrypt_text(data,key))
            if int(data) == 0:
                yesOrNo = True
            else:
                yesOrNo =  not bool(data)

        if yesOrNo:
            totalBudget = input("Enter Budget: ")
            try:
                test = float(totalBudget)
                print("\nWorking On It..")
                for i in tqdm(range(0, 30), colour="#00ffff", desc ="Progress: "):
                    time.sleep(.1)
                encrypt = ed.encrypt()
                decrypt = ed.decrypt()
                key = decrypt.get_key()
                TotalBudget = encrypt.encrypt_text(totalBudget,key)
                encrypt.write_encrypted_file("budget.txt",TotalBudget)
                print(self.generate_ascii_text("Done","green"))
            except Exception as e:
                print(e)
                print("Data should be in integer or decimal form.")
        else:
            print("You Can't Update Budget In Creating Budget Mode")
    
    def __viewBudget__(self):
        decrypt = ed.decrypt()
        key = decrypt.get_key()
        data = decrypt.read_encrypted_file("budget.txt")
        budget = str(decrypt.decrypt_text(data,key))
        budget+= "/ -"
        budget = self.generate_ascii_text(budget,"yellow")
        print("\nWorking On It..")
        for i in tqdm(range(0, 30), colour="#00ffff", desc ="Progress: "):
            time.sleep(.1)
        print(f"\n{budget}")


    def __addExpense__(self):
        date = input("Enter date (YYYY-MM-DD): ")
        isValid = self.__validate_date__(date)

        if isValid:
            description = input("Enter description: ")
            amount = input("Enter amount: ")
            expense_data = [date, description, amount]
            with open('expenses.csv', 'a', newline='') as file:
                decrypt = ed.decrypt()
                key = decrypt.get_key()
                data = decrypt.read_encrypted_file("budget.txt")
                budget = str(decrypt.decrypt_text(data,key))
                if(int(budget)-int(amount) < 0):
                    print("Amount is greater than your current balance!")
                else:
                    print("\nWorking On It..")
                    for i in tqdm(range(0, 30), colour="#00ffff", desc ="Progress: "):
                        time.sleep(.1)
                    actAmount = int(budget)-int(amount)
                    self.updateBudget(str(actAmount))
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(expense_data)
        else:
            print("Date is Not Valid")
    def __viewExpense__(self, header_color_code="31", data_color_code="33"):
        print("\nWorking On It..")
        for i in tqdm(range(0, 30), colour="#00ffff", desc ="Progress: "):
            time.sleep(.1)
        def read_csv_data():
            with open("expenses.csv", 'r') as file:
                csv_reader = csv.reader(file)
                data = list(csv_reader)
            return data

        def print_colored_data(data):
            colored_data = [[f"\033[{data_color_code}m{item}\033[0m" for item in row] for row in data]
            return colored_data

        def print_colored_header(headers):
            colored_headers = [f"\033[{header_color_code}m{header}\033[0m" for header in headers]
            return colored_headers

        csv_data = read_csv_data()

        headers = csv_data[0]
        data = csv_data[1:]

        colored_headers = print_colored_header(headers)
        colored_data = print_colored_data(data)

        table = tabulate(colored_data, colored_headers, tablefmt="fancy_grid")
        print(table)

    def __validate_date__(self,date_string):
    # Define a regular expression pattern for the format YYYY-MM-DD
        pattern = r'^\d{4}-\d{2}-\d{2}$'

        # Use the re.match function to match the pattern against the date string
        if re.match(pattern, date_string):
            # Additional validation for valid year, month, and day values can be added here
            return True
        else:
            return False