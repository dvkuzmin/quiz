from questions.models import Answer, UserAnswer, TestSet, Question, UserTest


def extract_answers(data: dict):
    result = []
    for key, value in data.items():
        if value == 'on':
            result.append(key)
    if result:
        return result
    raise ValueError


def save_answer(data: dict, user_test_id: int):
    answers = extract_answers(data)
    for user_answer in answers:
        answer = Answer.objects.get(pk=user_answer)
        user_test = UserTest.objects.get(pk=user_test_id)
        UserAnswer.objects.create(answer=answer, user_test=user_test)


def create_user_test(test_id: int, user):
    test = TestSet.objects.get(pk=test_id)
    user_test = UserTest.objects.create(
        test=test,
        user=user
    )
    return user_test.pk


def get_results(user_test_id: int):
    user_test = UserTest.objects.get(pk=user_test_id)
    user_answers = UserAnswer.objects.filter(user_test=user_test)
    questions = Question.objects.filter(test_id=user_test.test_id)
    questions_counter = questions.count()

    correct_answers_counter = 0

    for question in questions:
        right_answers_for_question = Answer.objects.filter(question_id=question.pk, correct_answer=True)
        answer_is_right = True
        for right_answer in right_answers_for_question:
            if right_answer.answer_text not in map(lambda el: el.answer.answer_text, user_answers):
                answer_is_right = False
                break
        if answer_is_right:
            correct_answers_counter += 1

    right_answer_percentage = round(correct_answers_counter * (100 / questions_counter), 1)
    wrong_answers_counter = questions_counter - correct_answers_counter
    return {'right': correct_answers_counter,
            'wrong': wrong_answers_counter,
            'right_answer_percentage': right_answer_percentage}
