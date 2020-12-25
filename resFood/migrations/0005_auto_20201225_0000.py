# Generated by Django 3.1.4 on 2020-12-24 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resFood', '0004_auto_20201224_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='attribute',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resFood.foodattribute'),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resFood.foodcategory'),
        ),
    ]
