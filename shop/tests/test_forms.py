from django.test import TestCase

from shop.forms import SearchForm, LoginForm, RegisterForm


class SearchFormTest(TestCase):
    def test_search_success(self):
        form_data = {
            'searh_string': 'поиск по данной строке'
        }
        form = SearchForm(data=form_data)
        self.assertTrue(form.is_valid())


class LoginFormTest(TestCase):
    def test_loginform_login_max_length_fail(self):
        form_data = {
            'login': 'lorem ipsum ' * 25,
            'password': 'lorem ipsum '
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())

class RegisterFormTest(TestCase):
    def test_registerform_passwords_compare_fail(self):
        form_data = {
            'login': 'lorem ipsum ' * 25,
            'email': 'lorem ipsum ' * 25,
            'password1': 'lorem ipsum2',
            'password2': 'lorem ipsum1'
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())


