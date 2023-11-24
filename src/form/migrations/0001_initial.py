# Generated by Django 4.2.7 on 2023-11-22 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DropDownSide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('not_required_sum_investments', models.CharField(max_length=50, verbose_name='not required sum investments')),
                ('not_required_term', models.CharField(max_length=40, verbose_name='not required term')),
            ],
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Name')),
                ('surname', models.CharField(max_length=70, verbose_name='Surname')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('code_country', models.CharField(max_length=5, verbose_name='Code country')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at application: ')),
                ('drop_down_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.dropdownside', verbose_name='drop down data')),
            ],
            options={
                'verbose_name': 'Form data',
                'verbose_name_plural': 'Forms data',
            },
        ),
    ]
