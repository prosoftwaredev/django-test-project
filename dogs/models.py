from django.db import models
from django.core.urlresolvers import reverse


class dogs(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dogs:dogs_edit', kwargs={'pk': self.pk})