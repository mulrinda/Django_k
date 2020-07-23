# Generated by Django 2.1.15 on 2020-07-23 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_name', models.CharField(max_length=500)),
                ('show_img', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Showman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('showman_name', models.CharField(max_length=500)),
                ('showman_img', models.CharField(max_length=500)),
                ('showman_likenum', models.IntegerField()),
                ('show_cd', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='enters.Show')),
                ('spot_cd', models.ManyToManyField(null=True, related_name='spot_show', to='maps.Spot')),
            ],
        ),
    ]
