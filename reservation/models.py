from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .choices import *


class Table(models.Model):
    table_id = models.CharField(unique=True, help_text="Table ID", max_length=10)
    capacity = models.PositiveSmallIntegerField(validators=[MinValueValidator(2), MaxValueValidator(12)],
                                                help_text="Capacity")
    shape = models.CharField(choices=SHAPE, help_text="Type of the table", max_length=25)
    length = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)],
                                              help_text='Length')
    width = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)],
                                             help_text='Width')

    x_coordinate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)],
                                                    help_text='x')
    y_coordinate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)],
                                                    help_text='y')

    def __str__(self):
        return self.table_id

    class Meta:
        ordering = ['table_id']


class Order(models.Model):
    first_name = models.CharField(max_length=50, help_text='First Name')
    last_name = models.CharField(max_length=50, help_text='Last Name')
    email = models.EmailField(help_text='Email')
    date = models.DateTimeField(help_text='Date')
    table = models.ForeignKey(Table, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name





