# Generated by Django 4.2.7 on 2023-12-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskTitle', models.CharField(max_length=255)),
                ('taskDescription', models.TextField()),
                ('is_completed', models.BooleanField(default=False)),
                ('taskAssignedDate', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(to='category.category')),
            ],
        ),
    ]