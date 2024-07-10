from django.contrib import admin
from .models import QuizCategory, Question, Answer

admin.site.register(QuizCategory)
admin.site.register(Question)
admin.site.register(Answer)
