import math

# Data Initialization
student_names = ["Lina", "Omar", "Zaid", "Sara", "Tariq"]
student_grades = [(88.5, 90, 79), (75, 80, 70), (60, 65, 70), (95, 92, 89), (100, 98, 99)]
student_courses = [{"AI", "Math"}, {"AI", "Ethics"},{"Ethics", "Writing"}, {"AI", "Math", "Robotics"},{"AI"}]

# Part 1: General Information
print("--- 1. General Information ---")
total_students = len(student_names)
print("Total number of students:", total_students)

for i in range(len(student_names)):
    name = student_names[i]
    courses_count = len(student_courses[i])
    print(name, "is enrolled in", courses_count, "courses.")

# Part 2: Grade Analysis
print("\n--- 2. Grade Analysis ---")
def average_grade(grades):
    return sum(grades) / len(grades)

high_achievers_count = 0

for i in range(len(student_names)):
    name = student_names[i]
    current_grades = student_grades[i]
    avg = average_grade(current_grades)
    print(name, "has an average of:", avg)
    
    if avg > 85:
        high_achievers_count += 1

print("Number of students with an average above 85 is:", high_achievers_count)

# Part 3: Course Analysis
print("\n--- 3. Course Analysis ---")
all_courses = set()

for courses in student_courses:
    all_courses.update(courses)

print("All unique courses offered:", all_courses)
print("Number of unique courses is:", len(all_courses))

ai_counter = 0

for courses in student_courses:
    if "AI" in courses:
        ai_counter += 1

print("Number of students enrolled in 'AI' is:", ai_counter)

# Part 4: Modifications
print("\n--- 4. Modifications ---")
student_courses[2].add("Cybersecurity")
print("Zaid's courses after adding Cybersecurity:", student_courses[2])
student_courses[3].remove("Math")
print("Sara's courses after removing Math:", student_courses[3])

omar_grades_list = list(student_grades[1])
omar_grades_list[1] += 5
student_grades[1] = tuple(omar_grades_list)
print("Omar's grades after modification:", student_grades[1])

# Part 5: Copy and Isolation
print("\n--- 5. Copy and Isolation ---")
names_copy = student_names.copy()
names_copy[0] = "Maya"

print("Original names list:", student_names)
print("Copied names list:", names_copy)

courses_copy = student_courses[0].copy()
courses_copy.add("Physics")

print("Original courses for Lina:", student_courses[0])
print("Copied courses:", courses_copy)

# Extra Part II: Data Cleaning Function
print("\n--- Extra Part II ---")
def process_data(arr):
    new_list = []
    
    for item in arr:
        if item == "NAN" or item == "":
            continue
        elif item.isdigit():
            new_list.append(item)
        elif "." in item:
            floored_num = math.floor(float(item))
            new_list.append(str(floored_num))
            
    return new_list

old_array = ["NAN", "", "4", "4.8", "3.2", "10", ""]
print("Before:", old_array)
after_array = process_data(old_array)
print("After:", after_array)
