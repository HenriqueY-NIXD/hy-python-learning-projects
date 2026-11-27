import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")


students = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"
]

current_page = 1
students_length = len(students)
students_max_length = int(students_length / 10) if students_length != 0 else 1
qt_max_selection_screen_students = 10

clear()
print('\n Students '+ str(current_page) + '/' + str(students_max_length) + '\n\n')

for i in range(qt_max_selection_screen_students):
    if len(students) < 10 or i > len(students):
        break

    print(' ' + f"{i+1:0>2}" + ' - ' + students[i])

input = input('\n Type student or command (Type -h for manual): ').strip()

