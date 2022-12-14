# Generated by Django 4.1.3 on 2022-11-25 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('star_nv', '0010_places_restaurent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Review',
            fields=[
                ('article_id', models.AutoField(primary_key=True, serialize=False)),
                ('article_name', models.CharField(blank=True, max_length=100, null=True)),
                ('book_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['article_name'],
                'abstract': False,
            },
        ),
    ]
