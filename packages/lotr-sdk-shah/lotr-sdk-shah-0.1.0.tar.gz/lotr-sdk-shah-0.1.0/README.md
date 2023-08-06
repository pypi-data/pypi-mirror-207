```
TLDR: This SDK provides a simple way to interact with The Lord of the Rings API using Python. It allows you to fetch movies, characters, and quotes from the API with easy-to-use methods.
```

# The Lord of the Rings SDK

A simple Python SDK for accessing the Lord of the Rings API. This SDK provides an easy-to-use interface for interacting with the movie and quote endpoints.

The purpose of an SDK is to provide an interface for developers to interact with an API more easily. This project is a Python library that wraps the Lord of the Rings API, making it simpler to access and interact with the API endpoints.

An API (Application Programming Interface) is a set of rules and protocols that allow different software applications to communicate with each other. The Lord of the Rings API is an example of an API.

An SDK is a collection of software tools, libraries, and documentation that makes it easier for developers to use an API, create software, or interact with a service. The code provided is an example of an SDK that simplifies the process of interacting with the Lord of the Rings API.

The provided SDK includes methods that make it easy to access movie and quote endpoints without having to manually construct HTTP requests. By using this SDK, developers can focus on implementing their application logic without worrying about the details of interacting with the Lord of the Rings API directly.

# Features

In each method, the optional `limit`, `page`, and `offset` parameters are used to build the appropriate query parameters for pagination. The optional `filters` parameter is used to build filter expressions using MongoDB lookup expressions. Finally, the optional `sort` parameter is used to specify sorting options. 

You can use these methods like this:

```
sdk = LOTRSDK(api_key='your_api_key')
```

Get the first 100 characters sorted by name ascending

```
characters = sdk.get_characters(limit=100, sort="name:asc")
```

Get the second page of characters with race Hobbit or Human

```
filters = {"race": {"$in": ["Hobbit", "Human"]}}
characters = sdk.get_characters(page=2, filters=filters)
```

Get characters with name starting with "Gandalf" and exclude those with race "Orc" or "Goblin"

```
filters = {"name": {"$regex": "^Gandalf"}, "race": {"$nin": ["Orc", "Goblin"]}}
characters = sdk.get_characters(filters=filters)
```

Get quotes for the first movie with a rating of at least 8.0

```
filters = {"movies.0.rating": {"$gte": 8.0}}
quotes = sdk.get_quotes(filters=filters)
```

Get the first 50 quotes for the first movie sorted by character name descending

```
filters = {"movies.0.rating": {"$gte": 8.0}}
sort = "character:desc"
quotes = sdk.get_movie_quotes(id="movie_id", limit=50, sort=sort, filters=filters)
```


# Some different example usage of SDK with movies and quotes

```
from lordoftheringssdk import LOTRSDK

api_key = "your_api_key_here"
sdk = LOTRSDK(api_key)

# Get a list of movies
movies = sdk.get_movies()
print(movies)

# Get a specific movie by ID
movie = sdk.get_movie("5cd95395de30eff6ebccde5c")

# Get movie quotes for a specific movie by ID
movie_quotes = sdk.get_movie_quotes("5cd95395de30eff6ebccde5c")

# Get a list of quotes
quotes = sdk.get_quotes()

# Get a specific quote by ID
quote = sdk.get_quote("5cd97b6bde30eff6ebccfe9a")
print(quote)

# Get a list of characters
characters = sdk.get_characters()
print(characters)

# Get a list of movies
movies = sdk.get_movies(params={"limit": 5, "page": 2})
print(movies)

# Get the first 5 characters sorted by name
characters = sdk.get_characters(params={"limit": 5, "sort": "name:asc"})
print(characters)

# Get quotes for a specific character
character_quotes = sdk.get_quotes(params={"character": "5cd99d4bde30eff6ebcce0a2"})
print(character_quotes)

# Get a list of characters with optional parameters
characters = sdk.get_characters(params={"name": "Gandalf", "race": "Hobbit,Human"})
print(characters)

# Get a movie quote for a specific movie by ID
movie_id = "5cd95395de30eff6ebccde5c"
quotes = sdk.get_movie_quotes(movie_id, params={"limit": 5, "page": 1})
print(quotes)

```

```
from lotr_sdk import LOTRSDK, LOTRException

api_key = "your-api-key-123"
sdk = LOTRSDK(api_key)

# Get all quotes with pagination support
quotes = sdk.get_quotes(page=1, limit=10)
print(quotes)

# Get a specific quote by ID
quote_id = "5cd96e05de30eff6ebccfea0"  # Example quote ID
try:
    quote = sdk.get_quote(quote_id)
    print(quote)
except LOTRException as e:
    print(f"Error: {e}")
```

```
from lotr_sdk import LOTRSDK, LOTRException

api_key = "your-api-key-123"
sdk = LOTRSDK(api_key)

    # Get all movies with pagination support
movies = sdk.get_movies(page=1, limit=10)
print(movies)

    # Get a specific movie by ID
movie_id = "5cd95395de30eff6ebcce7e9"  # Example movie ID
try:
    movie = sdk.get_movie(movie_id)
    print(movie)
except LOTRException as e:
    print(f"Error: {e}")

    # Get all movie quotes for a specific movie by ID with caching
sdk_cached = LOTRSDK(api_key, cache_expire_after=3600)
movie_quotes = sdk_cached.get_movie_quotes(movie_id, page=1, limit=10)
print(movie_quotes)
```

# Methods

get_quotes(page=1, limit=10): Retrieves a list of quotes with pagination support by passing the page and limit parameters.

get_quote(id): Retrieves a specific quote by its ID.


## Install the libraries
```
pip install requests
```

```
pip install ratelimiter
```

To install the sdk, run the following command:
```
pip install lordoftheringssdk
```
### Use it in your projects like this:




# Usage

```
api_key = "your-api-key-123"
sdk = LOTRSDK(api_key)

# Get all movies with pagination support
movies = sdk.get_movies(page=1, limit=10)

# Get a specific movie by ID
movie_id = "5cd95395de30eff6ebcce7e9"
try:
    movie = sdk.get_movie(movie_id)
except LOTRException as e:
    print(f"Error: {e}")

# Get all movie quotes for a specific movie by ID with caching
sdk_cached = LOTRSDK(api_key, cache_expire_after=3600)
movie_quotes = sdk_cached.get_movie_quotes(movie_id, page=1, limit=10)
```

# Usage in application
1. Include the updated LOTRSDK class in your project.
2. In your application code, import the LOTRSDK class and create an instance of it using your API key:

```
from your_sdk_module import LOTRSDK

api_key = "your-api-key"
sdk = LOTRSDK(api_key)
```

3. To interact with the API endpoints, create a params dictionary containing the pagination, sorting, and filtering options you want to use. For example, if you want to get a list of characters sorted by name in ascending order and filter them by race:

```
params = {
    "sort": "name:asc",
    "race": "Hobbit,Human"
}
characters = sdk.get_characters(params=params)
print(characters)
```

4. If you want more options to apply to the API request, you can use the following:

```
sdk = LOTRSDK(api_key)

    # Get characters with filtering, sorting, and pagination

params = {
    "limit": 100,
    "page": 2,
    "sort": "name:asc",
    "name": "Gandalf",
    "race": "Hobbit,Human",
    "name!": "Frodo",
    "name!": "/foot/i",
    "budgetinmillions<": 100,
    "academyawardwins>": 0,
    "runtimeinminutes>=": 160
}
characters = sdk.get_characters(params=params)
print(characters)
```

You can use any combination of pagination, sorting, and filtering options in the params dictionary. 
The SDK will pass these options to the API, and the response will include the requested data according to the specified options.

# Extensibility
The SDK is designed with extensibility in mind. Additional endpoints can be easily added by following the same pattern used for the existing endpoints.

# Testing
To test the SDK, you can create a separate Python script that imports and uses the SDK with various use cases. Make sure to use a valid API key for testing. 

## Download test_sdk.py and save the script in your project directory and you can run it with:

```
python -m unittest TestLOTRSDK.py
```

**TestLOTRSDK.py**
```
import unittest
from lordoftheringssdk import LOTRSDK
api_key = "your_api_key_here"
    
class TestLOTRSDK(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sdk = LOTRSDK(cls.api_key)

    def test_get_movies(self):
        movies = self.sdk.get_movies(limit=5, sort="budgetinmillions:desc")
        self.assertIsInstance(movies, list)
        self.assertTrue(len(movies) > 0)

    def test_get_movie_quotes(self):
        movie_id = "5cd95395de30eff6ebccde5c"
        quotes = self.sdk.get_movie_quotes(movie_id, limit=5, page=2, sort="character:asc")
        self.assertIsInstance(quotes, list)
        self.assertTrue(len(quotes) > 0)

    def test_get_quotes(self):
        quotes = self.sdk.get_quotes(limit=5, filter={"dialogue": "/^.*ring.*$/i"})
        self.assertIsInstance(quotes, list)
        self.assertTrue(len(quotes) > 0)

    def test_get_characters(self):
        characters = self.sdk.get_characters(limit=10, page=2, filter={"race": {"$in": ["Hobbit", "Elf"]}}, sort="name:asc")
        self.assertIsInstance(characters, list)
        self.assertTrue(len(characters) > 0)

    def setUp(self):
        self.sdk = LOTRSDK(api_key="your_api_key")

    def test_get_movies(self):
        response = self.sdk.get_movies(limit=10)
        self.assertEqual(len(response["docs"]), 10)

    def test_get_movie(self):
        response = self.sdk.get_movie(id="5cd95395de30eff6ebccde81")
        self.assertEqual(response["name"], "The Lord of the Rings: The Fellowship of the Ring")

    def test_get_movie_quotes(self):
        response = self.sdk.get_movie_quotes(id="5cd95395de30eff6ebccde81", limit=10)
        self.assertEqual(len(response["docs"]), 10)

    def test_get_quotes(self):
        response = self.sdk.get_quotes(limit=10)
        self.assertEqual(len(response["docs"]), 10)

    def test_get_quote(self):
        response = self.sdk.get_quote(id="5cd96e05de30eff6ebccf66d")
        self.assertEqual(response["dialog"], "All we have to decide is what to do with the time that is given us.")

    def test_get_characters(self):
        response = self.sdk.get_characters(limit=10)
        self.assertEqual(len(response["docs"]), 10)

    def test_get_character(self):
        response = self.sdk.get_character(id="5cd99d4bde30eff6ebcd473b")
        self.assertEqual(response["name"], "Gandalf")

    def test_get_character_quotes(self):
        response = self.sdk.get_character_quotes(id="5cd99d4bde30eff6ebcd473b", limit=10)
        self.assertEqual(len(response["docs"]), 10)

    def test_get_books(self):
        response = self.sdk.get_books(limit=10)
        self.assertEqual(len(response["docs"]), 10)

    def test_get_book(self):
        response = self.sdk.get_book(id="5cf5805fb53e011a64671582")
        self.assertEqual(response["name"], "The Lord of the Rings")

    def test_get_chapters(self):
        response = self.sdk.get_chapters(limit=10)
        self.assertEqual(len(response["docs"]), 10)

    def test_get_chapter(self):
        response = self.sdk.get_chapter(id="5cf5805fb53e011a64671585")
        self.assertEqual(response["name"], "A Long-expected Party")


if __name__ == "__main__":
    unittest.main()
    print("All tests passed!")
```

These tests check if the response types and content are as expected when calling the SDK methods. You can add more test cases or modify the existing ones to further test the functionality of your SDK.
If all tests pass, you should see the message "All tests passed! printed into your terminal. 

# How to package and publish it to the Python Package Index (PyPI)
1. If you don't have setuptools, wheel, and twine installed, install them using the following command:

```
pip install setuptools wheel twine
```
2. Create a 'setup.py' file in your projects root directory with this content in it:
** Make sure to replace 'Your Name' and 'your.email@example.com' and 'github repository url' with your own information **

```
from setuptools import setup, find_packages

setup(
    name="lotr-sdk",
    version="0.1.0",
    description="A Python SDK for The Lord of the Rings API",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/lotr-sdk",
    packages=find_packages(),
    install_requires=[
        "requests",
        "requests_cache",
        "ratelimiter",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
```

3. Create a `.pypirc` file in your home directory (%userprofile%\.pypirc on Windows), ('~/.pypirc' on UNIX systems), with this content:

```
[pypi]
username = your_username
password = your_password
```

4. Build the pakcage by running this command on your projects root directory, this command creates a 'dist' folder containing the
source distribution and the wheel distribution of this package:

```
python setup.py sdist bdist_wheel
```

5. Upload the package to PyPi using twine: 

```
twine upload dist/*
```

6. Now the package is available on Twine and can be installed using pip:

```
pip install lotr-sdk-shah
```

