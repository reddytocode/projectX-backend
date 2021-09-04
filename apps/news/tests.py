from django.test import TestCase

from apps.news.models import News


class TestModels(TestCase):
    def setUp(self):
        pass

    def test_news(self):
        count = News.objects.count()
        News.objects.create(
            title="asdf", link="asdf", content="asdfasdfa", author="213242fs"
        )
        self.assertEqual(News.objects.count(), count + 1)
