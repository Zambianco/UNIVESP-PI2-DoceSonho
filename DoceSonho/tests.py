from django.test import TestCase
from django.urls import reverse
import json
import uuid

from DoceSonho.forms import NewUserForm

# Create your tests here.

class NewUserFormTest(TestCase):

    def test_valid_email_dot_com(self):
        form = NewUserForm(data={'username':'teste','email':'teste@teste.com','password1':'1X<ISRUkw+tuK','password2':'1X<ISRUkw+tuK'})
        print(form.errors,form.non_field_errors)
        self.assertTrue(form.is_valid())

    def test_valid_email_dot_com_dot_br(self):
        form = NewUserForm(data={'username':'teste','email':'teste@teste.com.br','password1':'1X<ISRUkw+tuK','password2':'1X<ISRUkw+tuK'})
        print(form.errors,form.non_field_errors)
        self.assertTrue(form.is_valid())

    def test_invalid_email_without_dot_com(self):
        form = NewUserForm(data={'username':'teste','email':'teste@teste','password1':'1X<ISRUkw+tuK','password2':'1X<ISRUkw+tuK'})
        print(form.errors,form.non_field_errors)
        self.assertFalse(form.is_valid())       

    def test_invalid_email_without_dot_arroba(self):
        form = NewUserForm(data={'username':'teste','email':'teste.teste.com.br','password1':'1X<ISRUkw+tuK','password2':'1X<ISRUkw+tuK'})
        print(form.errors,form.non_field_errors)
        self.assertFalse(form.is_valid())   

    def test_invalid_password_match(self):
        form = NewUserForm(data={'username':'teste','email':'teste@teste.com.br','password1':'1X<ISRUkw+tuK','password2':'1X<ISRUkw+tuf'})
        print(form.errors,form.non_field_errors)
        self.assertFalse(form.is_valid())             

    def test_invalid_password_complexity(self):
        form = NewUserForm(data={'username':'teste','email':'teste@teste.com.br','password1':'123456789','password2':'123456789'})
        print(form.errors,form.non_field_errors)
        self.assertFalse(form.is_valid())        

        