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
    
    name = models.CharField(max_length=50)
    iso = models.CharField(primary_key=True, max_length=4)
    capital = models.CharField(max_length=50)
    flag = models.TextField()
    shape = models.TextField()
    long = models.FloatField()
    lat = models.FloatField()
    population = models.IntegerField()
    area = models.IntegerField()
    continent = models.CharField(choices=CONTINENTS, default=EUROPE)
    langue = models.TextField(validators=[validate_langue])
    
    @classmethod
    def get_main_fields(cls):
        return [
            'flag',
            'name',
            'shape',
            'capital'
        ]
        
    @classmethod
    def get_filter_fields(cls):
        return [
            "population",
            "continent",
            "area"
        ]
    
    @classmethod
    def get_other_quiz(cls):
        return [
            ("name", "population"),
            ("name", "langue"),
            ("name", "area")
        ]
    

class Japanese(models.Model):
    RATING = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
    }
    fr = models.TextField()
    furigana = models.TextField()
    kanji = models.TextField()
    kunyomi = models.TextField()
    onyomi = models.TextField()
    difficulty = models.IntegerField(choices=RATING, default=1)
    category = models.CharField(max_length=50)

    @classmethod
    def get_main_fields(cls):
        return [
            "fr",
            "hiragana",
            "katakana",
            "kanji",
            "romaji"
        ]
        
    @classmethod
    def get_filter_fields(cls):
        return [
            "difficulty",
            "category",
        ]
    
    @classmethod
    def get_other_quiz(cls):
        return []
    
    # Create your models here.
