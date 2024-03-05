def display_loans():
    try:
        with open("loans.txt", "r") as file:
            print("Book Title\t\tLoan Date")
            for line in file:
                title, loan_date = line.strip().split(";")
                print(f"{title}\t\t{loan_date}")
    except FileNotFoundError:
        print("No loans recorded yet.")

if __name__ == "__main__":
    display_loans()
