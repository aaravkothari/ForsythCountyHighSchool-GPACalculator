# utils.py
from .models import AddedCourse

def backup_to_model(added_courses):
    for course_data in added_courses:
        AddedCourse.objects.create(
            name = course_data['name'],
            type = course_data['type'],
            credit = course_data['credit'],
            grade = course_data['grade']
        )

def load_from_model():
    added_courses = []
    for course in AddedCourse.objects.all():
        course_data = {
            'name': course.name,
            'type': course.type,
            'credit': course.credit,
            'grade': course.grade
        }
        added_courses.append(course_data)
    return added_courses
