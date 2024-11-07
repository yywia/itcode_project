from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255, unique=True)
    release_date = models.DateField(verbose_name='Дата выхода', blank=True, null=True)
    is_alpha = models.BooleanField(verbose_name='Альфа версия', default=False)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    price = models.FloatField(blank=True, null=True, verbose_name='Цена')
    image = models.ImageField(upload_to='media', verbose_name='Изображение', blank=True, null=True)
    developer = models.ForeignKey(
        'Developer',
        verbose_name='Разработчик',
        blank=True,
        null=True,
        related_name='games',
        on_delete=models.SET_NULL,
    )
    publisher = models.ForeignKey(
        'Publisher',
        verbose_name='Издатель',
        blank=True,
        null=True,
        related_name='games',
        on_delete=models.SET_NULL,
    )

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
        ordering = ['title']

    def __str__(self):
        return self.title

class Publisher(models.Model):
    name = models.CharField(verbose_name='Имя издателя', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'
        ordering = ['name']

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(verbose_name='Имя разработчика', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'
        ordering = ['name']

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True)
    games = models.ManyToManyField(
        Game,
        verbose_name='Игры',
        related_name='genres',
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['name']

    def __str__(self):
        return self.name

class Reviews(models.Model):
    author = models.CharField(verbose_name='Автор', max_length=255)
    text = models.TextField(verbose_name='Текст')
    is_recommended = models.BooleanField(verbose_name='Рекомендовано')
    score = models.FloatField(verbose_name='Оценка', blank=True, null=True)
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='reviews',
        verbose_name='Игра'
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['score']

    def __str__(self):
        return f'{self.author} - {self.score} - {self.text}'

class Statistics(models.Model):
    review_score = models.FloatField(default=0.0)
    review_amount = models.IntegerField(default=0)
    game = models.OneToOneField(
        Game,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='statistics',
        verbose_name='Игра'
    )

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'
        ordering = ['review_score']

    def __str__(self):
        return str(self.review_score)