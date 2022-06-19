from django.test import TestCase
from django.urls import reverse
import json
import uuid

from django.contrib.messages import get_messages
from DoceSonho.forms import NewUserForm

# Create your tests here.

class NewUserFormTest(TestCase):

    def test_valid_email_dot_com(self):
        form = NewUserForm(data={'username':'teste','email':'teste@teste.com','password1':'1X<ISRUkw+tuK','password2':'1X<ISRUkw+tuK'})
        self.assertTrue(form.is_valid())

    def test_valid_email_dot_com_dot_br(self):
        form = NewUserForm(data={'username':'teste','email':'teste@teste.com.br','password1':'1X<ISRUkw+tuK','password2':'1X<ISRUkw+tuK'})
        self.assertTrue(form.is_valid())

    def test_invalid_email_without_dot_com(self):
        form = NewUserForm(data={'username':'teste','email':'teste@teste','password1':'1X<ISRUkw+tuK','password2':'1X<ISRUkw+tuK'})
        self.assertFalse(form.is_valid())       

    def test_invalid_email_without_dot_arroba(self):
        form = NewUserForm(data={'username':'teste','email':'teste.teste.com.br','password1':'1X<ISRUkw+tuK','password2':'1X<ISRUkw+tuK'})
        self.assertFalse(form.is_valid())   

    def test_invalid_password_match(self):
        form = NewUserForm(data={'username':'teste','email':'teste@teste.com.br','password1':'1X<ISRUkw+tuK','password2':'1X<ISRUkw+tuf'})
        self.assertFalse(form.is_valid())             

    def test_invalid_password_complexity(self):
        form = NewUserForm(data={'username':'teste','email':'teste@teste.com.br','password1':'123456789','password2':'123456789'})
        self.assertFalse(form.is_valid())        

class UserViewsTest(TestCase):
    def setUp(self):
        self.username = "usuario1"
        self.password = str(uuid.uuid4())
        self.email = 'renatozane90.rz@gmail.com'
        
        form = NewUserForm(data={'username':self.username,'email':self.email,'password1':self.password,'password2':self.password})       
        form.save()

    def test_create_user(self):
        response = self.client.post('/register/', data = {'username':self.username,'email':'teste@teste.com','password1':self.password,'password2':self.password},follow=True)
        self.assertEqual(response.status_code, 200)
        # self.assertRedirects(response, '/')

    def test_login(self):
        login = self.client.login(username=self.username, password=self.password)
        self.assertTrue(login)

    def test_password_reset(self):
        response = self.client.post('/password_reset', data = {'email':self.email},follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/password_reset/done/')

    def test_create_user_invalid_email(self):
        response = self.client.post('/register/', data = {'username':self.username,'email':'teste.teste','password1':self.password,'password2':self.password})
        print(get_messages(response))
        self.assertEqual(response.status_code, 200)

    def test_login_invalid_user(self):
        login = self.client.login(username='invalido', password=self.password)
        self.assertFalse(login)

    def test_login_invalid_password(self):
        login = self.client.login(username=self.username, password='123456')
        self.assertFalse(login)

    def test_password_reset_invalid_email(self):
        response = self.client.post('/password_reset', data = {'email':'teste@teste.com'})
        self.assertEqual(response.status_code, 200)        