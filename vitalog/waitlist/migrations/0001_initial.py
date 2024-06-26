# Generated by Django 5.0.3 on 2024-04-01 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaitlistUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('health_challenge', models.CharField(choices=[('Mental Health/Depression', 'Mental Health/Depression'), ('Cardiovascular/Heart Disease', 'Cardiovascular/Heart Disease'), ('Cancer', 'Cancer'), ('Loneliness', 'Loneliness'), ("Women's Health", "Women's Health"), ('Palliative Care and End of Life Care', 'Palliative Care and End of Life Care')], max_length=100)),
                ('note', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
