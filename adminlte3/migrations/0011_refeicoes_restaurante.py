# Generated by Django 3.2.12 on 2023-07-28 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte3', '0010_alimentos_tipoalimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refeicoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ide_municipio', models.IntegerField()),
                ('dat_ano', models.IntegerField()),
                ('dat_mes', models.IntegerField()),
                ('ide_restaurante', models.IntegerField()),
                ('des_faixaetaria', models.CharField(max_length=50)),
                ('ide_tipo_refeicao', models.IntegerField()),
            ],
            options={
                'db_table': 'refeicoes',
            },
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des_restaurante', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'restaurante',
            },
        ),
    ]