import csv
import re

class Movie:
    def __init__(self, index, genres, original_language, original_title, runtime, title):
        # Initialize Movie object with provided attributes
        self.index = index
        self.genres = genres
        self.original_language = original_language
        self.original_title = original_title
        self.runtime = self.extract_numeric_part(runtime)  # Update the runtime
        self.title = title
