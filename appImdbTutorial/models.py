from django.db import models

# Create your models here.
class Film(models.Model) :
    # Null : Bool : 
    # If the value can be null without assigning anything to
    
    # Blank : Bool : 
    # If the value can be null without assigning anything to

    #Choices : iterables of exactly two items (e.g. foo = [(A, B), (A, B) ...])
    # Use as choices for this field

    #default : 
    # The default value for the field

    # unique : bool
    # Make field unique 
    title = models.CharField(max_length=64, blank=False, unique=True) #Text
    year = models.PositiveSmallIntegerField(default=2000)

    # Charfield : 
    # For limited text

    #TextField :
    # for unlimited text
    description = models.TextField(default='')

    release = models.DateField(null=True, blank=True)

    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)

    poster = models.ImageField(upload_to='posters', null=True, blank=True)

    def __str__(self) -> str:
        return self.title_with_year()
        #return self.title + '(' + str(self.year) + ')'

    def title_with_year(self) :
        return "{} ({})".format(self.title, self.year)
        # return f'{self.title}({str(self.year)})'
