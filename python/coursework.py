# import libraries: This code imports two modules: csv for handling CSV files and re for regular expressions.
import csv
import re  


# This class represents a movie. It has attributes like index, genres, the original
# language and title, runtime, and title.
class Movie:
    def __init__(self, index, genres, original_language, original_title, runtime, title):
        # Initialize Movie object with provided attributes
        self.index = index
        self.genres = genres
        self.original_language = original_language
        self.original_title = original_title
        self.runtime = self.extract_numeric_part(runtime)  # Update the runtime
        self.title = title

# This method of the Movie class uses regular expressions to extract the numeric part
# from the runtime string.
    def extract_numeric_part(self, runtime):
        # Use regular expression to extract numeric part from the runtime string
        match = re.search(r'\d+', runtime)
        return int(match.group()) if match else None


# string representation for the Movie object, making it easier to display information about a movie.
    def __str__(self):
        # Define a string representation for the Movie object
        return f"{self.title} ({self.original_language}) - {self.genres} - {self.runtime} min"
        
# Represents a movie recommendation system. It has methods to load movies
# from a file, save movies to a file, and get recommendations based on genre.
class MovieRecommendation:
    
    # initializes a MovieRecommendation object with an empty list of
    # movies and the file path to the movie data file.
    def __init__(self, file_path):
        self.movies = []
        self.file_path = file_path
        self.load_movies()

# load movies from file: Is trying to open and read the CSV file containing movie data. It creates
# Movie objects for each row in the file and adds them to the list of movies.
    def load_movies(self):
        try:
            # Attempt to open and read the CSV file containing movie data
            with open(self.file_path, 'r', encoding='utf-8') as file:
                # Create a CSV reader object
                reader = csv.DictReader(file)
                # Iterate through each row in the CSV file and create Movie objects
                for row in reader:
                    # Create a Movie object and update the runtime using the extract_numeric_part method
                    movie = Movie(int(row['index']), row['genres'], row['original_language'],row['original_title'], row['runtime'], row['title'])
                    # Add the Movie object to the list of movies
                    self.movies.append(movie)
        except FileNotFoundError:
            # Handle the case where the file is not found
            print(f"Error: File not found at {self.file_path}")
        except Exception as e:
            # Handle other unexpected errors
            print(f"Error: An unexpected error occurred - {e}")


# save movies to file: try to open and read the CSV file containing movie data.
#It creates Movie objects for each row in the file and adds them to the list of movies.
    def save_movies(self):
        try:
            # Attempt to open the CSV file for writing
            with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
                # Create a CSV writer object
                writer = csv.writer(file)
                # Write the header row
                writer.writerow(['index', 'genres', 'original_language', 'original_title', 'runtime', 'title'])
                # Iterate through movies and write each row to the CSV file
                for movie in self.movies:
                    writer.writerow([movie.index, movie.genres, movie.original_language, movie.original_title, movie.runtime, movie.title])
        except Exception as e:
            # Handle other unexpected errors
            print(f"Error: An unexpected error occurred - {e}")

# takes a genre as input and returns a list of movie recommendations for that genre.
    def get_recommendations_by_genre(self, genre):
        # Get a list of movie recommendations for the specified genre
        recommendations = [movie for movie in self.movies if genre.lower() in movie.genres.lower()]
        return recommendations


# takes a list of recommendations and prints them. If there are no recommendations, it indicates that.
def display_recommendations(recommendations):
    if recommendations:
        print("\nRecommendations:")
        for movie in recommendations:
            print(movie)
    else:
        print("No recommendations found for this genre.")


#  main function where the program execution begins.
def main():
    # Specify the path to the movie data file
    file_path = 'movies data.csv'  

    # Create a MovieRecommendation object
    recommendation_system = MovieRecommendation(file_path)


#This loop continues until the user chooses to exit.
    while True:
        # menu display for user
        print("\nWelcome to the Movie Recommendation System!")
        print("1. Get Recommendations by Genre")
        print("2. Add a New Movie")
        print("3. Exit")

        # Get user input for the menu choice
        choice = input("Enter your choice (1, 2, or 3): ")

        #Use try to handle potential errors.
        try:
            # Convert user input to an integer
            choice = int(choice)
            # If the user chooses 1 - get recommendations by genre, prompt for a genre and display recommendations
            if choice == 1:
                genre = input("Enter a genre to get recommendations: ")
                recommendations = recommendation_system.get_recommendations_by_genre(genre)
                display_recommendations(recommendations)
            # If the user chooses 2 - add a new movie, prompt for details, create a new Movie object, and save to file
            elif choice == 2:
                index = int(input("Enter the index for the new movie: "))
                genres = input("Enter genres for the new movie: ")
                language = input("Enter the original language for the new movie: ")
                title = input("Enter the title for the new movie: ")
                runtime = input("Enter the runtime for the new movie (e.g., 110 min): ")
                new_movie = Movie(index, genres, language, title, runtime, title)
                recommendation_system.movies.append(new_movie)
                recommendation_system.save_movies()
                print("New movie added successfully!")
            # If the user chooses 3 - exit, save movies and break out of the loop
            elif choice == 3:
                recommendation_system.save_movies()
                print("Exiting. Thank you!")
                break
            else:
                # user invalid choice
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            # user value error
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    # Run the main function if the script is executed directly
    main()


