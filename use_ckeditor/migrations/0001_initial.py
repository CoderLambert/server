# Generated by Django 2.0.3 on 2018-03-28 13:03

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='contents')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='express_time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='update_time')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='use_ckeditor.Category'),
        ),
    ]
