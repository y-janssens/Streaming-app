# Generated by Django 4.0.3 on 2022-03-27 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
                ('length', models.IntegerField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
