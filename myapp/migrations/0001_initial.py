# Generated by Django 4.1.6 on 2023-02-06 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='datagithub',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_project', models.CharField(max_length=100)),
                ('title_project', models.TextField()),
                ('Url_project', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='imgcertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_img', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
    ]
