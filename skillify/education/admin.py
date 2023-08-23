from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(GradeClass)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Assignment)
admin.site.register(Feedback)
admin.site.register(GradeAchievement)
admin.site.register(Schedule)
# Register your models here.
