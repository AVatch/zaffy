from django.db import models


class Zaffy(models.Model):
    title = models.CharField(max_length=240)
    media = models.URLField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __unicode__(self):
        return self.title
