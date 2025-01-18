import updateBook

def main():
    while True:
        
        subject_code = int(input("Which subject class?\n1. subject1\n2. subject2\n3. subject3\n\n"))
        
       
        absentees = list(map(int, input("Enter roll numbers separated by spaces: ").split()))
        
        
        if len(absentees) > 0:
            updateBook.handle(subject_code=subject_code, roll_absentees=absentees)
        else:
            print("No absentees entered for this subject class.")
        
       
        choice = int(input("Enter 1 to continue or 0 to exit: "))
        if choice == 0:
            print("Exiting...")
            break

if __name__ == '__main__':
    main()
