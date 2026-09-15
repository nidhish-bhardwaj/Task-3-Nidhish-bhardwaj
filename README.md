# AI Recommendation System

DecodeLabs AI Internship - Project 3: AI Recommendation Logic

## Project Overview

This project is a simple AI-based Movie Recommendation System.

The system takes the user's movie genre or interest as input and
recommends movies based on the similarity between the user's
preference and movie genres.

The project uses TF-IDF and Cosine Similarity to find relevant
movies and display the top recommendations.

## Objective

The main objective of this project is to understand:

- User preference input
- Pattern matching
- Similarity-based recommendation
- TF-IDF
- Cosine Similarity
- Ranking recommendations

## Key Features

- Takes user's preferred genre as input
- Uses movie genre information
- Calculates similarity between user preference and movies
- Ranks movies based on similarity score
- Displays top 10 recommended movies
- Shows similarity score for each recommendation

## Dataset

The project uses a movie dataset containing information such as:

- Movie ID
- Movie Title
- Movie Genres

Example genres:

- Action
- Comedy
- Drama
- Horror
- Romance
- Adventure
- Animation
- Fantasy

## Algorithm Used

### TF-IDF

TF-IDF (Term Frequency-Inverse Document Frequency) converts the
movie genre text into numerical values.

### Cosine Similarity

Cosine Similarity compares the user's preference with movie genres
and calculates how similar they are.

Movies with higher similarity scores are ranked higher in the
recommendation list.

## How the Project Works

The project follows these steps:

1. Load the movie dataset.
2. Process the movie genres.
3. Convert genres into numerical vectors using TF-IDF.
4. Take the user's preferred genre as input.
5. Convert the user preference into a TF-IDF vector.
6. Calculate Cosine Similarity.
7. Sort movies according to similarity score.
8. Display the top 10 recommended movies.

## Project Flow

User Input
↓
Preference Processing
↓
TF-IDF Vectorization
↓
Cosine Similarity
↓
Similarity Score
↓
Ranking
↓
Top 10 Movie Recommendations

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

## Installation

Install the required libraries:

```bash
pip install pandas scikit-learn

## Dataset and License

This project uses the Movie Recommendation System dataset
available on Kaggle.

**Dataset Source:**
Kaggle - Movie Recommendation System by Manas Parashar

**Original Dataset:** MovieLens

**Kaggle Dataset:**
https://www.kaggle.com/datasets/parasharmanas/movie-recommendation-system

### License

The database is provided under the Open Database License (ODbL).

Database: Open Database
Contents: © Original Authors

The dataset is used for educational and project demonstration
purposes in this AI recommendation system.

License:
https://opendatacommons.org/licenses/odbl/1-0/

