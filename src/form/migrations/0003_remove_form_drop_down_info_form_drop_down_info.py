# Generated by Django 4.2.7 on 2023-11-22 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_remove_form_drop_down_info_form_drop_down_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='drop_down_info',
        ),
        migrations.AddField(
            model_name='form',
            name='drop_down_info',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='form.dropdownside', verbose_name='drop down data'),
            preserve_default=False,
        ),
    ]