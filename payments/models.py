import json

import requests
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from base.models import BaseModel


class PaymentStatus(BaseModel):
    status = models.CharField(max_length=200, verbose_name=_('status'))

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = _('Payment Status')
        verbose_name_plural = _('Payment Statuses')


class Payment(models.Model):
    user = models.ForeignKey(verbose_name=_('user'), to=User, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(verbose_name=_('amount'))
    ref_id = models.CharField(verbose_name=_('ref_id'), max_length=512, blank=True, null=True)
    status = models.ForeignKey(to=PaymentStatus, on_delete=models.CASCADE, verbose_name=_('status'))
    authority = models.CharField(verbose_name=_('authority'), max_length=512, blank=True, null=True)
    link = models.URLField(verbose_name=_('link'), blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('created_date'))

    def __str__(self):
        return f'{self.user} - {self.amount} : {self.status}'

    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payments')
        ordering = ('created_date',)

    def save(self, *args, **kwargs):
        if not self.pk:
            description = 'Core'
            req_data = {
                "merchant_id": settings.MERCHANT,
                "amount": self.amount,
                "callback_url": settings.CALLBACKURL,
                "description": description
            }
            req_header = {"accept": "application/json",
                          "content-type": "application/json'"}
            req = requests.post(url=settings.ZP_API_REQUEST, data=json.dumps(req_data), headers=req_header)
            authority = req.json()['data']['authority']

            if len(req.json()['errors']) == 0:
                self.authority = authority
                self.link = settings.ZP_API_STARTPAY.format(authority=authority)
            else:
                e_code = req.json()['errors']['code']
                e_message = req.json()['errors']['message']
                self.error = f"Error code: {e_code}, Error Message: {e_message}"

        super(Payment, self).save(*args, **kwargs)
