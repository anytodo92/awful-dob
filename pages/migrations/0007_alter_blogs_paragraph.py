# Generated by Django 4.0.4 on 2022-06-30 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_blogs_paragraph_alter_blogs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='paragraph',
            field=models.TextField(default='fndjkfkjdfkjdjkfkjdsfkjdsfjdsfjkdsjf'),
        ),
    ]
