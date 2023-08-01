# Generated by Django 4.2.3 on 2023-07-28 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog_images/')),
                ('title', models.CharField(max_length=200)),
                ('detail', models.TextField(max_length=500)),
                ('post_date', models.DateField()),
            ],
        ),
    ]
