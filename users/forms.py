from django import forms
from django.forms import ModelForm
from users.models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import SetPasswordForm

class VentureCapitalForm(ModelForm):

    class Meta:
        model = VentureCapital
        fields = "__all__"

    def __init__(self, data=None, *args, **kwargs):
        super(VentureCapitalForm, self).__init__(data, *args, **kwargs)

        STATES = ((1,"AL"), (2,"AK"), (3,"AZ"), (4,"AR"), (5,"CA"), (6,"CO"), (7,"CT"), (8,"DC"), (9,"DE"), (10,"FL"), (11,"GA"), (12,"HI"), (13,"ID"), (14,"IL"), (15,"IN"), (16,"IA"), (17,"KS"), (18,"KY"), (19,"LA"), (20,"ME"), (21,"MD"), (22,"MA"), (23,"MI"), (24,"MN"), (25,"MS"), (26,"MO"), (27,"MT"), (28,"NE"), (29,"NV"), (30,"NH"), (31,"NJ"), (32,"NM"), (33,"NY"), (34,"NC"), (35,"ND"), (36,"OH"), (37,"OK"), (38,"OR"), (39,"PA"), (40,"RI"), (41,"SC"), (42,"SD"), (43,"TN"), (44,"TX"), (45,"UT"), (46,"VT"), (47,"VA"), (48,"WA"), (49,"WV"), (50,"WI"), (51,"WY"))

        STAGES = ((1, "Pre-Seed"), (2, "Seed"), (3, "Series A"), (4, "Series B"), (5, "Series C/Growth"))

        CHECK_SIZE = ((1, "$0-250k"), (2, "$250k-500k"), (3, "$500k-1m"), (4, "$1m-3m"), (5, "$3m-5m"), (6, "$5m-10m"), (7, "$10m+"))

        SECTORS = ((1, "AI/ML/Cloud"), (2, "Cryptocurrency/Blockchaim"), (3, "Technology"), (4, "Pharmacy"), (5, "Market Places"), (6, "Real Estate"), (7, "Robotics/Drones"), (8, "Security"), (9, "Infrastructure/Transportation"), (10, "E-Commerce"), (11, "Human Resources"), (12, "Consumers"), (13, "Entertainment"), (14, "Mobile"), (15, "Data Analytics"), (16, "Developer Tools"), (17, "Marketing"), (18, "Enterprises"), (19, "Wearables"))

        self.fields['company_name'] = forms.CharField(max_length=150)
        self.fields['company_city'] = forms.CharField(max_length=150)

        self.fields['company_state'] = forms.ChoiceField(choices=STATES)

        self.fields['sectors_avoid'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SECTORS)
        self.fields['sectors_interested'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=SECTORS)

        self.fields['company_mission'] = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows':1,'cols':10}))

        self.fields['check_size'] = forms.ChoiceField(choices=CHECK_SIZE)


        self.fields['previous_investments'] = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows':1,'cols':10}))

        #determine which fields to not make required.

class EntrepreneurForm(ModelForm):

    class Meta:
        model = Entrepreneur
        fields = "__all__"

    def __init__(self, data=None, *args, **kwargs):
        super(EntrepreneurForm, self).__init__(data, *args, **kwargs)

        STATES = ((1,"AL"), (2,"AK"), (3,"AZ"), (4,"AR"), (5,"CA"), (6,"CO"), (7,"CT"), (8,"DC"), (9,"DE"), (10,"FL"), (11,"GA"), (12,"HI"), (13,"ID"), (14,"IL"), (15,"IN"), (16,"IA"), (17,"KS"), (18,"KY"), (19,"LA"), (20,"ME"), (21,"MD"), (22,"MA"), (23,"MI"), (24,"MN"), (25,"MS"), (26,"MO"), (27,"MT"), (28,"NE"), (29,"NV"), (30,"NH"), (31,"NJ"), (32,"NM"), (33,"NY"), (34,"NC"), (35,"ND"), (36,"OH"), (37,"OK"), (38,"OR"), (39,"PA"), (40,"RI"), (41,"SC"), (42,"SD"), (43,"TN"), (44,"TX"), (45,"UT"), (46,"VT"), (47,"VA"), (48,"WA"), (49,"WV"), (50,"WI"), (51,"WY"))

        STAGES = ((1, "Pre-Seed"), (2, "Seed"), (3, "Series A"), (4, "Series B"), (5, "Series C/Growth"))

        CHECK_SIZE = ((1, "$0-250k"), (2, "$250k-500k"), (3, "$500k-1m"), (4, "$1m-3m"), (5, "$3m-5m"), (6, "$5m-10m"), (7, "$10m+"))

        SECTORS = ((1, "AI/ML/Cloud"), (2, "Cryptocurrency/Blockchaim"), (3, "Technology"), (4, "Pharmacy"), (5, "Market Places"), (6, "Real Estate"), (7, "Robotics/Drones"), (8, "Security"), (9, "Infrastructure/Transportation"), (10, "E-Commerce"), (11, "Human Resources"), (12, "Consumers"), (13, "Entertainment"), (14, "Mobile"), (15, "Data Analytics"), (16, "Developer Tools"), (17, "Marketing"), (18, "Enterprises"), (19, "Wearables"))

        self.fields['company_name'] = forms.CharField(max_length=150)
        self.fields['company_city'] = forms.CharField(max_length=150)

        self.fields['company_state'] = forms.ChoiceField(choices=STATES)
        self.fields['current_stage'] = forms.ChoiceField(choices=STAGES)

        self.fields['company_mission'] = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows':1,'cols':10}))


        self.fields['check_size'] = forms.ChoiceField(choices=CHECK_SIZE)
        self.fields['sector'] = forms.ChoiceField(choices=SECTORS)

        self.fields['locations_interested'] = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=STATES)

        self.fields['other'] = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','rows':1,'cols':10}))
