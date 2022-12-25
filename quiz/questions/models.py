from django.db import models
from django.contrib.auth.models import User


class TestSet(models.Model):
    class Meta:
        verbose_name = 'Набор тестов'
        verbose_name_plural = 'Наборы тестов'

    name = models.CharField(max_length=255)

    def __str__(self):
        return f'Тест по теме {self.name}'


class Question(models.Model):
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    question_text = models.TextField()
    test = models.ForeignKey(TestSet, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question_text[:30]}'


class Answer(models.Model):
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    answer_text = models.TextField()
    correct_answer = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.answer_text[:30]}'


class UserTest(models.Model):
    test = models.ForeignKey(TestSet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)


class UserAnswer(models.Model):
    user_test = models.ForeignKey(UserTest, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.answer.answer_text}"
