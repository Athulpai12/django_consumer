# Generated by Django 3.1.7 on 2021-03-29 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_view', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='appointment_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='user_id',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
    ]