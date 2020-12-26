from django.test import TestCase
from .models import Article
# Create your tests here.
class ArticleTestCase(TestCase):

  def test_article_model(self):
    Article.objects.create(title='title', content='content1', slug='slugy1')
    Article.objects.create(title='title2', content='content2', slug='slugy2')
    object_1 = Article.objects.get(title='title')
    object_1.title = 'title1'
    object_2 = Article.objects.get(title='title2')

    self.assertEqual(object_1.title, 'title1')
    self.assertNotEqual(object_1.title, 'title2')
    self.assertEqual(len(object_1.title), 6)
    self.assertIsNot(object_1, object_2)