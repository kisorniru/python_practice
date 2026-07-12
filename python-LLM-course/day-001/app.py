from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# 1. We are using a demo database (Cause we don't have any LLM or original vector Database)
movies_database = [
    {"id": 1, "title": "Interstellar", "desc": "Science fiction, space exploration, wormhole, black holes, astronauts, time dilation, survival, artificial intelligence, family drama."},

    {"id": 2, "title": "The Conjuring", "desc": "Supernatural horror, haunted house, ghosts, demons, paranormal investigation, exorcism, suspense, psychological horror."},

    {"id": 3, "title": "Die Hard", "desc": "Action thriller, police officer, terrorists, skyscraper, hostage rescue, explosions, gunfights, survival."},

    {"id": 4, "title": "Avatar", "desc": "Science fiction adventure, alien planet, Pandora, Na'vi, futuristic technology, space travel, environmental conflict, epic battle."},

    {"id": 5, "title": "The Martian", "desc": "Science fiction, Mars, astronaut, survival, NASA, engineering, botany, rescue mission."},

    {"id": 6, "title": "Apollo 13", "desc": "Historical drama, space mission, NASA, astronauts, engineering, teamwork, real events, lunar mission."},

    {"id": 7, "title": "Inception", "desc": "Science fiction thriller, dreams, subconscious mind, mind bending, heist, psychological, action, layered reality."},

    {"id": 8, "title": "The Dark Knight", "desc": "Superhero action, Batman, Joker, crime, Gotham City, detective, vigilante, thriller."},

    {"id": 9, "title": "Titanic", "desc": "Romantic drama, historical disaster, shipwreck, love story, ocean voyage, survival, tragedy."},

    {"id": 10, "title": "The Shawshank Redemption", "desc": "Prison drama, friendship, hope, injustice, escape, perseverance, redemption."},

    {"id": 11, "title": "The Godfather", "desc": "Crime drama, mafia, organized crime, family business, power, betrayal, leadership."},

    {"id": 12, "title": "The Matrix", "desc": "Science fiction, virtual reality, artificial intelligence, hackers, cyberpunk, action, dystopian future."},

    {"id": 13, "title": "Jurassic Park", "desc": "Adventure, dinosaurs, genetic engineering, theme park, survival, science fiction, action."},

    {"id": 14, "title": "Jaws", "desc": "Thriller, shark attack, ocean, beach town, suspense, survival, horror."},

    {"id": 15, "title": "Gladiator", "desc": "Historical epic, Roman Empire, revenge, gladiator, war, leadership, action."},

    {"id": 16, "title": "Finding Nemo", "desc": "Animated adventure, ocean, fish, family, friendship, underwater world, comedy."},

    {"id": 17, "title": "Frozen", "desc": "Animated fantasy, princesses, magic, snow, family, adventure, musical."},

    {"id": 18, "title": "Mad Max: Fury Road", "desc": "Post apocalyptic action, desert, survival, vehicles, warlords, high-speed chase."},

    {"id": 19, "title": "John Wick", "desc": "Action thriller, assassin, revenge, gunfights, criminal underworld, martial arts."},

    {"id": 20, "title": "The Silence of the Lambs", "desc": "Psychological thriller, serial killer, FBI, investigation, crime, suspense, horror."},
]

@app.route('/')
def home():
    # This will return a very simple HTML page where will be a search box only
    return '''
        <form action="/search" method="POST">
            <input type="text" name="query" placeholder="What kind of movie do you want?" style="width:300px;">
            <button type="submit">Search</button>
        </form>
    '''

@app.route('/search', methods=['POST'])
def search():
    user_query = request.form.get('query')
    
    all_descriptions = [movie['desc'] for movie in movies_database]
    all_descriptions.append(user_query)
    
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_descriptions)
    
    movie_vectors = tfidf_matrix[:-1]
    query_vector = tfidf_matrix[-1]
    
    similarity_scores = cosine_similarity(query_vector, movie_vectors).flatten()
    
    # --- নতুন কোড শুরু ---
    # স্কোরের ভিত্তিতে বড় থেকে ছোট ক্রমানুসারে (Descending order) সাজানো
    # এবং সেরা ৫টি মুভির ইনডেক্স নেওয়া
    top_indices = similarity_scores.argsort()[::-1][:5]
    
    html_output = f"<h2>Search Results for: '{user_query}'</h2><ol>"
    
    for index in top_indices:
        score = similarity_scores[index]
        if score > 0:  # শুধু মিল থাকা মুভিগুলো দেখাবে
            movie = movies_database[index]
            html_output += f"""
                <li>
                    <strong>{movie['title']}</strong> (Match: {round(float(score)*100, 1)}%) <br>
                    <em>Tags: {movie['desc']}</em>
                </li><br>
            """
            
    html_output += "</ol><a href='/'>Search Again</a>"
    return html_output
    # --- নতুন কোড শেষ ---


if __name__ == '__main__':
    app.run(debug=True)
