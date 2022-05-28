from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import AnswerForm, ReviewForm
from .models import Lesson, Answer, Grade, Review
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.forms.formsets import formset_factory
from django.contrib.auth.decorators import login_required


# Create your views here.


def welcome(request):
    return render(request, 'welcome.html')


def base(request):
    return render(request, 'base.html')


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            context = {}
            return render(request, 'registration/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('lessons/')


@login_required
def lessons(request):
    # users can view lessons #
    lessons = Lesson.objects.all().order_by('level')
    context = {"lessons": lessons}
    return render(request, "lessons/index.html", context)


# #Users can view an active lesson
@login_required
def detail(request, lesson_pk):
    lesson = get_object_or_404(Lesson, pk=lesson_pk)
    questions = lesson.question_set.all()

    # Display the grade
    grade = lesson.grade_set.all()
    if grade.exists():
        grade = grade.first().score
    else:
        grade = 0
    print(grade)
    context = {"lesson": lesson, "questions": questions, "grade": grade}
    return render(request, "lessons/details.html", context)


def start(request, lesson_pk):
    lesson = get_object_or_404(Lesson, pk=lesson_pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            lesson.grade_set.create(answers=form.cleaned_data['answers'],
                                    user=request.user)
            return redirect("lessons/submit.html", lesson.id)
        else:
            pass
    else:
        form = AnswerForm()
    context = {'lessons': lesson}
    return render(request, "lessons/start.html", context)


def submit(request, lesson_pk):
    if request.method == "POST":
        print(request.POST)
        lesson = get_object_or_404(Lesson, pk=lesson_pk)
        answers = Answer.objects.all()
        questions = lesson.question_set.all()
        correct = 0
        grade = 0
        for question in questions:
            q_id = question.id
            choice = request.POST.get(F"choice-{q_id}")
            if choice:
                correct_answer = question.get_correct_answer()
                if correct_answer.id == int(choice):
                    correct += 1
        grade = correct / 3 * 100
        if not lesson.grade_set.all().exists():
            lesson.grade_set.create(user=request.user, score=grade, lesson = lesson_pk)
        else:
          lesson.grade_set.create(user=request.user, score=grade, lesson = lesson_pk)
        context = {
            'correct': correct,
            'grade': grade,
        }
        return render(request, 'lessons/thanks.html', context)
    else:
        form = AnswerForm()
        lesson = get_object_or_404(Lesson, pk=lesson_pk)
        questions = lesson.question_set.all()
        answers = Answer.objects.all()
        context = {
            'questions': questions,
            'answers': answers,
            'form': form,
            "lesson": lesson,
        }
        return render(request, 'lessons/submit.html', context)


def thanks(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    context = {"lesson": lesson}
    return render(request, "lessons/thanks.html", context)

def create_review(request, lesson_pk): 
    p = get_object_or_404(Lesson, pk=lesson_pk)
    if request.method=='POST':
      form = ReviewForm(request.POST)
      if form.is_valid():
        print(form.cleaned_data)
        p.review_set.create(stars=form.cleaned_data['stars'],review=form.cleaned_data['review'],user=request.user)
        return redirect ('lesson-detail', p.id)
      else:
        pass
    else:
      print("HERE")
      form = ReviewForm()
      context = {'lesson':p, 'form':form}
      return render(request, 'lessons/review.html', context)
