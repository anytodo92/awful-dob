# Generated by Django 4.0.4 on 2022-06-30 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_blogs_paragraph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='paragraph',
            field=models.TextField(default=False),
        ),
    ]
