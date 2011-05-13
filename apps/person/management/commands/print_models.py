from django.core.management.base import BaseCommand
from django.db.models import get_apps, get_models


class Command(BaseCommand):
    args = ''
    help = 'prints all project models and the count of objects in every model'

    def handle(self, *args, **options):
        apps_list = get_apps()
        for app in apps_list:
            models_list = get_models(app)
            for model in models_list:
                model_name = model._meta.object_name
                count = model.objects.count()
                self.stdout.write('%s: %i\n' % (model_name, count))
                self.stderr.write('Error::  %s: %i\n' % (model_name, count))