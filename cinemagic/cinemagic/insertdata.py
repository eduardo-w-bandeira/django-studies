from django.core.management.base import BaseCommand
from master.models import Movie


class Command(BaseCommand):
    help = 'Populate Movie table with sample data'

    def handle(self, *args, **kwargs):
        # Sample movie data
        movie_data = [
            {"title": "The Matrix", "duration": 136,
                "genre": "Action", "year": 1999},
            {"title": "Inception", "duration": 148,
                "genre": "Sci-Fi", "year": 2010},
            {"title": "The Shawshank Redemption",
                "duration": 142, "genre": "Drama", "year": 1994},
            {"title": "Pulp Fiction", "duration": 154,
                "genre": "Crime", "year": 1994},
            {"title": "The Dark Knight", "duration": 152,
                "genre": "Action", "year": 2008},
            {"title": "Forrest Gump", "duration": 142,
                "genre": "Drama", "year": 1994},
            {"title": "The Godfather", "duration": 175,
                "genre": "Crime", "year": 1972},
            {"title": "Fight Club", "duration": 139,
                "genre": "Drama", "year": 1999},
            {"title": "Interstellar", "duration": 169,
                "genre": "Sci-Fi", "year": 2014},
            {"title": "The Lord of the Rings: The Return of the King",
                "duration": 201, "genre": "Fantasy", "year": 2003},
        ]

        # Create Movie objects
        for data in movie_data:
            movie = Movie.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(
                f'Successfully created movie "{movie.title}"'))
