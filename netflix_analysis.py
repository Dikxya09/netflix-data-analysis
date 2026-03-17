# Perform exploratory data analysis on the netflix_data.csv data to understand more about movies from the 1990s decade.
# What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration (use 1990 as the decade's start year).
# A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the 1990s and save this integer as short_movie_count.

import pandas as pd
netflix = pd.read_csv("netflix_data.csv")

movies_1990s = netflix[(netflix["release_year"] >= 1990) & (netflix["release_year"] < 2000)]

short_movies_list = []

for index, movie in movies_1990s.iterrows():
    if movie["duration"] < 90:
        short_movies_list.append(movie)

print("1990s short movies:")
print(short_movies_list)
# Filter 1990s movies
netflix_1990s = netflix[(netflix['release_year'] >= 1990) & (netflix['release_year'] < 2000)]
movies_1990s = netflix_1990s[netflix_1990s['type'] == 'Movie']

# Most frequent duration
duration = int(movies_1990s['duration'].mode()[0])
print("Most frequent movie duration in 1990s:", duration)

action_movies_1990s = movies_1990s[
    movies_1990s['genre'].str.contains('Action', case=False, na=False)
]

# Count short movies
short_movie_count = action_movies_1990s[
    action_movies_1990s['duration'] < 90
].shape[0]

print("Number of short action movies in 1990s:", short_movie_count)