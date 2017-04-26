import pytest

from askpy import Validator, ValidationError


def make_validation_func(func, args=None, expand_args=True):
    """Create a validation function based on our input"""
    validation_func = func
    if args is not None:
        if expand_args:
            validation_func = validation_func(*args)
        else:
            validation_func = validation_func(args)
    return validation_func


def validate(user_input, expected_result, func, args=None, expand_args=True):
    """Helper to reduce some test boilerplate.
    
    We have to be careful about how we build the validation function to test
    against. In some cases it expects args to build the validation and in other
    cases it does not. Also, some cases expect an iterable and some expect
    multiple arguments. This cleans up some of that conditional boilerplate.

    In some cases, building the validation function can fail because we
    validate the arguments to ensure they are numeric for instance. Because of
    this we have to be careful about where we instantiate that function in this
    case.
    """

    if not expected_result:
        with pytest.raises(ValidationError):
            make_validation_func(func, args, expand_args)(user_input)
    else:
        assert make_validation_func(func, args, expand_args)(user_input)


class TestValidation(object):
    """Test the builtin validation methods work"""

    @pytest.mark.parametrize('input, expected', [
        ('a', False),
        ('1', True)
    ])
    def test_numeric(self, input, expected):
        validate(input, expected, Validator.num)

    @pytest.mark.parametrize('input, expected', [
        (None, False),
        ('', False),
        ('1', True)
    ])
    def test_required(self, input, expected):
        validate(input, expected, Validator.required)

    @pytest.mark.parametrize('input, expected', [
        ('-1', False),
        ('1', True)
    ])
    def test_positive_num(self, input, expected):
        validate(input, expected, Validator.positive_num)

    @pytest.mark.parametrize('args, input, expected', [
        (5, 'a', False),
        (5, '4', False),
        (5, '5', False),
        (5, '6', True)
    ])
    def test_num_gt(self, args, input, expected):
        validate(input, expected, Validator.num_gt, [args])

    @pytest.mark.parametrize('args, input, expected', [
        (5, 'a', False),
        (5, '4', False),
        (5, '5', True),
        (5, '6', True)
    ])
    def test_num_gte(self, args, input, expected):
        validate(input, expected, Validator.num_gte, [args])

    @pytest.mark.parametrize('args, input, expected', [
        (5, 'a', False),
        (5, '6', False),
        (5, '5', False),
        (5, '4', True)
    ])
    def test_num_lt(self, args, input, expected):
        validate(input, expected, Validator.num_lt, [args])

    @pytest.mark.parametrize('args, input, expected', [
        (5, 'a', False),
        (5, '6', False),
        (5, '5', True),
        (5, '4', True)
    ])
    def test_num_lte(self, args, input, expected):
        validate(input, expected, Validator.num_lte, [args])

    @pytest.mark.parametrize('args, input, expected', [
        (['a', 5], '1', False),
        ([1, 'a'], '1', False),
        ([5, 4], '1', False),
        ([4, 5], 'a', False),
        ([4, 5], '1', False),
        ([4, 6], '4', True),
        ([4, 6], '5', True),
        ([4, 6], '6', True)
    ])
    def test_num_between(self, args, input, expected):
        validate(input, expected, Validator.num_between, args)

    @pytest.mark.parametrize('args, input, expected', [
        (1, 'a', False),
        (1, 'ab', True)
    ])
    def test_len_gt(self, args, input, expected):
        validate(input, expected, Validator.len_gt, [args])

    @pytest.mark.parametrize('args, input, expected', [
        (2, 'a', False),
        (1, 'ab', True),
        (2, 'ab', True)
    ])
    def test_len_gte(self, args, input, expected):
        validate(input, expected, Validator.len_gte, [args])

    @pytest.mark.parametrize('args, input, expected', [
        (2, 'ab', False),
        (2, 'a', True)
    ])
    def test_len_lt(self, args, input, expected):
        validate(input, expected, Validator.len_lt, [args])

    @pytest.mark.parametrize('args, input, expected', [
        (2, 'abc', False),
        (2, 'ab', True),
        (2, 'a', True)
    ])
    def test_len_lte(self, args, input, expected):
        validate(input, expected, Validator.len_lte, [args])

    def test_one_of_requires_list(self):
        with pytest.raises(AssertionError):
            Validator.one_of('test')('test')

    @pytest.mark.parametrize('args, input, expected', [
        (['a', 'b'], 'c', False),
        (['a', 'b'], 'a', True)
    ])
    def test_one_of(self, args, input, expected):
        validate(input, expected, Validator.one_of, args, False)

    def test_contains_must_be_iterable_string_or_list(self):
        with pytest.raises(Exception):
            Validator.contains({'a': 1})('test')

    @pytest.mark.parametrize('args, input, expected', [
        ('abe', 'test', False),
        (['a', 'b'], 'ab', True),
        ('ab', 'acdeb', True)
    ])
    def test_contains(self, args, input, expected):
        validate(input, expected, Validator.contains, args, False)

    @pytest.mark.parametrize('args, input, expected', [
        ('^a.*', 'baby', False),
        ('^a.*', 'ababy', True)
    ])
    def test_contains(self, args, input, expected):
        validate(input, expected, Validator.matches, args, False)
