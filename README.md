# Python-Project-Submission-Vishwas

# Box Office Blockbusters: Genre Categorization & Analysis

## Project Description

This project involves processing and analyzing a dataset of the top 50 highest-grossing films of all time. The goal is to:

- Identify each film’s **correct genre**, especially when it was listed as “Unknown”.
- Normalize and structure the data to be usable in applications (e.g., web-based dashboards, APIs, or analytical tools).
- Provide a **Python dictionary** (`GENRE_MAP`) that maps each film to its accurate genre classification.

This project is especially useful for developers, analysts, or filmmakers who need clean, categorized data for visualizations, film recommendations, or trend analysis.

---

## Software & Libraries Used

| Tool/Library        | Purpose                                         |
|---------------------|-------------------------------------------------|
| Python 3.x          | Core programming language                       |
| pandas              | Data parsing, filtering, and transformation     |
| requests            | (Optional) For accessing film info from APIs    |
| BeautifulSoup       | (Optional) For web scraping from review sites   |
| JSON                | Data formatting and exporting                   |



## Project Structure

```
├── genre_mapper.py         # Python script with GENRE_MAP dictionary
├── raw_data.csv            # Original film dataset (comma-separated)
├── genre_fixer.py          # Script to clean up 'Unknown' genres
├── README.md               # Project documentation
```

---

## How to Run

1. **Clone the Repository**  
```bash
git clone https://github.com/yourusername/movie-genre-fixer.git
cd movie-genre-fixer
```

2. **Install Required Libraries**  
```bash
pip install pandas beautifulsoup4 requests
```

3. **Run the Script**  
```bash
python genre_fixer.py
```

The script will read the raw CSV data, apply correct genres using the `GENRE_MAP`, and output a clean, structured dataset ready for use.

---

## Output

- A cleaned list of the top 50 movies with accurate genres.
- A `GENRE_MAP` Python dictionary for developers.
- Optional: JSON export for front-end or API use.

## Developer
- Vishwas Tyagi


