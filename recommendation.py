import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv(r"c:\Users\hp\Downloads\archive\movies.csv")

movies["genres"] = movies["genres"].str.replace("|", " ", regex=False)

tfidf = TfidfVectorizer()
matrix = tfidf.fit_transform(movies["genres"])

def recommend(genre):
    user_vector = tfidf.transform([genre])

    similarity = cosine_similarity(user_vector, matrix)[0]

    movies["score"] = similarity

    recommendations = movies.sort_values(
        "score",
        ascending=False
    )

    print("\nRecommended Movies")
    print("=" * 40)

    count = 0

    for _, movie in recommendations.iterrows():
        if movie["score"] > 0:
            count += 1
            print(f"\n{count}. {movie['title']}")
            print(f"Genre: {movie['genres']}")
            print(f"Similarity Score: {movie['score'] * 100:.2f}%")

        if count == 10:
            break

    if count == 0:
        print("No matching movies found.")

print("AI Movie Recommendation System")
print("=" * 40)

genre = input(
    "\nEnter your preferred genre "
    "(Action, Comedy, Horror, Romance, etc.): "
)

recommend(genre)