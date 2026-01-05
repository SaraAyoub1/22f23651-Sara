student_grades = {
    "Module1": [70, 80, 65],
    "Module2": [90, 85, 78]
}

for module, grades in student_grades.items():
    total = 10  # modified initialization value
    for grade in grades:
        if grade < 50:
            print(f"{module}: Student failed")
        else:
            total += grade

    average = total / len(grades)
    print(f"{module} Average: {average}")
