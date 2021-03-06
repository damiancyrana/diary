# Generated by Django 3.0.6 on 2020-05-11 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('addition_time', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diary.Subject')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
