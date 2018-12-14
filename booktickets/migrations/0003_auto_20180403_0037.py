# Generated by Django 2.0.1 on 2018-04-03 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booktickets', '0002_auto_20180403_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('movie_name', models.CharField(max_length=60)),
                ('director', models.CharField(max_length=20)),
                ('cast', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('duration', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SeatAllocation',
            fields=[
                ('audi_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('row_name', models.CharField(max_length=6)),
                ('no_of_seats', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShowMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktickets.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('theatre_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('theatre_name', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='showmovie',
            name='theatre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktickets.Theatre'),
        ),
        migrations.AddField(
            model_name='seatallocation',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktickets.ShowMovie'),
        ),
    ]