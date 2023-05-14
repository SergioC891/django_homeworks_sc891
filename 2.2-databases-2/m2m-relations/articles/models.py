from django.db import models


class Tag(models.Model):

    tag = models.CharField(max_length=256, verbose_name='Название')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статьи'
        ordering = ['tag']

    def __str__(self):
        return self.tag


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    scopes = models.ManyToManyField(Tag, through='Scope', related_name='scopes')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):

    articles = models.ForeignKey('Article', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, verbose_name='Раздел')
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статьи'
        ordering = ['-is_main', 'tag']

    def __str__(self):
        return f'{self.tag}'
