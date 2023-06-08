from django.core.management import BaseCommand

from catalog.models import Blog


class Command(BaseCommand):
    def handle(self, *args, **options):
        blog_list= [
            {"id": 1, "name": "Реки", "content": "Рассказ про сплав по очень опасной реке", "image": "blog/media/river.jpg"},
            {"id": 2,"name": "Горы", "content": "Невероятный рассказ про горы",
             "image": "blog/media/Mountain.jpg"},
            {"id": 3,"name": "Пещеры", "content": "Увлекательные факты про какие-то затерянные пещеры",
             "image": "blog/media/Hall.jpg"},


        ]
        blog_for_create = []
        for blog in blog_list:
            blog_for_create.append(Blog(**blog))

        Blog.objects.all().delete()
        Blog.objects.bulk_create(blog_for_create)