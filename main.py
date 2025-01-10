import updateBook

while True:
    subject_code = int(input('Which subject class?\nsubject1\nsubject2\nsubject3\n\n'))
    absentes = list(map(int, input("Enter roll numbers").split(' ')))
    
    if len(absentes) > 0:
        updateBook.handle(subject_code=subject_code, roll_absentees=absentes)
    else:
        print('No absentess entered for this subject class')
    
    exit = int(input("Enter 1 to continue or 0 to exit"))
    if exit == 0:
        print('Exiting...')
        break 
