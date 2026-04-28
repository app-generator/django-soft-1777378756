# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Requesttype(models.Model):

    #__Requesttype_FIELDS__
    request_type_name = models.CharField(max_length=255, null=True, blank=True)

    #__Requesttype_FIELDS__END

    class Meta:
        verbose_name        = _("Requesttype")
        verbose_name_plural = _("Requesttype")


class Ticketstatus(models.Model):

    #__Ticketstatus_FIELDS__
    satus_id = models.IntegerField(null=True, blank=True)
    status_sequence = models.IntegerField(null=True, blank=True)
    status_name = models.CharField(max_length=255, null=True, blank=True)

    #__Ticketstatus_FIELDS__END

    class Meta:
        verbose_name        = _("Ticketstatus")
        verbose_name_plural = _("Ticketstatus")


class Ticket(models.Model):

    #__Ticket_FIELDS__
    affected_email = models.CharField(max_length=255, null=True, blank=True)
    date_created = models.DateTimeField(blank=True, null=True, default=timezone.now)
    date_updated = models.DateTimeField(blank=True, null=True, default=timezone.now)
    user_updated = models.ForeignKey(TicketStatus, on_delete=models.CASCADE)
    user_assigned = models.ForeignKey(RequestType, on_delete=models.CASCADE)
    request_type = models.ForeignKey(RequestType, on_delete=models.CASCADE)
    current_status = models.ForeignKey(TicketStatus, on_delete=models.CASCADE)

    #__Ticket_FIELDS__END

    class Meta:
        verbose_name        = _("Ticket")
        verbose_name_plural = _("Ticket")



#__MODELS__END
