# Generated by Django 5.0.4 on 2024-05-20 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_alter_production_cast_alter_production_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfiladministrador',
            name='password',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perfiladministrador',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
