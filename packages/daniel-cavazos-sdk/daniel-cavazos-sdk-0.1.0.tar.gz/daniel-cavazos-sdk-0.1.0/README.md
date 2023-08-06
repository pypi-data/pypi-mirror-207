# Daniel Cavazos SDK

The `daniel-cavazos-sdk` package provides a Python client library for interacting with The One API. This library provides a convenient `TheOneClient` class that provides methods for interacting with The One API.

## Installation

You can install the `daniel-cavazos-sdk` package using `pip`:

```
pip install daniel-cavazos-sdk
```

## Usage

First, import the `TheOneClient` class from the `daniel_cavazos_sdk` module:

```python
from daniel_cavazos_sdk.client import TheOneClient
```

Then, create an instance of the `TheOneClient` class with your API token:

```python
client = TheOneClient(token="your-api-token")
```

Now, you can use the various methods available in the `TheOneClient` class to interact with TheOneAPI:

```python
# get all movies
all_movies = client.get_movies()

# get a specific movie by ID
movie = client.get_movie(id="123")

# get all quotes for a specific movie by ID
movie_quotes = client.get_movie_quotes(id="123")

# get all quotes
all_quotes = client.get_quotes()

# get a specific quote by ID
quote = client.get_quote(id="123")
```

Each method returns the parsed JSON response from the API. If the response has a non-2xx status code, a `requests.exceptions.HTTPError` is raised.

## Contributing

If you find any bugs or issues with this package, please report them on the [GitHub Issues page](https://github.com/Caaz/daniel-cavazos-sdk/issues).

If you would like to contribute to the development of this package, please fork the repository and submit a pull request with your changes.

## License

This package is distributed under the MIT License. See the `LICENSE` file for more information.