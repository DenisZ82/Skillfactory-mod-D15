from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category


# D11
class Command(BaseCommand):
    help = 'Удаление всех новостей из какой-либо категории'

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no: ')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
            return
        try:
            category = Category.objects.get(name=options['category'])
            Post.objects.filter(category_post_many__name=category.name).delete()  # либо (category_post_many=category)
            self.stdout.write(self.style.SUCCESS(f'Успешно удалены все новости из категории {category.name}'))  # в случае неправильного подтверждения говорим, что в доступе отказано
        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Не удалось найти категорию {options["category"]}'))
