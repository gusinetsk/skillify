from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser, Group, Permission

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

class User(AbstractUser):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Email')
    photo = models.ImageField(upload_to="photo", null=True, blank=True, verbose_name='Фото')
    sex = models.CharField(max_length=1, choices=SEX, verbose_name='Пол')
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        Group,
        verbose_name='Группы',
        blank=True,
        related_name='education_users'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='Права доступа',
        blank=True,
        related_name='education_users'
    )

    def __str__(self):
        return self.username

class GradeClass(models.Model):
    class_number = models.CharField(max_length=2,choices=CLASS_CHOICES, verbose_name='Номер класса')

    def __str__(self):
        return f"{self.class_number} класс"

class Pupil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='pupil',default=None)
    grade_class = models.ForeignKey(GradeClass, on_delete=models.CASCADE, verbose_name='Класс')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Subject(models.Model):
    name = models.CharField(max_length=100,choices=SUBJECTS, verbose_name='Название предмета')
    grade_class = models.ManyToManyField(GradeClass, verbose_name='Класс')

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название темы')
    description = models.CharField(max_length=200,verbose_name='Описание')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    grade_class = models.ForeignKey(GradeClass, on_delete=models.CASCADE, verbose_name='Класс',null=True, blank=True)
    def __str__(self):
        return self.name


class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет', default='')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
    title = models.CharField(max_length=200, verbose_name='Название задания')
    description = models.TextField(verbose_name='Описание задания')
    deadline = models.DateTimeField(verbose_name='Крайний срок выполнения')

    def __str__(self):
        return self.title


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher',default=None)
    subjects = models.ManyToManyField(Subject, verbose_name='Предметы')
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Feedback(models.Model):
    pupil = models.ForeignKey(Pupil, on_delete=models.CASCADE, verbose_name='Ученик')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, verbose_name='Задание')
    content = models.TextField(verbose_name='Отзыв')
    grade = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], verbose_name='Оценка')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')

    def __str__(self):
        return f"{self.student.name} - {self.assignment.title} - {self.grade}"


class GradeAchievement(models.Model):
    student = models.ForeignKey(Pupil, on_delete=models.CASCADE, verbose_name='Ученик')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Предмет')
    total_grade = models.FloatField(verbose_name='Общая успеваемость')

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} - {self.total_grade}"
