from django.db import models


class Author(models.Model):
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=64,
    )

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=128,
    )

    middle_name = models.CharField(
        verbose_name='Отчество (второе имя)',
        max_length=64,
    )

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(
        verbose_name='Название',
        max_length=128,
    )

    image = models.URLField(verbose_name='Изображение')

    author = models.ForeignKey(
        Author,
        verbose_name='Автор',
        on_delete=models.CASCADE,
    )
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

class File(models.Model):
    file = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.file.name