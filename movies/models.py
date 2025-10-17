from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Movie(models.Model):
    GENRE_CHOICES = [
        ('Comedy', 'Comedy'),
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Romance', 'Romance'),
        ('Documentary', 'Documentary'),
        ('Other', 'Other'),
    ]

    MovieID = models.CharField("Movie ID", max_length=20, primary_key=True)

    MovieTitle = models.CharField("Title", max_length=200)
    Actor1Name = models.CharField("Lead Actor", max_length=100)
    Actor2Name = models.CharField("Second Actor", max_length=100, blank=True)
    DirectorName = models.CharField("Director", max_length=100)
    MovieGenre = models.CharField("Genre", max_length=15, choices=GENRE_CHOICES)

    ReleaseYear = models.PositiveIntegerField(
        "Release Year",
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.date.today().year)
        ]
    )

    class Meta:
        ordering = ['-ReleaseYear', 'MovieTitle']

    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"
