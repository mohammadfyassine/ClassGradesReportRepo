records = [
    ["Layla", 89], ["Tariq", 77], ["Layla", 91], ["Jana", 100],
    ["Tariq", 84],["Ziad", 62], ["Jana", 97], ["Tariq", 73],
    ["Ziad", 71], ["Layla", 86],
    ["Jana", 94], ["Ziad", 75]
]

class_journal = {}

for name, grade in records:
    if name not in class_journal:
        class_journal[name] = []
    class_journal[name].append(grade)

for student, grades in class_journal.items():
    average = sum(grades) / len(grades)
    print("Name:", student)
    print("Grades:", grades)
    print("Average:", round(average, 2), " \n")

top_average = 0
top_student = ""
most_consistent_difference = float('inf')
most_consistent_student = ""
below_70 = []
total_grades = 0
total_sum = 0

for student, grades in class_journal.items():
    average = sum(grades) / len(grades)
    
    if average > top_average:
        top_average = average
        top_student = student
    
    difference = max(grades) - min(grades)
    if difference < most_consistent_difference:
        most_consistent_difference = difference
        most_consistent_student = student
    
    if any(grade < 70 for grade in grades):
        below_70.append(student)
    
    total_grades += len(grades)
    total_sum += sum(grades)

overall_class_average = total_sum / total_grades

print("1. Highest Average:", top_student, "with", round(top_average, 2))
print("2. Most Consistent Performer:", most_consistent_student, "(smallest grade difference:", most_consistent_difference, ")")
print("3. Students with at least one grade below 70:", below_70)
print("4. Total number of grades entered:", total_grades)
print("5. Overall class average:", round(overall_class_average, 2))