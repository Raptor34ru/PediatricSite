from django.db import models
from django.urls import reverse


class General(models.Model):
    title = models.CharField(max_length=100, verbose_name='Ф.И.О.')
    address = models.CharField(max_length=100, verbose_name='Адрес')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    content = models.TextField(blank=True, verbose_name='Контент')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заведующую кафедрой'
        verbose_name_plural = 'Заведующая кафедрой'


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-time_created']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'


class Sotr(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ф.И.О.')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    job_title = models.CharField(max_length=100, verbose_name='Должность')
    education = models.CharField(max_length=100, verbose_name='Образование', blank=True)
    phone = models.IntegerField(verbose_name='Телефон')
    email = models.EmailField(max_length=100, verbose_name='E-mail', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Articles(models.Model):
    Group_user = models.CharField(max_length=15, default='', verbose_name='Пользователи группы')
    Subject = models.CharField(max_length=120, verbose_name='Предмет')
    Teacher = models.CharField(max_length=120, verbose_name='Преподаватель')

    even = 'Четная'
    odd = 'Нечетная'
    same = 'Еженедельно'
    type_of_week_choices = (
        (even, 'Четная'),
        (odd, 'Нечетная'),
        (same, 'Еженедельно'),
    )
    type_of_week = models.CharField(max_length=20, choices=type_of_week_choices, default=same, verbose_name='Тип '
                                                                                                            'недели')

    Monday = '1Понедельник'
    Tuesday = '2Вторник'
    Wednesday = '3Среда'
    Thursday = '4Четверг'
    Friday = '5Пятница'
    Saturday = '6Суббота'
    day_of_week_choices = (
        (Monday, 'Понедельник'),
        (Tuesday, 'Вторник'),
        (Wednesday, 'Среда'),
        (Thursday, 'Четверг'),
        (Friday, 'Пятница'),
        (Saturday, 'Суббота'),
    )
    day_of_week = models.CharField(max_length=20,choices=day_of_week_choices,default=Monday, verbose_name='День недели')

    First = '1'
    Second = '2'
    Third = '3'
    Fourth = '4'
    Fifth = '5'
    Sixth = '6'
    time_of_day_choices = (
        (First, 'Первая'),
        (Second, 'Вторая'),
        (Third, 'Третья'),
        (Fourth, 'Четвертая'),
        (Fifth, 'Пятая'),
        (Sixth, 'Шестая'),
    )
    time_of_day = models.CharField( max_length=1,choices=time_of_day_choices,default=First, verbose_name='Время дня')
    Classes = models.CharField(max_length=10, verbose_name='Аудитория')

    def __str__(self):
        return self.Subject

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
