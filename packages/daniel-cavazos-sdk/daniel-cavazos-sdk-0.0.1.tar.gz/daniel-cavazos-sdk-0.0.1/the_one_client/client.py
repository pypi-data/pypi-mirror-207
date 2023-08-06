class TheOneClient(SDKBuilder):
    """
    A client for The One API that extends the SDKBuilder class.

    This class defines methods that interact with The One API to retrieve information
    about movies and quotes from the Lord of the Rings trilogy.

    Example usage:
    --------------
    # create an instance of the TheOneClient with a valid API token
    client = TheOneClient("my-api-token")

    # retrieve a list of all movies from The One API
    all_movies = client.get_movies()

    # retrieve a specific movie from The One API by ID
    the_fellowship_of_the_ring = client.get_movie(id="5cd95395de30eff6ebccde56")

    # retrieve all quotes for a specific movie by ID
    quotes = client.get_movie_quotes(id="5cd95395de30eff6ebccde56")

    # retrieve a specific quote by ID
    one_ring_quote = client.get_quote(id="5cd96e05de30eff6ebccebce")
    """

    host = "https://the-one-api.dev/v2"
    get_movies = SDKBuilder.GET("/movie")
    get_movie = SDKBuilder.GET("/movie/{id}")
    get_movie_quotes = SDKBuilder.GET(


client = TheOneClient(token="eUHAQDqjMHmj4rLHN8eF")
movies = client.get_movies()
print(movies)
movie = client.get_movie(id="5cd95395de30eff6ebccde56")
print(movie)
movie_quotes = client.get_movie_quotes(id="5cd95395de30eff6ebccde56")
print(movie_quotes)
quotes = client.get_quotes()
print(quotes)
quote = client.get_quote(id="5cd96e05de30eff6ebccebce")