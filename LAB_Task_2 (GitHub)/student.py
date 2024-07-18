students = {
    "Calculus": {
        101: {'name': 'Umar', 'grades': [85, 90, 92]},
        102: {'name': 'Inaam', 'grades': [88, 85, 87]},
        103: {'name': 'Shayan', 'grades': [90, 95, 92]}
    },
    "OOPs": {
        101: {'name': 'Umar', 'grades': [75, 80, 62]},
        102: {'name': 'Inaam', 'grades': [58, 95, 77]},
        103: {'name': 'Shayan', 'grades': [80, 75, 92]}
    },
    "DSA" : {
        101: {'name': 'Umar', 'grades': [78, 88, 68]},
        102: {'name': 'Inaam', 'grades': [78, 88, 78]},
        103: {'name': 'Shayan', 'grades': [88, 76, 98]}
    }
}

def add(course, stdid, name, grade):
    students[course][stdid] = {'name': name, 'grades': grade}
    
    
def average(course):
    for stdid in students[course]:
        grades = students[course][stdid]['grades']
        total = sum(grades)
        average = total / len(grades)
        return average
        
        
add("OOPs", 104, "Aliyan", [87,82,92])
        
average("OOPs")

for course, students_dict in students.items():
    print(f"Course: {course}")
    for stdid, info in students_dict.items():
        name = info['name']
        grades = info['grades']
        average_grade = sum(grades) / len(grades)
        print(f"  Student ID: {stdid}, Name: {name}, Grade: {average(course):.2f}")
