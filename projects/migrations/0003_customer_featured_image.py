# Generated by Django 3.2.7 on 2021-09-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_accounts_checking_checking_deposits_checking_withdrawals_loans_savings_savings_deposits_savings_with'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='featured_image',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]