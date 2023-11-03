# Generated by Django 3.2.12 on 2023-07-28 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte3', '0011_refeicoes_restaurante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf_produtor', models.IntegerField()),
                ('des_produtor', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'produtor',
            },
        ),
    ]
