# Generated by Django 4.2.6 on 2023-10-31 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joblist', '0002_remove_employer_summary_employer_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employer',
            name='type_job',
            field=models.CharField(choices=[('F', 'Fulltime'), ('P', 'Parttime'), ('I', 'Intership'), ('R', 'Remote')], default='1', max_length=100),
            preserve_default=False,
        ),
    ]