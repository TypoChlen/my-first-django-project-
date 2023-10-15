from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=255)  # максимальное значение длины строки 
                                              # для поле title для каждоый категории
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    """Показывает реальное название категории
    Programming а не Categoryes1"""
    
class Course(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField()
    students_qty = models.IntegerField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # при удалении категории
                                                                      # автоматически будут удалены все курсы в этой категории
    # так же устанавливает связь между моделью Course и моделью Category
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title