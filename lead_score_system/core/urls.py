from django.urls import path
from . import views


app_name='core'

urlpatterns=[
    path('', views.avaliar_lead, name="lead_form" )
]
