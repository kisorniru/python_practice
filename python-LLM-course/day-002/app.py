from flask import Flask, render_template, request
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

app = Flask(__name__)

# ১. Hugging Face থেকে ফ্রি সেম্যান্টিক এম্বেডিং মডেল লোড করা (ডাইমেনশন: ৩৮৪)
# এই মডেলটি শব্দের গভীর অর্থ বুঝতে পারে
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# আপনার দেওয়া সেই ২০টি মুভির ডেটাসেট
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
    {"id": 20, "title": "The Silence of the Lambs", "desc": "Psychological thriller, serial killer, FBI, investigation, crime, suspense, horror."}
]

# ২. অ্যাপ চালুর সাথেই ডেটাবেজের সব মুভির ডেসক্রিপশনকে আসল AI ভেক্টরে রূপান্তর করে রাখা
movie_descriptions = [movie['desc'] for movie in movies_database]
# এই লাইনটি সব মুভির জন্য ৩৮৪-ডাইমেনশনের রিয়েল এম্বেডিং ভেক্টর তৈরি করবে
movie_vectors = embedding_model.encode(movie_descriptions)

@app.route('/')
def home():
    return '''
        <div style="text-align: center; margin-top: 50px; font-family: Arial;">
            <h2>AI-Powered Semantic Movie Search</h2>
            <form action="/search" method="POST">
                <input type="text" name="query" placeholder="e.g., gun and car chase, scary ghosts, space travel..." style="width:400px; padding:10px;">
                <button type="submit" style="padding:10px 20px; cursor:pointer;">Search</button>
            </form>
        </div>
    '''

@app.route('/search', methods=['POST'])
def search():
    user_query = request.form.get('query')
    
    # ৩. ইউজারের ইনপুট করা প্রশ্নেরও ৩৮৪-ডাইমেনশনের ভেক্টর বের করা
    query_vector = embedding_model.encode([user_query])
    
    # ৪. কসাইন সিমিলারিটি দিয়ে অর্থবোধক তুলনা করা
    similarity_scores = cosine_similarity(query_vector, movie_vectors).flatten()
    
    # সেরা ৫টি রেজাল্ট ক্রমানুসারে নেওয়া
    top_indices = similarity_scores.argsort()[::-1][:5]
    
    # একটি ফ্ল্যাগ ভেরিয়েবল যা ট্র্যাক করবে আমরা কোনো ভালো রেজাল্ট পেয়েছি কিনা
    found_any_good_match = False
    
    html_output = f"<div style='font-family: Arial; margin: 20px;'><h2>Semantic Results for: '{user_query}'</h2><ol>"
    
    for index in top_indices:
        score = similarity_scores[index]
        # if score > 0.1:  # সামান্যতম অর্থ মিললেও দেখাবে মানে ১০% মিললেও দেখাবে । 
        if score > 0.3:  # আমরা এখানে থ্রেশহোল্ড ০.১ থেকে বাড়িয়ে ০.৩ (৩০%) করলাম, কারন ভেক্টর সার্চে ৩০% বা ৩৫% এর নিচের স্কোর মানে মূলত এতে কোনো মিল খুজে পাওয়া যায় নি । 
            found_any_good_match = True
            movie = movies_database[index]
            html_output += f"""
                <li style="margin-bottom: 15px;">
                    <strong style="font-size: 18px; color: #333;">{movie['title']}</strong> 
                    <span style="color: green; font-weight: bold;">(AI Semantic Score: {round(float(score)*100, 1)}%)</span><br>
                    <em style="color: #666;">Tags: {movie['desc']}</em>
                </li>
            """
            
    html_output += "</ol>"
    
    # যদি একটি মুভির স্কোরও ৩০% এর ওপরে না ওঠে
    if not found_any_good_match:
        html_output += "<p style='color: red; font-weight: bold;'>No relevant movies found for your query. Please try searching with meaningful words!</p>"
        
    html_output += "<br><a href='/'>Back to Search</a></div>"
    return html_output

if __name__ == '__main__':
    app.run(debug=True)
