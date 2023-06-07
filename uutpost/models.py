from django.conf import settings
from django.db import models
from django.utils import timezone


class Address(models.Model):
    name_addr = models.CharField(max_length=100)
    mobile_addr = models.IntegerField()
    vk_addr = models.CharField(max_length=300)
    tg_addr = models.CharField(max_length=300)
    management_company = models.CharField(max_length=300)

    def __str__(self):
        return self.name_addr


# class Management(models.Model):
#     address = models.ForeignKey('uutpost.Address', on_delete=models.CASCADE)
#     name_man = models.CharField(max_length=100)
#     mobile_man = models.IntegerField()
#     vk_man = models.CharField(max_length=300)
#     tg_man = models.CharField(max_length=300)
#
#     def __str__(self):
#         return self.name_man










