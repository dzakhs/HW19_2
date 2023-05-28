from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list= [
            {"name":"Смартфоны"  , "description": "Смартфоны"},
            {"name":"Телевизоры", "description":"Телевизоры"},
            {"name":"Компьютеры", "description":"Компьютеры, ноутбуки, планшеты"},
            {"name":"Холодильники", "description":"Бытовая техника"},
            {"name":"Микроволновые печи", "description":"Бытовая техника"},
            {"name":"Кофемашины", "description":"Бытовая техника"}

        ]
        category_for_create = []
        for category in category_list:
            category_for_create.append(Category(**category))

        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)