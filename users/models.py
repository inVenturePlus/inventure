# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from multiselectfield import MultiSelectField

from django.db import models

STATES = ((1,"AL"), (2,"AK"), (3,"AZ"), (4,"AR"), (5,"CA"), (6,"CO"), (7,"CT"), (8,"DC"), (9,"DE"), (10,"FL"), (11,"GA"), (12,"HI"), (13,"ID"), (14,"IL"), (15,"IN"), (16,"IA"), (17,"KS"), (18,"KY"), (19,"LA"), (20,"ME"), (21,"MD"), (22,"MA"), (23,"MI"), (24,"MN"), (25,"MS"), (26,"MO"), (27,"MT"), (28,"NE"), (29,"NV"), (30,"NH"), (31,"NJ"), (32,"NM"), (33,"NY"), (34,"NC"), (35,"ND"), (36,"OH"), (37,"OK"), (38,"OR"), (39,"PA"), (40,"RI"), (41,"SC"), (42,"SD"), (43,"TN"), (44,"TX"), (45,"UT"), (46,"VT"), (47,"VA"), (48,"WA"), (49,"WV"), (50,"WI"), (51,"WY"))

STAGES = ((1, "Pre-Seed"), (2, "Seed"), (3, "Series A"), (4, "Series B"), (5, "Series C/Growth"))

CHECK_SIZE = ((1, "$0-250k"), (2, "$250k-500k"), (3, "$500k-1m"), (4, "$1m-3m"), (5, "$3m-5m"), (6, "$5m-10m"), (7, "$10m+"))

SECTORS = ((1, "AI/ML/Cloud"), (2, "Cryptocurrency/Blockchaim"), (3, "Technology"), (4, "Pharmacy"), (5, "Market Places"), (6, "Real Estate"), (7, "Robotics/Drones"), (8, "Security"), (9, "Infrastructure/Transportation"), (10, "E-Commerce"), (11, "Human Resources"), (12, "Consumers"), (13, "Entertainment"), (14, "Mobile"), (15, "Data Analytics"), (16, "Developer Tools"), (17, "Marketing"), (18, "Enterprises"), (19, "Wearables"))

class VentureCapital(models.Model):
    company_name = models.CharField(max_length=150, default="")
    company_state = models.IntegerField(null=True, default=1)

    company_city = models.CharField(max_length=120, default="")

    company_mission = models.TextField(verbose_name="Mission statement of the company.", blank=True)
    company_fund_size = models.IntegerField(null=True, default=1)

    stages_interested = MultiSelectField(choices=STAGES)
    stages_avoid = MultiSelectField(choices=STAGES)

    locations_interested = MultiSelectField(choices=STATES)
    locations_avoid = MultiSelectField(choices=STATES)

    sectors_interested = MultiSelectField(choices=SECTORS)
    sectors_avoid = MultiSelectField(choices=SECTORS)

    check_size = models.IntegerField(null=True, default=1)

    previous_investments = models.TextField(verbose_name="Previous investments.", blank=True)


class Entrepreneur(models.Model):
    company_name = models.CharField(max_length=150, default="")
    company_state = models.IntegerField(null=True)

    company_city = models.CharField(max_length=150, default="")

    company_mission = models.TextField(verbose_name="Company's mission statement", blank=True)
    current_stage = models.IntegerField(null=True, default=1)

    locations_interested = MultiSelectField(choices=STATES)
    check_size = models.IntegerField(null=True, default=1)
    sector = models.IntegerField(null=True, default=1)
    other = models.TextField(verbose_name="Previous investors, etc.", blank=True)

    def makeMatch(self):
        # match = Matches()
        # match.entrepreneur = self.pk
        for v in VentureCapital:
            match = Matches()
            match.entrepreneur = self.pk
            match.venturecapital = v.pk
            match.match_score = generateScore(self.pk, v.pk)
            match.save()


class Matches(models.Model):
    entrepreneur = models.OneToOneField(Entrepreneur, on_delete=models.CASCADE, primary_key=False)
    venturecapital = models.OneToOneField(VentureCapital, on_delete=models.CASCADE, primary_key=False)

    match_score = models.IntegerField(null=False)

    class Meta:
       unique_together = (("entrepreneur", "venturecapital"))

    def __str__(self):
       return self.entrepreneur + ", " + self.venturecapital
