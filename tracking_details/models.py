from django.db import models
from django.utils import timezone
import string, random

# id genarator
def id_genarator(length=7, var=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(var) for _ in range(length))

# date limit genarator
def limit_day():
    var = timezone.now() + timezone.timedelta(days=21)
    return var
def next_day():
    num = 0
    while num < 22:
        var = timezone.now() + timezone.timedelta(days=num)
        if var != timezone.now() + timezone.timedelta(days=22):
            num += 1
            return num
        elif var == timezone.now() + timezone.timedelta(days=22):
            return 100

    
# client package information
class User_Package_Detail(models.Model):
    choice = {
        ('active', 'active'),
        ('pending', 'pending'),
        ('delayed', 'delayed'),
        ('waiting comfirmation', 'waiting comfirmation'),
    }
    tracker = models.CharField(unique=True ,blank=True, null=True, max_length=7, default=id_genarator)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, default='None Added')
    content = models.CharField(max_length=100, default='i-Phone12, D&G Designers Hand Bag')
    date_pushed = models.DateField(default=timezone.now)
    delivery_date = models.DateField(default=limit_day)
    progress = models.IntegerField(default=next_day, blank=True, null=True,)
    current_location = models.CharField(max_length=20)
    status = models.CharField(max_length=21, choices=choice ,default=3)

    def __str__(self) -> str:
        return self.name