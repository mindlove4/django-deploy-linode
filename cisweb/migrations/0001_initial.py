# Generated by Django 4.0.4 on 2022-05-01 16:57

import cisweb.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address_Student',
            fields=[
                ('address_stu_id', models.AutoField(primary_key=True, serialize=False)),
                ('house_number', models.CharField(max_length=255)),
                ('village_name', models.CharField(blank=True, max_length=255, null=True)),
                ('soi', models.CharField(blank=True, max_length=255, null=True)),
                ('road', models.CharField(max_length=255)),
                ('subdistrict', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('postcode', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(9999)])),
            ],
        ),
        migrations.CreateModel(
            name='Train_Contact',
            fields=[
                ('train_contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('institute_number', models.CharField(max_length=255)),
                ('institute_name', models.CharField(max_length=255)),
                ('soi', models.CharField(blank=True, max_length=255, null=True)),
                ('road', models.CharField(blank=True, max_length=255, null=True)),
                ('subdistrict', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('province', models.CharField(max_length=255)),
                ('postcode', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
                ('institute_tel', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(regex='^\\d{9,15}$'), django.core.validators.MinLengthValidator(9)])),
                ('institute_email', models.EmailField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('teacher_prefix', models.CharField(max_length=10)),
                ('teacher_firstname', models.CharField(max_length=255)),
                ('teacher_lastname', models.CharField(max_length=255)),
                ('id_card', models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(13)])),
                ('role', models.CharField(max_length=255)),
                ('status', models.BooleanField()),
                ('teacher_tel', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\d{9,15}$'), django.core.validators.MinLengthValidator(9)])),
                ('teacher_email', models.EmailField(max_length=255)),
                ('teacher_img', models.ImageField(blank=True, null=True, upload_to=cisweb.models.filepath)),
                ('certificate', models.ImageField(blank=True, null=True, upload_to=cisweb.models.filepath)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('student_prefix', models.CharField(max_length=10)),
                ('student_firstname', models.CharField(max_length=255)),
                ('student_lastname', models.CharField(max_length=255)),
                ('student_img', models.ImageField(blank=True, null=True, upload_to=cisweb.models.filepath)),
                ('date_of_birth', models.DateField()),
                ('id_card', models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(13)])),
                ('campus', models.CharField(max_length=255)),
                ('education_level', models.CharField(max_length=255)),
                ('study_year', models.CharField(max_length=2)),
                ('faculty', models.CharField(max_length=255)),
                ('major', models.CharField(max_length=255)),
                ('gpax', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('student_tel', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(regex='^\\d{9,15}$'), django.core.validators.MinLengthValidator(9)])),
                ('student_email', models.EmailField(max_length=255)),
                ('address_stu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cisweb.address_student')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cisweb.teacher')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Coop_Train',
            fields=[
                ('coop_train_id', models.AutoField(primary_key=True, serialize=False)),
                ('intstitute_name', models.CharField(max_length=255)),
                ('curriculum', models.CharField(blank=True, max_length=255, null=True)),
                ('datetime_event', models.CharField(blank=True, max_length=255, null=True)),
                ('start_apply', models.DateField(blank=True, null=True)),
                ('deadline_apply', models.DateField(blank=True, null=True)),
                ('amount', models.CharField(blank=True, max_length=255, null=True)),
                ('location', models.CharField(max_length=255)),
                ('cost', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
                ('link_detail', models.CharField(blank=True, max_length=255, null=True)),
                ('train_contact_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cisweb.train_contact')),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('agenda_id', models.AutoField(primary_key=True, serialize=False)),
                ('curriculum', models.CharField(max_length=255)),
                ('agenda_link', models.CharField(max_length=255)),
                ('coop_train_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cisweb.coop_train')),
            ],
        ),
    ]
