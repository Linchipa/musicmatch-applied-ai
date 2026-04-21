# MusicMatch Project Progress

## Who I Am
- GitHub username: Linchipa
- Course: AI110, Module 3 → Final Project
- Working directory: ai110-module3show-musicrecommendersimulation-starter

---

## What We Built (Module 3 Mini Project — COMPLETED)

### Project: MusicMatch
A content-based music recommender in Python that takes a user's taste profile and recommends the top 5 songs from a catalog based on weighted scoring.

### Files completed:
- `data/songs.csv` — expanded from 10 to 30 songs, 10 genres, 3 songs per genre
- `src/recommender.py` — 3 functions fully implemented
- `src/main.py` — runs 3 user profiles for testing
- `README.md` — How The System Works section completed
- `model_card.md` — all 9 sections completed

### Scoring rules we designed:
- Genre match → +3.0 points
- Mood match → +2.0 points
- Energy closeness → up to +1.0 point (1.0 - abs(song_energy - user_energy))
- Acoustic match → +0.5 points (only if user likes_acoustic AND song acousticness >= 0.5)
- Maximum possible score: 6.5 points

### 3 functions implemented in src/recommender.py:
1. `load_songs(csv_path)` — reads CSV, converts numeric columns to float/int
2. `score_song(user_prefs, song)` — returns (score, reasons) tuple
3. `recommend_songs(user_prefs, songs, k=5)` — scores all songs, sorts, returns top k

### 3 user profiles tested in src/main.py:
- Pop/Happy: genre=pop, mood=happy, energy=0.8, likes_acoustic=False
- Chill Lofi: genre=lofi, mood=chill, energy=0.35, likes_acoustic=True
- Intense Rock: genre=rock, mood=intense, energy=0.9, likes_acoustic=False

### Key fix applied:
- Changed `from recommender import` to `from src.recommender import` in main.py
  to fix ModuleNotFoundError when running `python -m src.main`

### GitHub repo (Module 3):
https://github.com/Linchipa/ai110-module3show-musicrecommendersimulation-starter

---

## What's Next (Final Project — NOT STARTED)

### Goal
Extend MusicMatch into a full Applied AI System for the final project (21 pts).

### New repo to create
- Name: `musicmatch-applied-ai` (or similar professional name)
- Must be a NEW empty GitHub repo
- Mirror the existing MusicMatch repo into it using bare clone

### Commands to set up new repo (do these in terminal):
```bash
# Step 1: Clone bare copy of existing repo
git clone --bare https://github.com/Linchipa/ai110-module3show-musicrecommendersimulation-starter.git

# Step 2: Enter the bare folder
cd ai110-module3show-musicrecommendersimulation-starter.git

# Step 3: Mirror push to your new empty GitHub repo (replace URL with your new repo URL)
git push --mirror https://github.com/Linchipa/musicmatch-applied-ai.git

# Step 4: Go back and delete bare folder
cd ..
rm -rf ai110-module3show-musicrecommendersimulation-starter.git

# Step 5: Clone your new repo
git clone https://github.com/Linchipa/musicmatch-applied-ai.git

# Step 6: Enter the folder
cd musicmatch-applied-ai
```

### What to build for the final project:

#### New AI Feature: Claude API Integration
- Use the Anthropic Claude API to generate friendly natural language recommendations
- Instead of showing raw scores, Claude turns them into conversational responses
- Example output BEFORE: "Sunrise City - Score: 5.98, genre match (+3.0), mood match (+2.0)"
- Example output AFTER: "Hey! Based on your love for pop and happy vibes, Sunrise City is your top pick. The energy is just right and the mood is spot on!"

#### Reliability/Guardrails to add:
- Input validation (check genre/mood are valid strings, energy is between 0.0 and 1.0)
- Logging (record inputs, scores, and errors to a log file)
- Confidence scoring (normalize the score to a 0-100% confidence level)

#### Folder structure to create:
```
musicmatch-applied-ai/
├── assets/          ← system diagram and screenshots go here
├── data/
│   └── songs.csv
├── src/
│   ├── main.py
│   ├── recommender.py
│   └── ai_explainer.py   ← NEW: Claude API integration
├── tests/
│   └── test_recommender.py
├── logs/            ← NEW: logging goes here
├── README.md        ← needs full rewrite for final project
├── model_card.md    ← needs reflection on AI collaboration
└── PROGRESS.md      ← this file
```

### Rubric mapping (21 pts required):
| Points | Requirement | Plan |
|--------|-------------|------|
| 3pts | Identify base project | Document MusicMatch as base in README |
| 3pts | New AI feature | Claude API for natural language explanations |
| 3pts | Architecture diagram | Flowchart in /assets folder |
| 3pts | End-to-end demo | CLI with 2-3 profiles showing AI responses |
| 3pts | Reliability/guardrails | Input validation + logging + confidence score |
| 3pts | README documentation | Professional README with setup and examples |
| 3pts | Reflection | Update model_card.md with AI collaboration notes |

---

## Key Decisions and Reasoning

### Why genre weight is +3.0 (not +2.0 like the starter suggested)
We decided genre matters most because a rock fan almost never enjoys jazz even if the mood matches. Genre is the strongest predictor of whether someone will like a song.

### Why we expanded the CSV from 10 to 30 songs
The original 10 songs had 3 lofi songs and only 1 each of jazz and rock — biased toward lofi users. We expanded to 3 songs per genre across 10 genres to make it fair.

### Why latin was given extra attention
User noticed latin music is underrepresented in real music apps. We made sure to include 3 latin songs with different moods (happy, sad, intense).

### Key insight from testing
Even a perfectly fair algorithm produces biased results if the dataset is imbalanced. This was the user's biggest learning moment — data bias exists independently of algorithm bias.

### Future vision: friendly music personality
User wants MusicMatch to feel like a virtual music buddy that talks naturally rather than showing raw scores. This is the main motivation for adding the Claude API in the final project.

---

## How to Resume This Work

### In a new Claude conversation:
1. Open this file and paste its contents to Claude
2. Say: "This is my progress file. I am continuing my MusicMatch final project. Please read this and help me continue from where we left off."
3. Claude will have full context to continue

### To run the current project:
```bash
cd ai110-module3show-musicrecommendersimulation-starter
python -m src.main
```

### To run tests:
```bash
pytest
```
