from django.db import models


class DemoTable(models.Model):
    attr1 = models.CharField(max_length=100)
    attr2 = models.CharField(max_length=100)

    def __str__(self):
        return self.attr1
