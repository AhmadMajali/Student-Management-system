Exit = False 

while not Exit:
    print('\n-------------------\n1- Add Student\n2- View All students\n3- Search Student by Name\n4- Delete Student\n5- Exit\n\n')
    choice = int(input('Choose an option: '))
    match(choice):
        case 1:
            try: 
                with open('students.txt', 'a') as f:
                    name = input('Name: ')
                    age = int(input('Age: '))
                    valid = True
                    while valid:
                        if age > 100 or age < 5:
                            print('invalid Age\n')
                            age = int(input('Enter Age Again\n'))
                        else: 
                            valid = False
                            
                    grade = input('Grade: ').upper()
                    while grade not in 'ABCDEF':
                            print('Invalid Grade. should be (A-F)')
                            grade = input('Enter The Grade again: ').upper()
                        
                    f.write(f'Name: {name}, Age: {age}, Grade: {grade}\n')
            except FileNotFoundError:
                f = open('students.txt', 'x')
            except ValueError:
                print('Please Enter numbers not Letters')
        case 2: 
            try: 
                with open('students.txt', 'r') as f:
                    text = f.read().strip()
                    if not text: 
                        raise ValueError
                    else:
                        print(text)
            except ValueError:
                print('\nNo students records found.\n')
        case 3:
            try:
                search = input('Enter a Student name to search')
                found = False
                with open('students.txt', 'r') as f:
                    for line in f:
                        if search.lower() in line.lower():
                            print('student found: ', line.strip())
                            found= True
                            break
                        
                if not found:
                    print('Student Not Found!\n')            
            except FileNotFoundError:
                print('no such file')   
        case 4:
            try:
                StudentDeletion = input('Enter a student name to delete: ')
                found = False
                with open('students.txt') as f:
                    lines= f.readlines()
                
                with open('students.txt', 'w') as f:
                    for line in lines:
                        if StudentDeletion.lower() not in line.lower():
                            f.write(line)
                        else:
                            found = True
                if found:
                    print (f'Student \'{StudentDeletion}\' has been deleted.\n')
                else:
                    print('Student Not found!\n')
            except FileNotFoundError:
                print('File Doesnt exist')
        case 5:
            Exit = True

