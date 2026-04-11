"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = [
        {"name": "Pop/Happy",    "genre": "pop",  "mood": "happy",   "energy": 0.8,  "likes_acoustic": False},
        {"name": "Chill Lofi",   "genre": "lofi", "mood": "chill",   "energy": 0.35, "likes_acoustic": True},
        {"name": "Intense Rock", "genre": "rock", "mood": "intense", "energy": 0.9,  "likes_acoustic": False},
    ]

    for profile in profiles:
        print(f"\n=== {profile['name']} ===\n")
        recommendations = recommend_songs(profile, songs, k=5)
        for song, score, explanation in recommendations:
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()


if __name__ == "__main__":
    main()
