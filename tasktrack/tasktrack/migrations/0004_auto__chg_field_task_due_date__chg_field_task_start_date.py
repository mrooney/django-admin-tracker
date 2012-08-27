# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Task.due_date'
        db.alter_column('tasktrack_task', 'due_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Task.start_date'
        db.alter_column('tasktrack_task', 'start_date', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # Changing field 'Task.due_date'
        db.alter_column('tasktrack_task', 'due_date', self.gf('django.db.models.fields.DateField')(default=None))

        # Changing field 'Task.start_date'
        db.alter_column('tasktrack_task', 'start_date', self.gf('django.db.models.fields.DateField')(default=None))

    models = {
        'tasktrack.project': {
            'Meta': {'object_name': 'Project'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'tasktrack.task': {
            'Meta': {'object_name': 'Task'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'hours': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tasktrack.Project']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['tasktrack']