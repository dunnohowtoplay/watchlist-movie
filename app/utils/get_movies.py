from json import JSONDecodeError
import requests

from app.config import settings

class GetMovies:
    def __init__(self) -> None:
        self.api_key = settings.API_KEY

    def get_movie_list(self, page: int = 1):
        url = "https://api.themoviedb.org/3/movie/popular?"
        response = requests.get(
            url=f"{url}api_key={self.api_key}&page={page}"
        )

        try:
            data = response.json()
            list_movies = data.get("results", [])
        except JSONDecodeError:
            list_movies = []
        
        movies_data = []
        for movie in list_movies:
            movies_data.append(
                {
                    "movie_id": movie.get("id", 0),
                    "movie_title": movie.get("original_title", "")            
                }
            )
        
        return movies_data
