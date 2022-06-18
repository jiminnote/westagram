
# Generated by Django 4.0.5 on 2022-06-17 16:29

from django.db import migrations, models




class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('first_name', models.CharField(default=None, max_length=50, null=True, validators=[validation.validate_name])),
                ('last_name', models.CharField(default=None, max_length=50, null=True, validators=[validation.validate_name])),
                ('nick_name', models.CharField(default=None, max_length=50, null=True, unique=True)),
                ('password', models.CharField(default=None, max_length=25, null=True, validators=[validation.validate_password])),
                ('email', models.EmailField(default=None, max_length=25, null=True, unique=True, validators=[validation.validate_email])),
                ('phone_number', models.CharField(default=None, max_length=20, null=True, validators=[validation.validate_phone_number])),

            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
