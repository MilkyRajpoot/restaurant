# Generated by Django 3.1.4 on 2020-12-24 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resFood', '0003_auto_20201224_2328'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='foodCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='fooditem',
            name='attribute',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='resFood.foodattribute'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resFood.foodcategory'),
        ),
        migrations.DeleteModel(
            name='foodChoice',
        ),
    ]