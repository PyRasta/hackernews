from django.db import models
from django.db.models.fields import DateField


class Article(models.Model):
    title = models.CharField("Название", max_length=100)
    url = models.CharField('Адрес', max_length=150)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title    

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"    
        
class CreateAccount(models.Model):
    name = models.CharField("Пользователь", max_length=30)
    password = models.CharField("Пароль", max_length=50)       

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"    