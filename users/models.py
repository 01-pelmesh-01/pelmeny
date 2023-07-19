from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class story (models.Model):
    name = models.CharField (max_length = 250)
    desс = models.TextField('основная информация' , blank = True)
    image = models.ImageField(upload_to='static\media\img',  blank = True)
    creator = models.ForeignKey('CustomUser' , on_delete = models.CASCADE , null = True , blank = True )
    like_amount = models.IntegerField(default ='0')

    def __str__ (self):     
      return self.name;
    class Meta:
       verbose_name = 'МУЖСКОЙ сторис'
       verbose_name_plural = 'МУЖИТСКИЕ сторисы'


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default = False)
    code = CharField(max_length=16, blank = True)    
    premium = models.BooleanField(default = False)
    like = models.ManyToManyField(story)


from django.dispatch import receiver
from django.db.models.signals import post_save

class UserPayment(models.Model):
	app_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	payment_bool = models.BooleanField(default=False)
	stripe_checkout_id = models.CharField(max_length=500)

@receiver(post_save, sender=CustomUser)
def create_user_payment(sender, instance, created, **kwargs):
	if created:
		UserPayment.objects.create(app_user=instance)

# Create your models here.
