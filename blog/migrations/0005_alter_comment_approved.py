# Generated by Django 4.2.10 on 2024-02-20 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
