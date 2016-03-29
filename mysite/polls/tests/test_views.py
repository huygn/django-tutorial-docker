import datetime

from django.utils import timezone
from django.core.urlresolvers import reverse
from django.test import TestCase

from polls.models import Question


def create_question(question_text, days):
    """
    Creates a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(
        question_text=question_text,
        pub_date=time)


class QuestionIndexTests(TestCase):
    no_question_msg = "No polls are available."

    def test_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.no_question_msg)
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page.
        """
        question_text = "Past question"
        create_question(question_text=question_text, days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: %s>' % question_text]
        )

    def test_index_view_with_a_future_question(self):
        """
        Questions with a pub_date in the future should NOT be displayed on the
        index page.
        """
        question_text = "Future question"
        create_question(question_text=question_text, days=30)
        self.test_view_with_no_questions()

    def test_index_view_with_past_question_and_future_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        past_question_text = "Past question"
        future_question_text = "Future question"
        create_question(question_text=past_question_text, days=-30)
        create_question(question_text=future_question_text, days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: %s>' % past_question_text]
        )

    def test_index_view_with_two_past_questions(self):
        """
        The questions index page display multiple questions.
        """
        first_question_text = "Past question 1"
        second_question_text = "Past question 2"
        create_question(question_text=first_question_text, days=-30)
        create_question(question_text=second_question_text, days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            ['<Question: %s>' % second_question_text,
            '<Question: %s>' % first_question_text]
        )


class QuestionDetailTests(TestCase):
    def test_detail_view_with_a_future_question(self):
        """
        The detail view of a question with a pub_date in the future should
        return a 404 not found.
        """
        future_question = create_question(
            question_text='Future question.',
            days=5)
        response = self.client.get(reverse(
            'polls:detail',
            args=(future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        """
        The detail view of a question with a pub_date in the past should
        display the question's text.
        """
        past_question = create_question(
            question_text='Past Question.',
            days=-5)
        response = self.client.get(reverse(
            'polls:detail',
            args=(past_question.id,)))
        self.assertContains(
            response,
            past_question.question_text,
            status_code=200)
