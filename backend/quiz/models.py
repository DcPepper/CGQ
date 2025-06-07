from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_langue(text):
    if "-" not in text or len(text) == 0:
        raise ValidationError(
            _("%(value)s should be a list of languages"),
            params={"text": text},
        )
        
class Geophraphy(models.Model):
    AFRIQUE = "AF"
    AMERIQUEDUNORD = "NA"
    AMERIQUEDUSUD = "SA"
    ANTARCTIQUE = "AN"
    ASIE = "AS"
    EUROPE = "EU"
    CONTINENTS = {
        AFRIQUE: "AFRIQUE",
        AMERIQUEDUNORD: "AMERIQUE DU NORD",
        AMERIQUEDUSUD: "AMERIQUE DU SUD",
        ANTARCTIQUE: "ANTARCTIQUE",
        ASIE: "ASIE",
        EUROPE: "EUROPE",
    }
    
    iso = models.CharField(primary_key=True, max_length=4)
    flag = models.TextField()
    capital = models.CharField(max_length=50)
    shape = models.TextField()
    long = models.CharField(max_length=10)
    lat = models.CharField(max_length=10)
    population = models.IntegerField()
    continent = models.CharField(choices=CONTINENTS)
    langue = models.TextField(validators=[validate_langue])
    
        
    

    

# Create your models here.
