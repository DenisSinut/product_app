from django.db import models
from datetime import datetime, timezone
class Student(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')



    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'Студенты'

class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    owner = models.CharField(max_length=255, verbose_name='Автор')
    start_time = models.DateTimeField(verbose_name='Время старта')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Стоимость')
    lessons = models.ManyToManyField('Lesson', verbose_name='Уроки', blank=True, related_name='pr')
    max_count = models.IntegerField(default=0, verbose_name='Максимальное количество студентов в группе')
    min_count = models.IntegerField(default=0, verbose_name='Минимальное количество студентов в группе')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Курсы'

class Access(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE, verbose_name='Студент', related_name='access')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт', related_name='access')
    value = models.BooleanField(default=False, verbose_name='Доступ к курсу')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        groups_edit = Group.objects.filter(product=self.product)
        min_value = self.product.min_count
        max_value = self.product.max_count
        list_students = []
        if self.value:
            for item in groups_edit:
                if len(item.students.values_list()) < max_value:
                    item.students.add(self.student)
                    break
            if datetime.now(timezone.utc) < self.product.start_time:
                for item in groups_edit:
                    list_students += list(item.students.all())

                count = round(len(list_students) / len(groups_edit))

                for groups_add in groups_edit:
                    if groups_add != groups_edit[len(groups_edit)-1]:
                        groups_add.students.set(list_students[:count])
                        del list_students[:count]
                    else:
                        groups_add.students.set(list_students)

        else:
            for item in groups_edit:
                if self.student in item.students.all():
                    item.students.remove(self.student)
                    break


    class Meta:
        verbose_name_plural = 'Доступы к курсам'


class Lesson(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    link = models.SlugField(unique=True, verbose_name='Ссылка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Уроки'

class Group(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    students = models.ManyToManyField('Student', verbose_name='Студенты', blank=True)
    product = models.ForeignKey('Product', on_delete=models.SET_NULL, verbose_name='Продукт', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Группы'