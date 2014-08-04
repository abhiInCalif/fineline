# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ShoppingItem'
        db.create_table(u'partyorders_shoppingitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('sku', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('photo', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'partyorders', ['ShoppingItem'])

        # Adding model 'Delivery'
        db.create_table(u'partyorders_delivery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('datetime', self.gf('django.db.models.fields.CharField')(max_length=512)),
        ))
        db.send_create_signal(u'partyorders', ['Delivery'])

        # Adding model 'Order'
        db.create_table(u'partyorders_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('personName', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('delivery', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['partyorders.Delivery'], unique=True)),
        ))
        db.send_create_signal(u'partyorders', ['Order'])

        # Adding model 'OrderItem'
        db.create_table(u'partyorders_orderitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['partyorders.ShoppingItem'], unique=True)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['partyorders.Order'])),
        ))
        db.send_create_signal(u'partyorders', ['OrderItem'])


    def backwards(self, orm):
        # Deleting model 'ShoppingItem'
        db.delete_table(u'partyorders_shoppingitem')

        # Deleting model 'Delivery'
        db.delete_table(u'partyorders_delivery')

        # Deleting model 'Order'
        db.delete_table(u'partyorders_order')

        # Deleting model 'OrderItem'
        db.delete_table(u'partyorders_orderitem')


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
            'photo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'sku': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['partyorders']