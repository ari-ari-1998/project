from django.db import models


class NippoModel(models.Model):
    company = models.CharField(max_length=100)
    company_id = models.CharField(max_length=100)
    company_password = models.CharField(max_length=100)
    def __str__(self):
        return self.company
    