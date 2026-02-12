from django.db import models

# Create your models here.

class MainBoard(models.Model):
    # create a list of 9 inner boards
    # have a win boolean value


class InnerBoard(models.Model):
    # create a list of 9 cells
    # add a playable boolean value
    # have a inner board win value ('x', 'o')

class Cell(models.Model):
    value = models.CharField(max_length=1)

    def __str__(self):
        return self.value