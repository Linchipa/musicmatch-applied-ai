"""
MusicMatch Applied AI System
Extends the Module 3 recommender with Gemini AI explanations,
input validation, confidence scoring, and logging.
"""

import time
from src.recommender import load_songs, recommend_songs
from src.ai_explainer import explain_recommendations
from src.guardrails import setup_logging, validate_user_prefs, compute_confidence, log_recommendation


def main() -> None:
    setup_logging()
    songs = load_songs("data/songs.csv")

    profiles = [
        {"name": "Pop/Happy",    "genre": "pop",  "mood": "happy",   "energy": 0.8,  "likes_acoustic": False},
        {"name": "Chill Lofi",   "genre": "lofi", "mood": "chill",   "energy": 0.35, "likes_acoustic": True},
        {"name": "Intense Rock", "genre": "rock", "mood": "intense", "energy": 0.9,  "likes_acoustic": False},
    ]

    for profile in profiles:
        print(f"\n{'='*50}")
        print(f"  {profile['name']}")
        print(f"{'='*50}\n")

        # Step 1: Validate inputs before doing anything
        is_valid, error_message = validate_user_prefs(profile)
        if not is_valid:
            print(f"  Invalid profile — skipping. Reason: {error_message}\n")
            continue

        # Step 2: Run the recommender
        recommendations = recommend_songs(profile, songs, k=5)

        # Step 3: Print scored results with confidence
        print("Top 5 Matches:\n")
        for song, score, explanation in recommendations:
            confidence = compute_confidence(score)
            print(f"  {song['title']} by {song['artist']}")
            print(f"  Score: {score:.2f} | Confidence: {confidence}%")
            print(f"  Why: {explanation}")
            print()

        # Step 4: Log this run
        log_recommendation(profile, recommendations)

        # Step 5: Get and print the Gemini AI explanation
        print("MusicMatch says:\n")
        explanation = explain_recommendations(profile, recommendations)
        print(f"  {explanation}\n")

        # Pause between profiles to respect free tier rate limits
        time.sleep(10)


if __name__ == "__main__":
    main()
