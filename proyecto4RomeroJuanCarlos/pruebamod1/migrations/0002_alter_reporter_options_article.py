# Generated by Django 5.1.4 on 2025-01-24 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pruebamod1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reporter',
            options={'ordering': ['-id'], 'verbose_name': 'Reportero'},
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('pub_date', models.DateField()),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebamod1.reporter')),
            ],
            options={
                'verbose_name': 'Articulo',
                'db_table': 'articulo',
                'ordering': ['headline'],
            },
        ),
    ]
