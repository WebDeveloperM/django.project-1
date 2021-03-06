# Generated by Django 4.0.1 on 2022-02-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('teaching_course', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
