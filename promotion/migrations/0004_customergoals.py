# Generated by Django 4.1.5 on 2023-01-07 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0003_alter_promotion_end_date_alter_promotion_start_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerGoals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('user_name', models.CharField(max_length=64)),
                ('is_promotion', models.BooleanField(default=False)),
                ('benefitPercentage', models.FloatField(default=0)),
                ('depositedAmount', models.FloatField(default=0)),
                ('plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='promotion.plan')),
                ('promotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='promotion.promotion')),
            ],
        ),
    ]
