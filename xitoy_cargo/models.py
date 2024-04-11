from django.core.exceptions import ValidationError
from django.db import models

class Trek(models.Model):
    trek_code = models.CharField(max_length=32,unique=True)

    def __str__(self):
        return self.trek_code


class Key(models.Model):
    key_word = models.CharField(max_length=16)
    key_gaven_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.key_word + " - " + f"{self.key_gaven_date}"

class Client(models.Model):
    phone_number = models.CharField(max_length=16,blank=True,null=True)
    fullname = models.CharField(max_length=64)
    telegram_id = models.CharField(max_length=32,unique=True)
    kalit_soz = models.ForeignKey(Key, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        if not self.kalit_soz:

            obj = Key.objects.create(key_word="AAA")
            obj.key_word += f"{obj.id}"
            obj.save()
            self.kalit_soz = obj
        super().save(*args, **kwargs)


class Available_party(models.Model):
    # uchgan reyslar
    partiya_name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=True)
    registered_date = models.DateField(auto_now_add=True)
    arrived_date = models.DateField(auto_now=True,blank=True, null=True)

    def __str__(self):
        return self.partiya_name

class Chine_Db(models.Model):
    partiya = models.ForeignKey(Available_party, on_delete=models.CASCADE)
    id_raqam = models.ForeignKey(Key, on_delete=models.CASCADE)
    trek_code = models.ForeignKey(Trek, on_delete=models.CASCADE,related_name='chine_db')

    product_name = models.CharField(max_length=64)
    count_of_product = models.IntegerField(null=True)
    massa_of_product = models.FloatField()
    karopka_nomi = models.CharField(max_length=64)
    accepted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product_name

class Uzbek_Db(models.Model):
    CHOICES = [
        ("TOLANGAN", 'To\'langan'),
        ("TO'LANMAGAN", 'To\'lanmagan'),
    ]
    status = models.CharField(max_length=16, choices=CHOICES,default=CHOICES[0][0])
    massa_of_product = models.IntegerField()
    price_for_kg = models.DecimalField(decimal_places=2, max_digits=4)
    accepted_date = models.DateField(auto_now_add=True)

    id_raqam = models.ForeignKey(Key, on_delete=models.CASCADE)
    partiya = models.ForeignKey(Available_party, on_delete=models.CASCADE)
    trek_code = models.ForeignKey(Trek, on_delete=models.CASCADE,related_name='uzbek_db')

    def save(self, *args, **kwargs):
        if self.trek_code.id not in list(Chine_Db.objects.values_list('trek_code', flat=True)):
            raise ValidationError("Trek code is not in Chine_Db")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.id_raqam

