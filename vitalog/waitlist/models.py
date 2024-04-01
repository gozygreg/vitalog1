from django.db import models

class WaitlistUser(models.Model):
    HEALTH_CHALLENGES = [
        ('Mental Health/Depression', 'Mental Health/Depression'),
        ('Cardiovascular/Heart Disease', 'Cardiovascular/Heart Disease'),
        ('Cancer', 'Cancer'),
        ('Loneliness', 'Loneliness'),
        ("Women's Health", "Women's Health"),
        ('Palliative Care and End of Life Care', 'Palliative Care and End of Life Care'),
    ]

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=100)
    health_challenge = models.CharField(max_length=100, choices=HEALTH_CHALLENGES)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
