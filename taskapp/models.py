from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.



class Content(models.Model):
    title                  = models.CharField(max_length=150, null=False)
    body                   = models.TextField()
    average_score          = models.DecimalField(default=0, max_digits=5, decimal_places=1)
    number_of_users_rated  = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.title


class Rate(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    score   = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.content.title