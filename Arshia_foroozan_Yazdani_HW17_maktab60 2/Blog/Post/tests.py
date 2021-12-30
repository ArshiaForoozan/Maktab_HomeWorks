from django.test import TestCase
from .models import Post, comment
class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        post = Post.objects.create(title='arshia', description='arshia foroozan', author='arshia')
        comments = comment.objects.create(post=post, text='in bade')

    def test_title_content(self):
        post = Post.objects.get(id = 1)
        expected_name = f'{post.title}'
        self.assertEqual("arshia", expected_name)
    
    def test_comment_text(self):
        comments = comment.objects.get(id = 1)
        expected_name = f'{comments.text}'
        self.assertEqual("in bade", expected_name)