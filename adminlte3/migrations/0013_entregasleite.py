# Generated by Django 3.2.12 on 2023-08-02 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte3', '0012_produtor'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntregasLeite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_entrega', models.IntegerField()),
                ('mes_entregs', models.IntegerField()),
                ('ide_municipio', models.IntegerField()),
                ('ide_laticinio', models.IntegerField()),
                ('ide_entidade', models.IntegerField()),
                ('ide_tipo_leite', models.CharField(max_length=1)),
                ('qtd_entrega', models.FloatField()),
                ('val_entrega', models.FloatField()),
            ],
            options={
                'db_table': 'entregas_leite',
            },
        ),
    ]
