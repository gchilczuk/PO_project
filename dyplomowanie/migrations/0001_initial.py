# Generated by Django 2.0 on 2018-01-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deklaracja',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('celizakres', models.CharField(blank=True, db_column='CelIzakres', max_length=2000, null=True)),
                ('opis', models.CharField(blank=True, db_column='Opis', max_length=2000, null=True)),
            ],
            options={
                'db_table': 'deklaracja',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormaStudiow',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nazwaformy', models.CharField(db_column='nazwaFormy', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'formastudiow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JezykRealizacji',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nazwajezyka', models.CharField(db_column='nazwaJezyka', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'jezykrealizacji',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NauczycielAkademicki',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('login', models.CharField(db_column='Login', max_length=30, unique=True)),
                ('haslo', models.CharField(db_column='Haslo', max_length=255)),
                ('imie', models.CharField(db_column='Imie', max_length=255)),
                ('nazwisko', models.CharField(db_column='Nazwisko', max_length=255)),
                ('sumagodzin', models.IntegerField(db_column='SumaGodzin')),
            ],
            options={
                'db_table': 'nauczycielakademicki',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PowiadomienieOWyborzeTematu',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'powiadomienieowyborzetematu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='StopienStudiow',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('stopien', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'stopienstudiow',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('login', models.CharField(db_column='Login', max_length=30, unique=True)),
                ('haslo', models.CharField(db_column='Haslo', max_length=255)),
                ('imie', models.CharField(db_column='Imie', max_length=255)),
                ('nazwisko', models.CharField(db_column='Nazwisko', max_length=255)),
                ('nrindeksu', models.CharField(db_column='NrIndeksu', max_length=9, unique=True)),
                ('kierunekstudiow', models.CharField(db_column='KierunekStudiow', max_length=255)),
                ('specjalnosc', models.CharField(blank=True, db_column='Specjalnosc', max_length=255, null=True)),
                ('rokstudiow', models.IntegerField(db_column='RokStudiow')),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Temat',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('trescpl', models.CharField(db_column='TrescPL', max_length=255)),
                ('tresceng', models.CharField(db_column='TrescENG', max_length=255)),
                ('maxiloscrealizujacych', models.IntegerField(db_column='MaxIloscRealizujacych')),
                ('czyzatwierdzony', models.IntegerField(db_column='CzyZatwierdzony')),
                ('czywolny', models.IntegerField(db_column='CzyWolny')),
                ('czyzaliczona', models.IntegerField(blank=True, db_column='CzyZaliczona', null=True)),
                ('czyplagiat', models.IntegerField(blank=True, db_column='CzyPlagiat', null=True)),
            ],
            options={
                'db_table': 'temat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TypPracy',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('nazwatypu', models.CharField(db_column='nazwaTypu', max_length=255, unique=True)),
            ],
            options={
                'db_table': 'typpracy',
                'managed': False,
            },
        ),
    ]
