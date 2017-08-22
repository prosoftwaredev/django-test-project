from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

class owners(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=200)
    date = models.DateField()

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('owners:owners_edit', kwargs={'pk': self.pk})