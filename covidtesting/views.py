from django.shortcuts import render, redirect
from .models import CovidDetails
import tensorflow as tf
from django.db.models import Count
import json

# Create your views here.
def home_page(request):
    return render(request, "home.html", {})

def details_page(request):
    return render(request, "details_page.html", {})

def about(request):
    return render(request, "about.html", {})


def validate_details(request):
    if request.method == 'POST':
        covid_details = CovidDetails()
        covid_details.breathing_problem = request.POST.get("breathing_problem")
        covid_details.fever = request.POST.get("fever")
        covid_details.dry_cough = request.POST.get("dry_cough")
        covid_details.sore_throat = request.POST.get("sore_throat")
        covid_details.running_nose = request.POST.get("running_nose")
        covid_details.asthma = request.POST.get("asthma")
        covid_details.chronic_lung_disease = request.POST.get("chronic_lung_disease")
        covid_details.headache = request.POST.get("headache")
        covid_details.heart_disease = request.POST.get("heart_disease")
        covid_details.diabetes = request.POST.get("diabetes")
        covid_details.hyper_tension = request.POST.get("hyper_tension")
        covid_details.fatigue = request.POST.get("fatigue")
        covid_details.gastrointestinal = request.POST.get("gastrointestinal")
        covid_details.abroad_travel = request.POST.get("abroad_travel")
        covid_details.contact_with_covid_patient = request.POST.get("contact_with_covid_patient")
        covid_details.attended_large_gathering = request.POST.get("attended_large_gathering")
        covid_details.visited_public_exposed_places = request.POST.get("visited_public_exposed_places")
        covid_details.family_working_in_public_exposed_places = request.POST.get("family_working_in_public_exposed_places")
        covid_details.wearing_masks = request.POST.get("wearing_masks")
        covid_details.sanitization_from_market = request.POST.get("sanitization_from_market")
        covid_details.latitude = request.POST.get("latitude", "None")
        covid_details.longitude = request.POST.get("longitude", "None")
        covid_details.area_name = request.POST.get("area_name", "None")
        
        symptoms = [
            request.POST.get('breathing_problem'),
            request.POST.get('fever'),
            request.POST.get('dry_cough'),
            request.POST.get('sore_throat'),
            request.POST.get('running_nose')
        ]
        conditions = [
            request.POST.get('asthma'),
            request.POST.get('chronic_lung_disease'),
            request.POST.get('heart_disease'),
            request.POST.get('diabetes'),
            request.POST.get('hyper_tension')
        ]
        factors = [
            request.POST.get('fatigue'),
            request.POST.get('gastrointestinal'),
            request.POST.get('abroad_travel'),
            request.POST.get('contact_with_covid_patient'),
            request.POST.get('attended_large_gathering'),
            request.POST.get('visited_public_exposed_places'),
            request.POST.get('family_working_in_public_exposed_places'),
            request.POST.get('wearing_masks'),
            request.POST.get('sanitization_from_market')
        ]
        
        old_input_data = symptoms + conditions + factors
        new_input_data = []        

        for i in old_input_data:
            if i == "True":
                new_input_data.append(1.0)
            elif i == "False":
                new_input_data.append(0.0)

        loaded_model = tf.keras.models.load_model('my_model_lstm')
        old_prediction = loaded_model.predict([new_input_data])[0]
        prediction = str(old_prediction)[1:-1]
        prediction = float(prediction) * 100
        prediction = str(prediction)[0:5]
        if float(prediction) > 50.00:
            covid_details.covid_19 = True

        elif float(prediction) < 50.00:
            covid_details.covid_19 = False

        covid_details.save()
        return render(request, "results_page.html", {'prediction': prediction, "result": covid_details.covid_19})
    else:
        return redirect('/covid/home')
    
def graph(request):

    covid_patients_count = CovidDetails.objects.filter(covid_19 = True)
    non_covid_patients_count = CovidDetails.objects.filter(covid_19 = False)
    return render(request, "graph.html", { "covid_patients_count": covid_patients_count,
                                           "non_covid_patients_count": non_covid_patients_count})

def location_bar_chart(request):
    area_counts = CovidDetails.objects.filter(covid_19=True).values('area_name').annotate(count=Count('id')).order_by('area_name')

    area_dict = {item['area_name']: item['count'] for item in area_counts}

    return render(request, "location_bar.html", {
        "area_dict": json.dumps(area_dict)
    })