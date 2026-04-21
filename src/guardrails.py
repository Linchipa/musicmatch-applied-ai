import logging
import os
from typing import Dict, Tuple

# Valid values based on the songs.csv catalog
VALID_GENRES = [
    "pop", "lofi", "rock", "jazz", "ambient",
    "synthwave", "indie pop", "latin", "electronic", "acoustic"
]
VALID_MOODS = [
    "happy", "chill", "intense", "moody",
    "sad", "relaxed", "focused", "nostalgic"
]

MAX_SCORE = 6.5


def setup_logging():
    """Sets up logging to both the console and a log file in logs/."""
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.FileHandler("logs/musicmatch.log"),
            logging.StreamHandler()
        ]
    )


def validate_user_prefs(prefs: Dict) -> Tuple[bool, str]:
    """
    Validates a user preferences dictionary.
    Returns (True, "") if valid, or (False, error message) if not.
    """
    genre = prefs.get("genre", "")
    mood = prefs.get("mood", "")
    energy = prefs.get("energy", None)
    likes_acoustic = prefs.get("likes_acoustic", None)

    if not isinstance(genre, str) or genre not in VALID_GENRES:
        return False, f"Invalid genre '{genre}'. Must be one of: {', '.join(VALID_GENRES)}"

    if not isinstance(mood, str) or mood not in VALID_MOODS:
        return False, f"Invalid mood '{mood}'. Must be one of: {', '.join(VALID_MOODS)}"

    if not isinstance(energy, (int, float)) or not (0.0 <= energy <= 1.0):
        return False, f"Invalid energy '{energy}'. Must be a number between 0.0 and 1.0"

    if not isinstance(likes_acoustic, bool):
        return False, f"Invalid likes_acoustic '{likes_acoustic}'. Must be True or False"

    return True, ""


def compute_confidence(score: float) -> int:
    """Converts a raw score (0–6.5) into a confidence percentage (0–100)."""
    return round((score / MAX_SCORE) * 100)


def log_recommendation(user_prefs: Dict, recommendations: list):
    """Logs a recommendation run with inputs and top result."""
    logger = logging.getLogger(__name__)
    top_song, top_score, top_reasons = recommendations[0]
    confidence = compute_confidence(top_score)
    logger.info(
        f"User: genre={user_prefs['genre']}, mood={user_prefs['mood']}, "
        f"energy={user_prefs['energy']} | "
        f"Top pick: '{top_song['title']}' (score={top_score}, confidence={confidence}%)"
    )
