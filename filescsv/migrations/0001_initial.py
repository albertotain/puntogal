# Generated by Django 4.0.5 on 2022-06-02 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filescsv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roid', models.CharField(max_length=255, verbose_name='roid')),
                ('domain_name', models.CharField(max_length=255, verbose_name='domain-name')),
                ('creation_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Arquivo CSV',
                'verbose_name_plural': 'Arquivos CVS',
            },
        ),
    ]
