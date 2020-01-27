from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Unique(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Property(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(default='default.jpg', upload_to='property_pics')
    description = models.TextField(default='Modern Apartments')
    price = models.IntegerField(default='0')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    uniqueness = models.ForeignKey(Unique, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 
