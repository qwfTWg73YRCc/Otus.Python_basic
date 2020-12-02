from django.core.management.base import BaseCommand
from index.models import BaseModel


class Command(BaseCommand):
    help = 'Work with db'


    def handle(self, *args, **options):
        # Удаление
        BaseModel.objects.all().delete()
        # Создание
        user1 = BaseModel.objects.create(id='1')
        user2 = BaseModel.objects.create(id='2')
        user3 = BaseModel.objects.create(id='3')
        # Обновление
        user1.id = '1'
        # Сохранение
        user1.save()
        user2.save()
        user3.save()
        # Вывод результата
        print(f"Users` id: ", user1.id,",", user2.id,",", user3.id)
        # Выборка всех данных
        users = BaseModel.objects.all()
        # Вывод всех данных
        for user in users:
            print(user.id)

