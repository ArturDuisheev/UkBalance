# Generated by Django 4.2.7 on 2023-11-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='section_text',
            field=models.ManyToManyField(to='main_page.sectionincard', verbose_name='секция по тексту '),
        ),
    ]