from django.db import models
from django.urls import reverse

class Link(models.Model):
    url = models.URLField(verbose_name='Початкове посилання')
    short_link = models.CharField(max_length=50, unique=True, verbose_name='Скорочене посилання')
    created = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)
    
    def __str__(self):
        return self.short_link
    
    def get_absolute_url(self):
        return reverse('link_stat', args=[self.short_link])    

