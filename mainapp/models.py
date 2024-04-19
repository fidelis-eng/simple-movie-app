from django.db import models

class Genre(models.Model):
    genre_name = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.genre_name
    
class Movie(models.Model):

    MPAARATING_CHOICES = (
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('R', 'R'),
        ('NC-17', 'NC-17'),
    )

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    img_path = models.CharField(max_length=50)
    duration = models.IntegerField(default=0)
    language = models.CharField(max_length=50)
    mpaa_rating_type = models.CharField(max_length=10, choices=MPAARATING_CHOICES)
    mpaa_rating_label = models.CharField(max_length=50)
    user_rating = models.FloatField(default=0.0)
    genres = models.ManyToManyField(Genre, through='MovieGenre')

    def __str__(self):
        return self.name

class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.name} - {self.genre.genre_name}"



