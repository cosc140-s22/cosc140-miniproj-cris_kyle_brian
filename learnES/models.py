from django.db import models
from django.contrib.auth import models as auth_models
from django.core.validators import *

# Create your models here.

class Lesson(models.Model):
  level = models.IntegerField(blank=False, default=0, validators=[MinValueValidator(1), MaxValueValidator(3)])
  description = models.CharField(max_length=300, null=True)
  number_of_questions = models.IntegerField(default=1)
  difficulty= models.CharField(max_length=50, blank=False)
  
  def __str__(self):
    return f"Lesson #{self.level}, {self.difficulty} Difficulty"

  def get_all_questions(self):
    return self.question_set.all()

# One Question that can be available in a Lesson
class Question(models.Model):
  question = models.CharField(max_length=200, blank=False)
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.question

  def get_answers(self):
    return self.answer_set.all()

  def get_correct_answer(self):
    answers = self.get_answers()
    for answer in answers:
      if answer.correct:
        return answer

# all of the possible answers for a question, with one being the correct option
class Answer(models.Model):
  content = models.CharField(max_length=200)
  correct = models.BooleanField(default=False)
  question = models.ForeignKey(Question, on_delete=models.CASCADE)

  def __str__(self):
    return f"Question: {self.question.question}, answer: {self.content}, correct: {self.correct}"


# A grade model that scores the User's Lesson based on the number of the correct questions
class Grade(models.Model):
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
  user = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
  score = models.IntegerField(default=0.0)

  def __str__(self):
    return str(self.score)


# A comment model allowing users to leave a comment on the lesson
class Review(models.Model):
    stars = models.IntegerField(blank=False,validators=[MinValueValidator(1),MaxValueValidator(5)])
    review = models.TextField()
    lesson = models.ForeignKey(Lesson, models.CASCADE)
    user = models.ForeignKey(auth_models.User, models.CASCADE)

    def __str__(self):
        return f"User reviewed this lesson to be {self.stars} stars"



