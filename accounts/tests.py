from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your tests here.
class UserTestCase(TestCase):

  def setUp(self):
    user_a = User(username='aaa')
    user_a_pw = 'passwordForTesting'
    self.user_a_pw = user_a_pw
    user_a.is_staff = True
    user_a.is_superuser = True
    user_a.set_password(user_a_pw)
    user_a.save()
    self.user_a = user_a
  
  def tearDown(self):
    self.user_a.delete()
  
  def test_user_exist(self):
    user_count = User.objects.all().count()
    self.assertEqual(user_count, 1)
    self.assertNotEqual(user_count, 0)
    self.assertNotEqual(user_count, 2)
  
  # def test_user_already_exist(self):
  #   User.objects.create(username='aaa', password='password')
  #   user_count = User.objects.all().count()
  #   self.assertEqual(user_count, 1)
  
  def test_user_correct_username(self):
    user_username = User.objects.first().username
    self.assertEqual(user_username, 'aaa')
    self.assertNotEqual(user_username, 'aba')

  def test_user_password(self):
    user_a = User.objects.get(username='aaa')
    self.assertTrue(user_a.check_password(self.user_a_pw))
  
  def test_user_login(self):
    user = authenticate(username='aaa', password='passwordForTesting')
    self.assertTrue((user is not None) and user.is_authenticated)
  
  def test_wrong_username(self):
    user = authenticate(username='wrong', password='passwordForTesting')
    self.assertFalse(user is not None and user.is_authenticated)

  def test_wrong_password(self):
    user = authenticate(username='aaa', password='wrongPassword')
    self.assertFalse(user is not None and user.is_authenticated)