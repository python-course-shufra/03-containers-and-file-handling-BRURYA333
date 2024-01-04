classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]


def add_student(name, email=None):
    if email is None:
        email = f'{name.lower()}@example.com'
    new_student={'name':name,'email':email,'grades':[]}
    classroom.append(new_student)

    

def delete_student(name):
    for student in classroom:
        if student['name'] == name:
            classroom.remove(student)
            break
    


def set_email(name, email):
    for student in classroom:
        if student['name']==name:
            classroom[name].update({'email':email})
    
    


def add_grade(name, profession, grade):
    for student in classroom:
        if student['name']==name:
            student['grades'].append((profession, grade))
            break
    


def avg_grade(name, profession):
    for student in classroom:
        if student['name']==name:
            count = 0
            total = 0
            for grade_profession, grade_value in student['grades']:
                if grade_profession == profession:
                    count += 1
                    total += grade_value
            if count > 0:
                return total / count
            else:
                return 0 
    return 0                  

    


def get_professions(name):
    for student in classroom:
        if student ['name']== name:
            professions = [grade_profession[0] for grade_profession in student['grades']]
            return professions
    return []




print(classroom)
add_student('bbb',)

"""print(classroom)
delete_student('Bob')
print(classroom)"""

print(avg_grade('Charlie','physics'))

print(get_professions('Alice'))

