from django.test import TestCase
from account.models import User


class UserTestCase(TestCase):
    def test_user(self):
        username = 'kcorkery'
        first_name = 'Karley'
        last_name = 'Corkery'
        email = 'Karley_Corkery64@hotmail.com'
        password = 'XGxO9LKvrDBs_ny'
        u = User(username=username, first_name=first_name, last_name=last_name, email=email)
        u.set_password(password)
        u.save()

        self.assertEqual(u.username, username)
        self.assertEqual(u.first_name, first_name)
        self.assertEqual(u.last_name, last_name)
        self.assertEqual(u.email, email)
        self.assertTrue(u.check_password(password))
