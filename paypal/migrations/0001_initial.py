# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PayPalResponseStatus'
        db.create_table(u'paypal_paypalresponsestatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'paypal', ['PayPalResponseStatus'])

        # Adding model 'PayPalResponse'
        db.create_table(u'paypal_paypalresponse', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('token', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=256, null=True, blank=True)),
            ('trans_id', self.gf('django.db.models.fields.CharField')(db_index=True, max_length=256, null=True, blank=True)),
            ('correlation_id', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('response', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('error_msg', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('error', self.gf('django.db.models.fields.CharField')(max_length=512, null=True, blank=True)),
            ('currencycode', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('raw_response', self.gf('django.db.models.fields.TextField')()),
            ('charged', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=7, decimal_places=2, blank=True)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['paypal.PayPalResponseStatus'])),
            ('payment_received', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'paypal', ['PayPalResponse'])


    def backwards(self, orm):
        # Deleting model 'PayPalResponseStatus'
        db.delete_table(u'paypal_paypalresponsestatus')

        # Deleting model 'PayPalResponse'
        db.delete_table(u'paypal_paypalresponse')


    models = {
        u'paypal.paypalresponse': {
            'Meta': {'object_name': 'PayPalResponse'},
            'charged': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'}),
            'correlation_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'currencycode': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'error': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'error_msg': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_received': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'raw_response': ('django.db.models.fields.TextField', [], {}),
            'response': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['paypal.PayPalResponseStatus']"}),
            'token': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'trans_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        u'paypal.paypalresponsestatus': {
            'Meta': {'object_name': 'PayPalResponseStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['paypal']