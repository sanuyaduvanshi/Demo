from django.urls import path
from webapp import views
# from .views import *

urlpatterns = (
    path('',views.home,name='home'),
    path('ourbank',views.ourbank,name="ourbank"),
    path('research',views.research,name="research"),
    path('financing',views.financing,name="financing"),
    path('<str:selectedFolder>/',views.lang,name='lang'),
    path('errorpage',views.errorpage,name="errorpage"),

    path('EN/finance',views.enfinance,name='enfinance'),
    path('EN/investment',views.eninvestment,name='eninvestment'),
    path('EN/ourbank',views.enourbank,name='enourbank'),

    path('DE/finance',views.definance,name='definance'),
    path('DE/investment',views.deinvestment,name='deinvestment'),
    path('DE/ourbank',views.deourbank,name='deourbank'),

    path('CZ/finance',views.czfinance,name='czfinance'),
    path('CZ/investment',views.czinvestment,name='czinvestment'),
    path('CZ/ourbank',views.czourbank,name='czourbank'),

    path('ES/finance',views.esfinance,name='esfinance'),
    path('ES/investment',views.esinvestment,name='esinvestment'),
    path('ES/ourbank',views.esourbank,name='esourbank'),

    path('TR/finance',views.trfinance,name='trfinance'),
    path('TR/investment',views.trinvestment,name='trinvestment'),
    path('TR/ourbank',views.trourbank,name='trourbank'),

)