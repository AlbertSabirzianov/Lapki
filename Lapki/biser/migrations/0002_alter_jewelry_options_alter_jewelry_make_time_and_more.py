# Generated by Django 4.2 on 2023-05-03 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jewelry',
            options={'ordering': ['-make_time']},
        ),
        migrations.AlterField(
            model_name='jewelry',
            name='make_time',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='jewelry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biser.jewelry'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('make_time', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('mail', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=17)),
                ('jewelry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biser.jewelry')),
            ],
            options={
                'ordering': ['-make_time'],
            },
        ),
    ]