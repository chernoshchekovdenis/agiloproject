from django.db import models
from django.db.models.signals import post_save, post_delete


class ModelCrudLog(models.Model):
    text = models.CharField(max_length=300)

    def __unicode__(self):
        return self.text


def edit(sender, instance, created, **kwargs):
    if sender != ModelCrudLog:
        if created:
            action = "created"
        else:
            action = "updated"
        model_name = sender._meta.object_name
        log_text = "Instance of %s was %s." % (model_name, action)
        ModelCrudLog(text=log_text).save()


def delete(sender, instance, **kwargs):
    if sender != ModelCrudLog:
        model_name = sender._meta.object_name
        log_text = "Instance of %s was deleted." % (model_name)
        ModelCrudLog(text=log_text).save()


post_save.connect(edit)
post_delete.connect(delete)
