from django.db import models
from django.urls import reverse

from django.conf import settings

import datetime


class Sample(models.Model):
    txn_desc = models.CharField(max_length=80)
    txn_amt  = models.DecimalField(max_digits=10, decimal_places=2)
    txn_date = models.DateField()

    def __str__(self):
        return self.txn_desc + ',  ' + self.txn_date.strftime("%Y-%m-%d") + ',  '+ str(self.txn_amt)
    