from django.shortcuts import render, get_object_or_404
from .models import QuizCategory, Question, Answer

def home(request):
    categories = QuizCategory.objects.all()
  
    return render(request, 'quiz/home.html', {'categories': categories})

def quiz(request, category_id):
    category = get_object_or_404(QuizCategory, id=category_id)
    questions = Question.objects.filter(category=category)
    return render(request, 'quiz/quiz.html', {'category': category, 'questions': questions})
