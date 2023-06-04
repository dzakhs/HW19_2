from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list= [
            {"id":1, "name":"Смартфоны", "description": "Смартфоны"},
            {"id":2, "name":"Телевизоры", "description":"Телевизоры"},
            {"id":4, "name":"Компьютеры", "description":"Компьютеры, ноутбуки, планшеты"},
            {"id":5, "name":"Холодильники", "description":"Бытовая техника"},
            {"id":6, "name":"Микроволновые печи", "description":"Бытовая техника"},
            {"id":7, "name":"Кофемашины", "description":"Бытовая техника"}

        ]
        category_for_create = []
        for category in category_list:
            category_for_create.append(Category(**category))

        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)