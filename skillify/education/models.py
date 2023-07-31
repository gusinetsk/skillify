from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

SEX = [
    ('m', 'мужской'),
    ('f', 'женский')
    ]
SUBJECTS = [
    ('бел.яз','белорусский язык'),
    ('рус.яз','русский язык'),
    ('англ.яз','английский язык'),
    ('бел.лит','белорусская литература'),
    ('рус.лит','русская литература'),
    ('матем','математика'),
    ('ист','история'),
    ('био','биология'),
    ('гео','география'),
    ('физ','физика'),
    ('инф','информатика'),
    ('общ','обществоведение'),
    ('хим','химия')
]
CLASS_CHOICES = [
    ('1', '1 класс'),
    ('2', '2 класс'),
    ('3', '3 класс'),
    ('4', '4 класс'),
    ('5', '5 класс'),
    ('6', '6 класс'),
    ('7', '7 класс'),
    ('8', '8 класс'),
    ('9', '9 класс'),
    ('10', '10 класс'),
    ('11', '11 класс')
]

# Модель Класса (1-11 классы)
class GradeClass(models.Model):
    class_number = models.CharField(max_length=2,choices=CLASS_CHOICES, verbose_name='Номер класса')

    def __str__(self):
        return f"{self.class_number} класс"

# Модель Предмета
class Subject(models.Model):
    name = models.CharField(max_length=100,choices=SUBJECTS, verbose_name='Название предмета')
    grade_class = models.ManyToManyField(GradeClass, verbose_name='Класс')

    def __str__(self):
        return self.name

# Модель Темы
class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название темы')
    description = models.CharField(max_length=200,verbose_name='Описание')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')

    def __str__(self):
        return self.name

# Модель Задания
class Assignment(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
    title = models.CharField(max_length=200, verbose_name='Название задания')
    description = models.TextField(verbose_name='Описание задания')
    deadline = models.DateTimeField(verbose_name='Крайний срок выполнения')

    def __str__(self):
        return self.title


class Person(models.Model):
    username = models.CharField(max_length=50,verbose_name='логин')
    name = models.CharField(max_length=50,verbose_name='имя')
    surname = models.CharField(max_length=50,verbose_name='фамилия')
    sex = models.CharField(max_length=1,choices=SEX,verbose_name='пол')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, verbose_name='пароль')
    photo = models.ImageField(upload_to="photo", null=True, blank=True)
    class Meta:
        abstract = True
# Модель Ученика
class Pupil(Person):
    grade_class = models.ForeignKey(GradeClass,on_delete=models.CASCADE, verbose_name='Класс')
    subjects = models.ManyToManyField(Subject, verbose_name='Предметы')

    def __str__(self):
        return self.name

# Модель Учителя
class Teacher(Person):
    subjects = models.ManyToManyField(Subject, verbose_name='Предметы')

    def __str__(self):
        return self.name

# Модель Отзыва и Оценки
class Feedback(models.Model):
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE, verbose_name='Ученик')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, verbose_name='Задание')
    content = models.TextField(verbose_name='Отзыв')
    grade = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name='Оценка')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')

    def __str__(self):
        return f"{self.student.name} - {self.assignment.title} - {self.grade}"

# Модель Общей успеваемости по предмету для Ученика
class GradeAchievement(models.Model):
    student = models.ForeignKey(Pupil, on_delete=models.CASCADE, verbose_name='Ученик')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    total_grade = models.FloatField(verbose_name='Общая успеваемость')

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.total_grade}"
