# Generated by Django 2.2.5 on 2019-11-25 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(blank=True, editable=False, max_length=100),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, editable=False, max_length=100)),
                ('comment_text', models.TextField()),
                ('comment_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified_time', models.DateTimeField(auto_now=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogs.Blog')),
            ],
        ),
    ]
