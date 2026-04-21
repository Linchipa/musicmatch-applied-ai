import os
from dotenv import load_dotenv
from google import genai
from typing import List, Tuple, Dict

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def explain_recommendations(user_prefs: Dict, recommendations: List[Tuple[Dict, float, str]]) -> str:
    """
    Takes the user's taste profile and their top recommended songs,
    sends them to Gemini, and returns a friendly paragraph explanation.
    """
    # Build a summary of the top songs to include in the prompt
    songs_summary = ""
    for i, (song, score, reasons) in enumerate(recommendations, start=1):
        songs_summary += (
            f"{i}. {song['title']} by {song['artist']} "
            f"(genre: {song['genre']}, mood: {song['mood']}, "
            f"energy: {song['energy']}) — matched because: {reasons}\n"
        )

    prompt = f"""You are MusicMatch, a friendly and knowledgeable music buddy.
You know a lot about music but you talk like a real friend — warm, casual, and enthusiastic.

A user has the following taste profile:
- Favorite genre: {user_prefs['genre']}
- Favorite mood: {user_prefs['mood']}
- Target energy level: {user_prefs['energy']} (scale of 0.0 to 1.0)
- Likes acoustic music: {user_prefs.get('likes_acoustic', False)}

Based on their profile, here are their top 5 recommended songs:
{songs_summary}
Write one friendly paragraph (4-6 sentences) explaining these recommendations to the user.
Talk directly to them. Mention specific song titles and why they fit.
Sound like a knowledgeable friend, not a robot reading a list."""

    try:
        response = client.models.generate_content(
            model="gemma-3-1b-it",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"(AI explanation unavailable: {e})"
