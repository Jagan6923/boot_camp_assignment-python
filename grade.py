def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "Fail"

while True:
    mark_input = input("Type the student's mark (type 'exit' to quit): ")

    if mark_input.lower() == 'exit':
        break

    if mark_input.isdigit():
        mark = int(mark_input)
        if 0 <= mark <= 100:
            grade = calculate_grade(mark)
            print(f"Your grade is: {grade}")
        else:
            print("Invalid marks. Marks should be between 0 and 100.")
    else:
        print("Type a number next time.")

print("Goodbye! Exiting the program.")
