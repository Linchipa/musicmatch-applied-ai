from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        def score(song: Song) -> float:
            s = 0.0
            if song.genre == user.favorite_genre:
                s += 3.0
            if song.mood == user.favorite_mood:
                s += 2.0
            energy_score = round(1.0 - abs(song.energy - user.target_energy), 2)
            if energy_score > 0:
                s += energy_score
            if user.likes_acoustic and song.acousticness >= 0.5:
                s += 0.5
            return s

        return sorted(self.songs, key=score, reverse=True)[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []
        if song.genre == user.favorite_genre:
            reasons.append("genre match")
        if song.mood == user.favorite_mood:
            reasons.append("mood match")
        energy_gap = abs(song.energy - user.target_energy)
        if energy_gap <= 0.2:
            reasons.append("energy is a close fit")
        elif energy_gap <= 0.5:
            reasons.append("energy is a decent match")
        if user.likes_acoustic and song.acousticness >= 0.5:
            reasons.append("acoustic sound")
        if reasons:
            return f"{song.title} by {song.artist} matches because: {', '.join(reasons)}."
        return f"{song.title} by {song.artist} is a partial match based on overall profile similarity."

def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file and returns them as a list of dictionaries."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song against user preferences and returns a score and list of reasons."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["genre"]:
        score += 3.0
        reasons.append("genre match (+3.0)")

    if song["mood"] == user_prefs["mood"]:
        score += 2.0
        reasons.append("mood match (+2.0)")

    energy_gap = abs(song["energy"] - user_prefs["energy"])
    energy_score = round(1.0 - energy_gap, 2)
    if energy_score > 0:
        score += energy_score
        reasons.append(f"energy score (+{energy_score})")

    if user_prefs.get("likes_acoustic") and song["acousticness"] >= 0.5:
        score += 0.5
        reasons.append("acoustic match (+0.5)")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores all songs, sorts them highest to lowest, and returns the top k recommendations."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons) if reasons else "no strong match"
        scored.append((song, score, explanation))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
