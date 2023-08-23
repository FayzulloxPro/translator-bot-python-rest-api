# Generated by Django 4.2.3 on 2023-07-21 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TranslationResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=10)),
                ('confidence', models.FloatField()),
                ('translation', models.TextField()),
                ('destination', models.CharField(max_length=10)),
            ],
        ),
    ]
