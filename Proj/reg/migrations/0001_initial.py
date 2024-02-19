# Generated by Django 5.0.1 on 2024-01-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.CharField(max_length=20)),
                ('firstname', models.CharField(max_length=20)),
                ('middlename', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('suffix', models.CharField(max_length=8)),
                ('gender', models.CharField(max_length=10)),
                ('birthofdate', models.CharField(max_length=45)),
                ('birthofplace', models.CharField(max_length=45)),
                ('religion', models.CharField(max_length=45)),
                ('citizenship', models.CharField(max_length=45)),
                ('contactno', models.CharField(max_length=20)),
                ('DateRegistered', models.CharField(max_length=255)),
                ('presentAddress', models.CharField(max_length=50)),
                ('homeAddress', models.CharField(max_length=50)),
                ('motherFirstname', models.CharField(max_length=20)),
                ('motherMiddlename', models.CharField(max_length=20)),
                ('motherLastname', models.CharField(max_length=20)),
                ('motherOccupation', models.CharField(max_length=50)),
                ('motherContact', models.CharField(max_length=20)),
                ('fatherFirstname', models.CharField(max_length=20)),
                ('fatherMiddlename', models.CharField(max_length=20)),
                ('fatherLastname', models.CharField(max_length=20)),
                ('fatherOccupation', models.CharField(max_length=50)),
                ('fatherContactno', models.CharField(max_length=15)),
                ('GuardianName', models.CharField(max_length=50)),
                ('GuardianOccupation', models.CharField(max_length=50)),
                ('GuardianAddress', models.CharField(max_length=50)),
                ('GuardianContactno', models.CharField(max_length=20)),
                ('SpouseName', models.CharField(max_length=50)),
                ('SpouseOccupation', models.CharField(max_length=50)),
                ('SpouseAddress', models.CharField(max_length=50)),
                ('JHSLastAttended', models.CharField(max_length=10)),
                ('JHSdateLastAttended', models.DateField()),
                ('SHSLastAttended', models.CharField(max_length=60)),
                ('SHSDateLastAttended', models.DateField()),
                ('CollegiateLastAttended', models.CharField(max_length=50)),
                ('CollegiateDateLastAttended', models.DateField()),
                ('Clearance', models.CharField(max_length=10)),
                ('Sid', models.CharField(max_length=10)),
                ('psa', models.CharField(max_length=10)),
                ('Form148', models.CharField(max_length=10)),
                ('Form137', models.CharField(max_length=10)),
                ('GoodMoral', models.CharField(max_length=10)),
                ('Credential', models.CharField(max_length=10)),
                ('Picture', models.CharField(max_length=10)),
                ('Envelop', models.CharField(max_length=10)),
                ('refno', models.CharField(max_length=8)),
                ('studentStatus', models.CharField(max_length=10)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('password', models.CharField(default='', max_length=15)),
            ],
        ),
    ]
