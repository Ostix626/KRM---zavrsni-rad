from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Materijal(models.Model):
    naziv = models.CharField(max_length=300)
    sifra = models.CharField(max_length=50)
    mjerna_jedinica = models.CharField(max_length=10)
    skladiste_kolicina = models.DecimalField(default=0, decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.00'))])
    cijena = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    vrijednost = models.DecimalField(default=0, decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.00'))])

    class Meta:
        db_table = "Materijal"

    def __str__(self):
        return self.sifra

class Racuni(models.Model):
    firma = models.CharField(max_length=150)
    ulaz_izlaz = models.CharField(max_length=10)
    broj_racuna = models.CharField(max_length=50)
    datum = models.DateField()

    class Meta:
        db_table = "Racuni"


class Krm(models.Model):
    materijalID = models.ForeignKey(Materijal, on_delete=models.CASCADE, db_column='materijalID')
    racunID = models.ForeignKey(Racuni, on_delete=models.CASCADE, db_column='racunID')
    kolicina = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])
    datum_kolicina_skladiste = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.00'))])
    vrijednost = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])

    class Meta:
        db_table = "Krm"