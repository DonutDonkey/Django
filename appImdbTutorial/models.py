from django.db import models

# Create your models here.
class AdditionalInfo(models.Model) :
    duration_time = models.PositiveSmallIntegerField(default=0)

    __GENRE = {
        (0, 'Else'),
        (1, 'Horror'),
        (2, 'Comedy'),
        (3, 'Sci-fi'),
        (4, 'Drama')
    }
    genre = models.PositiveSmallIntegerField(default=0, choices=__GENRE)

    # def __str__(self) -> str :
    #     return 

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

    additional_info = models.OneToOneField(AdditionalInfo, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str :
        return self.title_with_year()
        #return self.title + '(' + str(self.year) + ')'

    def title_with_year(self) :
        return "{} ({})".format(self.title, self.year)
        # return f'{self.title}({str(self.year)})'

class Rating(models.Model) :
    review = models.TextField(default='', blank=True)
    stars = models.SmallIntegerField(default=5)

    film = models.ForeignKey(Film, on_delete=models.CASCADE)

class Actor(models.Model) :
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    movies = models.ManyToManyField(Film, related_name='actors')

    def __str__(self) -> str:
        return "{} {}".format(self.first_name, self.last_name)