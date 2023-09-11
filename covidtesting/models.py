from django.db import models

# Create your models here.
class CovidDetails(models.Model):
# Breathing Problem,Fever,Dry Cough,Sore throat,Running Nose,Asthma,Chronic Lung Disease,Headache,

# Heart Disease,Diabetes,Hyper Tension,Fatigue,Gastrointestinal,Abroad travel,Contact with COVID Patient,

# Attended Large Gathering,Visited Public Exposed Places,Family working in Public Exposed Places,Wearing Masks,

# Sanitization from Market,COVID-19

    breathing_problem = models.BooleanField(null=False)
    fever = models.BooleanField(null=False)
    dry_cough = models.BooleanField(null=False)
    sore_throat = models.BooleanField(null=False)
    running_nose = models.BooleanField(null=False)
    asthma = models.BooleanField(null=False)
    chronic_lung_disease = models.BooleanField(null=False)
    headache = models.BooleanField(null=False)
    heart_disease = models.BooleanField(null=False)
    diabetes = models.BooleanField(null=False)
    hyper_tension = models.BooleanField(null=False)
    fatigue = models.BooleanField(null=False)
    gastrointestinal = models.BooleanField(null=False)
    abroad_travel = models.BooleanField(null=False)
    contact_with_covid_patient = models.BooleanField(null=False)
    attended_large_gathering = models.BooleanField(null=False)
    visited_public_exposed_places = models.BooleanField(null=False)
    family_working_in_public_exposed_places = models.BooleanField(null=False)
    wearing_masks = models.BooleanField(null=False)
    sanitization_from_market = models.BooleanField(null=False)
    covid_19 = models.BooleanField(null=False)