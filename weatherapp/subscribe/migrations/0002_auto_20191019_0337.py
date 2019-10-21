# Generated by Django 2.2.5 on 2019-10-19 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]