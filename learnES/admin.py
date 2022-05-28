from django.contrib import admin
from .models import Lesson, Question, Answer, Grade
admin.site.register(Lesson)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Grade)
# Register your models here.
