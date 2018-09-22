# Generated by Django 2.1.1 on 2018-09-22 19:49

from django.db import migrations, models
import django.db.models.deletion
import wfb.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('label', models.CharField(help_text='label to be assigned to each help location', max_length=300, primary_key=True, serialize=False, verbose_name='Label of the category')),
            ],
        ),
        migrations.CreateModel(
            name='HelpLocationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the help location', max_length=200, verbose_name='Name of the help location')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='latitude')),
                ('lon', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='longtitude')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.TextField(blank=True, help_text='Address of this help location', null=True)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[wfb.models.validate_email], verbose_name='email address')),
                ('description', models.TextField(blank=True, help_text='more detail of this help location', verbose_name='Description of this help location')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='locations', to='wfb.CategoryModel')),
            ],
        ),
    ]
