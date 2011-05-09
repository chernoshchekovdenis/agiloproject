# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Request'
        db.create_table('db_requests_request', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request_body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('db_requests', ['Request'])


    def backwards(self, orm):
        
        # Deleting model 'Request'
        db.delete_table('db_requests_request')


    models = {
        'db_requests.request': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'Request'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request_body': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['db_requests']
