# Generated by Django 5.1.4 on 2024-12-05 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(blank=True, max_length=20, null=True)),
                ('cname', models.CharField(max_length=220)),
                ('cqty', models.CharField(blank=True, max_length=220, null=True)),
                ('cprice', models.CharField(blank=True, max_length=220, null=True)),
            ],
        ),
    ]