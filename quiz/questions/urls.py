from django.urls import path

from .views import TestListView, QuestionListView, handle_answer, get_results

urlpatterns = [
    path('list/', TestListView.as_view()),
    path('<int:test_pk>/', QuestionListView.as_view(), name='questions'),
    path('answer/question/<int:test_pk>/', handle_answer, name='handle_answer'),
    path('results/', get_results, name='results'),
]
