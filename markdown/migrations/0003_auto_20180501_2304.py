# Generated by Django 2.0.3 on 2018-05-01 15:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('use_ckeditor', '0016_article_auther'),
        ('markdown', '0002_auto_20180425_2246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='markdownartical',
            options={'verbose_name': 'Markdown文章', 'verbose_name_plural': 'Markdown文章'},
        ),
        migrations.AddField(
            model_name='markdownartical',
            name='link_address',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='转载地址'),
        ),
        migrations.AddField(
            model_name='markdownartical',
            name='original',
            field=models.CharField(choices=[('yes', '是'), ('no', '否')], default='yes', max_length=6, verbose_name='是否原创'),
        ),
        migrations.AddField(
            model_name='markdownartical',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='发表时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='markdownartical',
            name='tag',
            field=models.ManyToManyField(blank=True, to='use_ckeditor.Category', verbose_name='标签名'),
        ),
        migrations.AddField(
            model_name='markdownartical',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
    ]
