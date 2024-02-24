from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    completed = models.BooleanField(default=False, verbose_name="Выполнен")
    created = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return "{}. {}".format(self.pk, self.summary)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
