from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.db import connection
from django.db.models import Q
import datetime
import json

from .models import Materijal, Racuni, Krm


app_name = 'krm'

def index(request):
    id = Krm.objects.all().values_list('materijalID', flat=True).distinct()
    all_materijal = Materijal.objects.filter(id__in=id).only("naziv", "sifra")
    context = {'all_materijal': all_materijal}
    return render(request, 'krm/index.html', context)

def tablica(request, materijal_id):
    naziv = Materijal.objects.filter(id=materijal_id).values('naziv')[:1]
    materijal = Krm.objects.filter(materijalID=materijal_id).order_by('racunID__datum', 'id').select_related('materijalID', 'racunID')
    context = {'materijal': materijal, 'naziv': naziv}
    return render(request, 'krm/tablica.html', context)

def informacije(request):
    if request.method == 'GET': 
        materijal_naziv = Materijal.objects.filter(sifra=request.GET['sifra']).values_list('naziv')
        cijena = Materijal.objects.filter(sifra=request.GET['sifra']).values_list('cijena')[0][0]
        response_data = {}  
        try:
            response_data['naziv'] = list(materijal_naziv)
            response_data['cijena'] = str(cijena)
        except: 
            response_data['naziv'] = 'Doslo je do pogreske u bazi'

        return HttpResponse(json.dumps(response_data), content_type="application/json")


def ulaz(request):
    datum = datetime.datetime.strptime(request.POST['datum_racuna'], '%d/%m/%Y').strftime('%Y-%m-%d')
    broj_racuna = request.POST['br_racuna']
    Racuni(firma=request.POST['dobavljac'], ulaz_izlaz='ulaz', broj_racuna=broj_racuna, datum=datum).save()
    #id_racun = Racuni.objects.all().order_by("-id").only("id")[0]
    id_racun = Racuni.objects.values('id').order_by('-id').first()
    str_id = str(id_racun['id'])
    x = int(request.POST['x'])

    for i in range(x):
        sifra = request.POST['sif'+str(i)]
        naziv = request.POST['naz'+str(i)]
        kolicina = request.POST['kol'+str(i)]
        cijena = request.POST['cij'+str(i)]
        cursor = connection.cursor()
        cursor.execute("call procedura_ulaz('"+sifra+"', '"+naziv+"', '"+cijena+"', '"+str_id+"', '"+kolicina+"')")

    return redirect(ulazniRacun)

def izlaz(request):
    datum = datetime.datetime.strptime(request.POST['datum_racuna'], '%d/%m/%Y').strftime('%Y-%m-%d')
    broj_racuna = request.POST['br_racuna']
    Racuni(firma=request.POST['dobavljac'], ulaz_izlaz='izlaz', broj_racuna=broj_racuna, datum=datum).save()
    id_racun = Racuni.objects.values('id').order_by('-id').first()
    str_id = str(id_racun['id'])
    x = int(request.POST['x'])

    for i in range(x):
        sifra = request.POST['sif'+str(i)]
        naziv = request.POST['naz'+str(i)]
        kolicina = request.POST['kol'+str(i)]
        cijena = request.POST['cij'+str(i)]
        cursor = connection.cursor()
        cursor.execute("call procedura_izlaz('"+sifra+"', '"+naziv+"', '"+cijena+"', '"+str_id+"', '"+kolicina+"')")

    return redirect(izlazniRacun)


def ulazniRacun(request):
    if 'term' in request.GET:
        qs = Materijal.objects.filter(sifra__istartswith=request.GET.get('term'))
        sifre = list()
        for materijal in qs:
            sifre.append(materijal.sifra)

        return JsonResponse(sifre, safe=False)
    return render(request, 'krm/ulazniRacun.html')

def izlazniRacun(request):
    if 'term' in request.GET:
        qs = Materijal.objects.filter(sifra__istartswith=request.GET.get('term'))
        sifre = list()
        for materijal in qs:
            sifre.append(materijal.sifra)

        return JsonResponse(sifre, safe=False) #safe=true u slučaju da saljemo dictionary
    return render(request, 'krm/izlazniRacun.html')

def inventura(request):
    all_materijal = Materijal.objects.filter(skladiste_kolicina__gt=0)
    context = {'all_materijal': all_materijal}
    return render(request, 'krm/inventura.html', context)

def racuni(request):
    all_racuni = Racuni.objects.all().order_by('-datum')
    context = {'all_racuni': all_racuni}
    return render(request, 'krm/racuni.html', context)    

def racun(request, racun_id):
    racun = Racuni.objects.filter(id=racun_id)
    all_materijal = Krm.objects.filter(racunID=racun_id).select_related('materijalID')
    context = {'all_materijal': all_materijal, 'racun': racun}
    return render(request, 'krm/racun.html', context)

def objekti(request):
    # all_materijal = Krm.objects.filter(racunID__ulaz_izlaz="ulaz").order_by('-racunID__datum').select_related('materijalID', 'racunID')[:2000]
    all_materijal = Krm.objects.filter(Q(racunID__ulaz_izlaz="ulaz") & Q(materijalID__skladiste_kolicina__gt=0)).order_by('-racunID__datum').select_related('materijalID', 'racunID')[:2000]
    context = {'all_materijal': all_materijal}
    return render(request, 'krm/objekti.html', context)

def manjakRobe(request):
    all_materijal = Materijal.objects.filter(skladiste_kolicina__lt=0)
    context = {'all_materijal': all_materijal}
    return render(request, 'krm/manjakRobe.html', context)

def info(request):
    return render(request, 'krm/info.html')





