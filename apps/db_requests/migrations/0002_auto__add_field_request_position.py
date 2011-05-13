# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Request.position'
        db.add_column('db_requests_request', 'position', self.gf('django.db.models.fields.IntegerField')(default=-1), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Request.position'
        db.delete_column('db_requests_request', 'position')


    models = {
        'db_requests.request': {
            'Meta': {'ordering': "('-id', 'position')", 'object_name': 'Request'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'request_body': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['db_requests']
