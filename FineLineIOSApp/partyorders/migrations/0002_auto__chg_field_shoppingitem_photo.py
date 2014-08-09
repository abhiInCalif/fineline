# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ShoppingItem.photo'
        db.alter_column(u'partyorders_shoppingitem', 'photo', self.gf('django.db.models.fields.URLField')(max_length=512))

    def backwards(self, orm):

        # Changing field 'ShoppingItem.photo'
        db.alter_column(u'partyorders_shoppingitem', 'photo', self.gf('django.db.models.fields.files.FileField')(max_length=100))

    models = {
        u'partyorders.delivery': {
            'Meta': {'object_name': 'Delivery'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'datetime': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'partyorders.order': {
            'Meta': {'object_name': 'Order'},
            'delivery': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['partyorders.Delivery']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'personName': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'partyorders.orderitem': {
            'Meta': {'object_name': 'OrderItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['partyorders.ShoppingItem']", 'unique': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['partyorders.Order']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        u'partyorders.shoppingitem': {
            'Meta': {'object_name': 'ShoppingItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'photo': ('django.db.models.fields.URLField', [], {'max_length': '512'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'sku': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['partyorders']