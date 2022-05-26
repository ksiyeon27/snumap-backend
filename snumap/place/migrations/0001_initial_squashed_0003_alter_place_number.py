# Generated by Django 4.0.3 on 2022-05-22 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('place', '0001_initial'), ('place', '0002_alter_place_category_alter_place_type'), ('place', '0003_alter_place_number')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.PositiveSmallIntegerField(null=True)),
                ('category', models.PositiveSmallIntegerField(choices=[('0', '시설(etc)'), ('1', '인문대학'), ('2', '사범대학'), ('3', '사회과학대학'), ('4', '자연과학대학'), ('5', '약학대학'), ('6', '공과대학'), ('7', '미술대학 및 음악대학'), ('8', '경영대학'), ('9', '수의과대학'), ('10', '생활과학대학'), ('11', '농업생명과학대학'), ('12', '자유전공학부'), ('13', '행정대학원'), ('14', '환경대학원'), ('15', '국제대학원'), ('16', '치의학대학원'), ('17', '법학전문대학원'), ('18', '데이터사이언스대학원')], default='0')),
                ('type', models.PositiveSmallIntegerField(choices=[('0', 'etc'), ('1', 'building'), ('2', 'atm'), ('3', 'playfield'), ('4', 'parking_lot')], default='0')),
                ('information', models.CharField(max_length=500, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='places', to='place.location')),
                ('tags', models.ManyToManyField(related_name='tag_places', to='place.tag')),
            ],
        ),
    ]
