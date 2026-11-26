from functools import reduce

students = [
    {
        "name":"John",
        "marks":[80,75,90],
        "courses":["Python","Java","Python"]
    },
    {
        "name":"Mary",
        "marks":[65,70,60],
        "courses":["Python","C++","C++"]
    }
]

def average(marks):
    return sum(marks)/len(marks)

for student in students:

    avg = average(student["marks"])

    upgraded_marks = list(
        map(
            lambda x:x+5,
            student["marks"]
        )
    )

    total_marks = reduce(
        lambda a,b:a+b,
        upgraded_marks
    )

    unique_courses = set(
        student["courses"]
    )

    report = {
        "Name": student["name"],
        "Average": avg,
        "Total Marks": total_marks,
        "Courses": unique_courses,
        "Status": "Distinction"
        if avg >= 70 else "Pass"
    }

    print("\nSTUDENT REPORT")
    print(report)