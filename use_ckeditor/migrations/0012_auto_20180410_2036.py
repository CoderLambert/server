# Generated by Django 2.0.3 on 2018-04-10 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('use_ckeditor', '0011_auto_20180410_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='original',
            field=models.CharField(choices=[('yes', '是'), ('no', '否')], default='yes', max_length=6, verbose_name='是否原创'),
        ),
    ]
