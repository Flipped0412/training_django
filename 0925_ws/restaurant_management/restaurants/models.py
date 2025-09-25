from django.db import models

class Restaurant(models.Model):
    name = models.CharField("식당 이름", max_length=100)
    description = models.TextField("식당 설명", blank=True)
    address = models.TextField("식당 주소")
    phone = models.CharField("식당 전화번호", max_length=20, blank=True)

    def __str__(self):
        return self.name
