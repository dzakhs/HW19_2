from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list= [
            {"name": "LG", "description": "Двухкамерный холодильник", "image": "product/media/Lg.jpg", "category_id":5, "price": 20000},
            {"name": "Liebherr", "description": "Двухкамерный холодильник с вместительной морозильной камерой", "image":"product/media/liebherr.jpg", "category_id":5, "price": 40000},
            {"name": "Saeco", "description": "Кофемашина с предустановленными настройками", "image":"product/media/Saeco.jpg", "category_id":7, "price": 30000},
            {"name": "Iphone 13 Pro Max", "description": "Смартфон с объемом памяти 256гб", "image": "product/media/Iphone.jpg", "category_id":1, "price": 100000 }

        ]
        product_for_create = []
        for product in product_list:
            product_for_create.append(Product(**product))

        Product.objects.all().delete()
        Product.objects.bulk_create(product_for_create)