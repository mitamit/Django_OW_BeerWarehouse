from django.conf import settings
from django.db import models
from django.utils.timezone import now

class CommonInfo(models.Model):
    created_at = models.DateTimeField('Created at', default=now, blank=True)
    last_modified_at = models.DateTimeField('Last modified at', default=now, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.DO_NOTHING, verbose_name='Created by', blank=True, null=True,
                                     related_name="%(app_label)s_%(class)s_created")
    last_modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.DO_NOTHING, verbose_name='Last modified by', blank=True, null=True,
                                     related_name="%(app_label)s_%(class)s_last_modified")

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = now()

        self.last_modified_at = now()
        super(CommonInfo, self).save(*args, **kwargs)

    class Meta:
        abstract = True