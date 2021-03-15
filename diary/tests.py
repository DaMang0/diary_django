from django.test import TestCase
from .models import Article
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.urls import resolve
from django.contrib.auth.models import User
# Create your tests here.
User = get_user_model()

class ArticleTestCase(TestCase):
  
  def setUp(self):
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    article_1 = Article.objects.create(title='title1', body='body', user=user)
  
  def test_article_list_url(self):
    url = reverse('article:list')
    self.assertEqual(url, '/article/list/')

  def test_article_list_resolve(self):
    resolver = resolve('/article/list/')
    # correct URL
    self.assertEqual(resolver.route, 'article/list/')
    # correct View Function
    self.assertEqual(resolver._func_path, 'diary.views.ArticleListView')
    # correct name space
    self.assertEqual(resolver.view_name, 'article:list')
  
  def test_article_detail_url(self):
    url = reverse('article:detail', args=['title1'])
    self.assertEqual(url, '/article/title1/detail/')
    self.assertNotEqual(url, '/article/incorrect-args/detail/')
  
  def test_article_detail_resolve(self):
    url = reverse('article:detail', args=['title1'])
    resolver = resolve(url)

    self.assertEqual(resolver.route, 'article/<slug:slug>/detail/')
    self.assertNotEqual(resolver.route, 'article/<slug:slug>/detail/')
    
    self.assertEqual(resolver._func_path, 'diary.views.ArticleDetail')
    self.assertNotEqual(resolver._func_path, 'diary.views.ArticleDetail')

    self.assertEqual(resolver.view_name, 'article:detail')
    self.assertNotEqual(resolver.view_name, 'article:WRONGdetail')
  

  def test_article_create(self):
    article_count = Article.objects.all().count()
    self.assertEqual(article_count, 1)
    self.assertNotEqual(article_count, 2)
    self.assertNotEqual(article_count, 0)
  

   
