from django.db import models

AMOUNT_CHOICES = (
    ('1000', '1000'),
    ('5000', '5000'),
    ('10000', '10000'),
    ('50000', '50000'),
    ('100000', '100000')
)

TENURE_CHOICES = (
    ('6', '6 months'),
    ('12', '1 year'),
    ('18', '1.5 year'),
    ('24', '2 year'),
    ('36', '3 year'),
    ('42', '3.5 year'),
    ('48', '4 year')
)

BENEFIT = (
    ('cashback', 'cashback'),
    ('extraVoucher', 'extraVoucher')
)

VALIDITY_TYPE = (
    ('end_date', 'End Date'),
    ('num_of_users', 'Max Number of Users')
)


class Plan(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    amount = models.CharField(max_length=64, choices=AMOUNT_CHOICES, default="5000")
    tenure = models.CharField(max_length=64, choices=TENURE_CHOICES, default="12")
    benefitPercentage = models.FloatField(default=0)
    benefitType = models.CharField(max_length=64, choices=BENEFIT, default="cashback")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Promotion(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE)
    validity_type = models.CharField(max_length=64, choices=VALIDITY_TYPE, default='end_date')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    users_left = models.IntegerField(null=True, blank=True)
    benefitPercentage = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)

    # WOULD NEED TO CREATE A CRON JOB TO TOGGLE is_active to FALSE ONCE THE END-DATE PASSES BY

    def __str__(self):
        return f'{self.plan.name}-{self.name}'


class CustomerGoal(models.Model):
    # the user and user_name should later be a foreign key to the user object
    user = models.IntegerField()
    user_name = models.CharField(max_length=64)

    plan = models.ForeignKey('Plan', on_delete=models.CASCADE, blank=True, null=True)
    promotion = models.ForeignKey('Promotion', on_delete=models.CASCADE, blank=True, null=True)

    # Here we have made both plan and promotion to be blank and null to true but we will make sure that either one of
    # them is set while creating the object in your view

    is_promotion = models.BooleanField(default=False)
    benefitPercentage = models.FloatField(default=0)
    depositedAmount = models.FloatField(default=0)

    def __str__(self):
        return self.user_name
