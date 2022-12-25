from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.views import View
from django.views.generic import ListView

from .models import TestSet, Question
from questions.services import save_answer, create_user_test, get_results


class TestListView(ListView):
    model = TestSet
    template_name = 'questions/test_list.html'
    context_object_name = 'tests'


class QuestionListView(View):
    def get(self, request, test_pk: int):
        questions = Question.objects.filter(test_id=test_pk)
        paginator = Paginator(questions, 1)

        user_test_id = request.GET.get('user_test_id')
        page_number = request.GET.get('page')
        error = request.GET.get('error', '')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'questions': questions,
            'user_test_id': user_test_id,
            'error': error,
        }
        return render(request, 'questions/question_list.html', context)


def handle_answer(request, test_pk: int):
    user_test_id = request.POST.get('user_test_id')

    if user_test_id == 'None':
        user_test_id = create_user_test(test_pk, request.user)

    next_page_number = request.POST.get('next_page')
    if next_page_number:
        current_page_number = int(next_page_number) - 1
    else:
        current_page_number = Question.objects.all().count()

    try:
        save_answer(request.POST, user_test_id)

        if next_page_number:
            query_dict = {'page': next_page_number, 'user_test_id': user_test_id}
            return redirect(f"{reverse('questions', kwargs={'test_pk': test_pk})}?{urlencode(query_dict)}")
        result_context = get_results(user_test_id)
        return render(request, 'questions/results.html', result_context)
    except ValueError:
        query_dict = {'page': current_page_number,
                      'user_test_id': user_test_id,
                      'error': 'Вы не выбрали ни один вариант'}
        return redirect(f"{reverse('questions', kwargs={'test_pk': test_pk})}?{urlencode(query_dict)}")
