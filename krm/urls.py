from django.urls import path

from . import views


urlpatterns = [
    # /krm/
    path('', views.index, name='index'),
    # /krm/informacije/
    path('informacije/', views.informacije, name='informacije'),
    # /krm/ulazniRacun/
    path('ulazniRacun/', views.ulazniRacun, name='ulazniRacun'),
    # /krm/izlazniRacun/
    path('izlazniRacun/', views.izlazniRacun, name='izlazniRacun'),
    # /krm/inventura/
    path('inventura/', views.inventura, name='inventura'),
    # /krm/racuni/
    path('racuni/', views.racuni, name='racuni'),
    # ex: /krm/racuni/5/racun/
    path('racuni/<int:racun_id>/racun/', views.racun, name='racun'),
    # /krm/objekti/
    path('objekti/', views.objekti, name='objekti'),
    # /krm/stanjeSkladista/
    path('manjakRobe/', views.manjakRobe, name='manjakRobe'),
    # ex: /krm/5/tablica/
    path('<int:materijal_id>/tablica/', views.tablica, name='tablica'),
    # /krm/info/
    path('info/', views.info, name='info'),

    # /krm/ulaz/
    path('ulaz/', views.ulaz, name='ulaz'),
    # /krm/izlaz/
    path('izlaz/', views.izlaz, name='izlaz'),
]