from django.db import models

# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField()
	mobile=models.CharField(max_length=10)
	number=models.CharField(max_length=15)
	age=models.IntegerField(null=True)

	def __str__(self):
		return self.name + ' ' + self.email
