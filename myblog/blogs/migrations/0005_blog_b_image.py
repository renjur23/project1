# Generated by Django 5.0.6 on 2024-07-08 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_rename_author_name_blog_a_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='b_image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_image/'),
        ),
    ]