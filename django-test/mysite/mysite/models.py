from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)
    carmodel = models.CharField(max_length=50)
    def __str__(self): 
        return self.make + ' ' + self.carmodel


class Employee(models.Model):
    name = models.CharField(max_length = 20)
    age = models.PositiveIntegerField()
    def __str__(self):
        return self.name + ' ' + str(self.age)