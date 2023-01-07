# Generated by Django 4.1.5 on 2023-01-07 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('validity_type', models.CharField(choices=[('end_date', 'End Date'), ('num_of_users', 'Max Number of Users')], default='end_date', max_length=64)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('users_left', models.IntegerField()),
                ('benefitPercentage', models.FloatField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promotion.plan')),
            ],
        ),
    ]
