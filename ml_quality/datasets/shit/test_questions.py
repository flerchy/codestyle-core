import pytest
from unittest.mock import patch

from askpy.question import Question
from askpy.exceptions import (
    ValidatorIsNotCallable,
    ManipulatorIsNotCalable,
    ValidationError,
    QuestionAlreadyAnswered,
    QuestionNotAnswered,
    ConditionalAlreadyExists,
    CreateQuestionError
)


def make_question(name=None, question=None):
    name = name or 'test_question'
    question = question or 'What is your name?'
    question_obj = Question(name, question)
    return question_obj


class TestQuestions(object):
    """Ensure the Question model works as expected"""

    def test_question_can_be_created(self):
        name = 'test_question'
        question = 'What is your name?'
        question_obj = Question(name, question)

        assert question_obj.name == name
        assert question_obj.question == question
        assert question_obj.response == None
        assert question_obj.validator == None
        assert question_obj.manipulator == None
        assert question_obj.has_followup == False
        assert question_obj.next_evaluator == None
        assert question_obj.if_true == None
        assert question_obj.if_false == None

    def test_create_requires_args(self):
        with pytest.raises(CreateQuestionError):
            Question.create()

    def test_create_from_dictionary(self):
        name = 'test_question'
        question = 'What is your name?'
        question_obj = Question.create({ 'name': name, 'question': question })

        assert question_obj.name == name
        assert question_obj.question == question
        assert question_obj.response == None
        assert question_obj.validator == None
        assert question_obj.manipulator == None
        assert question_obj.has_followup == False
        assert question_obj.next_evaluator == None
        assert question_obj.if_true == None
        assert question_obj.if_false == None

    def test_create_from_args(self):
        name = 'test_question'
        question = 'What is your name?'
        question_obj = Question.create(name, question)

        assert question_obj.name == name
        assert question_obj.question == question
        assert question_obj.response == None
        assert question_obj.validator == None
        assert question_obj.manipulator == None
        assert question_obj.has_followup == False
        assert question_obj.next_evaluator == None
        assert question_obj.if_true == None
        assert question_obj.if_false == None

    @pytest.mark.skip
    def test_was_answered(self):
        question = make_question()
        assert not question.was_answered()

        responded_question = make_question()
        responded_question.response = 'Hello, World!'

        with patch.object(question, 'ask', responded_question) as mock_question:
            question.ask()
            import pdb
            pdb.set_trace()
