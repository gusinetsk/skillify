from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


SEX = [
    ('m', 'male'),
    ('f', 'female')
    ]


class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    sex = models.CharField(max_length=1,choices=SEX)
    email = models.EmailField(unique=True)
    class Meta:
        abstract = True
class Student(Person):
    age = models.IntegerField()
    courses = models.ManyToManyField('Course', through='Enrollment')
    password = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} {self.surname}"



class Teacher(Person):

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.PositiveIntegerField(choices=[(i, f"{i} курс") for i in range(1, 5)])
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Subject(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title


class Feedback(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.assignment}"


class Grade(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    value = models.PositiveIntegerField(
            validators=[
                MaxValueValidator(10, message = 'input mark between 1 and 10'),
                MinValueValidator(1, message = 'input mark between 1 and 10')
            ]
        )

    def __str__(self):
        return f"{self.student.name} - {self.assignment.title} - {self.value}"

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student} - {self.course}"





