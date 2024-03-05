def record_loans():
    num_books = int(input("Enter the number of book records to input: "))

    with open("loans.txt", "a") as file:
        for _ in range(num_books):
            title = input("Enter the book title: ")
            loan_date = input("Enter the loan date (YYYY-MM-DD): ")
            file.write(f"{title};{loan_date}\n")

    print("Book records have been saved to loans.txt")

if __name__ == "__main__":
    record_loans()