import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


GENRE_MAP = {
    "Avatar": "Sci-Fi",
    "Avengers: Endgame": "Action",
    "Avatar: The Way of Water": "Sci-Fi",
    "Titanic": "Romance",
    "Ne Zha 2": "Animation/Fantasy",
    "Star Wars: The Force Awakens": "Sci-Fi/Action",
    "Avengers: Infinity War": "Action/Sci-Fi",
    "Spider-Man: No Way Home": "Action/Superhero",
    "Inside Out 2": "Animation/Family",
    "Jurassic World": "Adventure/Sci-Fi",
    "The Lion King": "Animation/Drama",
    "The Avengers": "Action/Superhero",
    "Furious 7": "Action",
    "Top Gun: Maverick": "Action/Drama",
    "Frozen 2": "Animation/Musical",
    "Barbie": "Fantasy/Comedy",
    "Avengers: Age of Ultron": "Action/Sci-Fi",
    "The Super Mario Bros. Movie": "Animation/Adventure",
    "Black Panther": "Superhero/Action",
    "Harry Potter and the Deathly Hallows – Part 2": "Fantasy/Adventure",
    "Deadpool & Wolverine": "Action/Comedy",
    "Star Wars: The Last Jedi": "Sci-Fi/Action",
    "Jurassic World: Fallen Kingdom": "Adventure/Sci-Fi",
    "Frozen": "Animation/Musical",
    "Beauty and the Beast": "Fantasy/Musical",
    "Incredibles 2": "Animation/Action",
    "The Fate of the Furious": "Action",
    "Iron Man 3": "Action/Sci-Fi",
    "Minions": "Animation/Comedy",
    "Captain America: Civil War": "Action/Superhero",
    "Aquaman": "Action/Fantasy",
    "The Lord of the Rings: The Return of the King": "Fantasy/Adventure",
    "Spider-Man: Far From Home": "Action/Superhero",
    "Captain Marvel": "Action/Sci-Fi",
    "Transformers: Dark of the Moon": "Action/Sci-Fi",
    "Skyfall": "Action/Thriller",
    "Transformers: Age of Extinction": "Action/Sci-Fi",
    "The Dark Knight Rises": "Action/Thriller",
    "Joker": "Drama/Crime",
    "Star Wars: The Rise of Skywalker": "Sci-Fi/Action",
    "Toy Story 4": "Animation/Comedy",
    "Toy Story 3": "Animation/Comedy",
    "Pirates of the Caribbean: Dead Man's Chest": "Adventure/Fantasy",
    "Moana 2": "Animation/Adventure",
    "Rogue One: A Star Wars Story": "Sci-Fi/Action",
    "Aladdin": "Fantasy/Musical",
    "Star Wars: Episode I – The Phantom Menace": "Sci-Fi/Action",
    "Pirates of the Caribbean: On Stranger Tides": "Adventure/Fantasy",
    "Jurassic Park": "Adventure/Sci-Fi",
    "Despicable Me 3": "Animation/Comedy",
}


def fetch_and_save_html(url, path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(response.text)
        print("[✔] HTML file saved successfully!")
    except requests.RequestException as e:
        print(f"[❌] Error fetching data: {e}")
    except IOError as e:
        print(f"[❌] Error saving file: {e}")

def extract_table_to_csv(html_path, csv_path):
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
        table = soup.find("table", {"class": "wikitable"})
        df = pd.read_html(str(table))[0]

        
        def get_genre(title):
            for key in GENRE_MAP:
                if key.lower() in title.lower():
                    return GENRE_MAP[key]
            return "Unknown"

        df['Genre'] = df['Title'].apply(get_genre)

        df.to_csv(csv_path, index=False)
        print(f"[✔] Data saved to {csv_path}")
        return df
    except Exception as e:
        print(f"[❌] Error extracting table: {e}")
        return None

def suggest_by_genre(df, genre_input):
    try:
        genre_input = genre_input.lower()
        filtered = df[df['Genre'].str.lower().str.contains(genre_input)]

        if not filtered.empty:
            print(f"\n Movies in genre '{genre_input}':\n")
            print(filtered[['Title', 'Genre', 'Worldwide gross']].head(10))
        else:
            print(f"[!] No movies found in genre '{genre_input}'.")
    except Exception as e:
        print(f"[❌] Error suggesting movies: {e}")

if __name__ == "__main__":
    URL = "https://en.wikipedia.org/wiki/List_of_highest-grossing_films"
    HTML_PATH = "data/highest_grossing_films.html"
    CSV_PATH = "data/highest_grossing_films.csv"

    fetch_and_save_html(URL, HTML_PATH)
    df = extract_table_to_csv(HTML_PATH, CSV_PATH)

    if df is not None:
        user_input = input("\nEnter a genre to get movie suggestions (e.g., 'action', 'animation', 'drama', 'Sci-Fi', 'Thriller','Adventure'): ")
        suggest_by_genre(df, user_input)
