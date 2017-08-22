from django.db import models
from django.core.urlresolvers import reverse


class cats(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cats:cats_edit', kwargs={'pk': self.pk})