# Generated by Django 3.2.12 on 2023-07-16 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='municipio',
            name='alt_municipio',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='municipio',
            name='area_municipio',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='municipio',
            name='des_status',
            field=models.CharField(default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='municipio',
            name='ind_capital',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='municipio',
            name='lat_municipio',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='municipio',
            name='lon_municipio',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='municipio',
            name='qtd_populacao',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]
