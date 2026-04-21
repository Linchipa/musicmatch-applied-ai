# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**MusicMatch**

---

## 2. Intended Use  

MusicMatch is designed to suggest songs that match a user's personal taste profile. It is intended for real music listeners who want personalized recommendations based on their preferred genre, mood, and energy level. The system assumes the user knows their own musical preferences — such as whether they enjoy chill lofi or intense rock — and that they are familiar with basic music descriptors like mood and genre in English.

---

## 3. How the Model Works  

MusicMatch looks at four key attributes of each song: genre, mood, energy level, and acousticness. Each attribute is compared against the user's stated preferences and awarded points based on how well it matches. Genre is weighted the highest (+3.0 points) because if a user already enjoys a particular genre, they are very likely to enjoy other songs in that same genre. Mood is second (+2.0 points) since the emotional feel of a song matters a lot to the listening experience. Energy closeness adds up to +1.0 point — the closer a song's energy is to the user's target, the more points it earns. Acoustic preference adds a small bonus (+0.5 points) if the user enjoys acoustic sound and the song qualifies.

Every song in the catalog competes for the highest score. Once all songs are scored, they are ranked from highest to lowest and the top 5 are presented to the user along with the reasons why each song was recommended.

In the final project version, a second AI layer was added on top of this scoring engine. After the top 5 songs are selected, the results are sent to Google Gemini along with the user's full taste profile. Gemini generates a friendly, conversational paragraph that explains the recommendations in plain language — like a knowledgeable friend rather than a calculator. Input validation runs before any scoring begins, and every recommendation session is logged to a file with a confidence percentage showing how strong the top match was.

---

## 4. Data  

The catalog contains 30 songs across 10 genres: pop, lofi, rock, jazz, ambient, synthwave, indie pop, latin, electronic, and acoustic. The original dataset had only 10 songs with an over-representation of lofi (3 out of 10 songs). To reduce this bias, we expanded the catalog to 30 songs with exactly 3 songs per genre, ensuring no single genre dominates the recommendations.

However, the dataset is still limited. Many popular genres are missing entirely such as R&B, hip-hop, country, classical, and reggae. The mood options are also narrow, covering only happy, chill, intense, moody, sad, relaxed, focused, and nostalgic. A real music platform would have millions of songs spanning hundreds of genres, moods, languages, and cultural backgrounds. Our catalog mostly reflects a Western, English-language perspective on music taste.

---

## 5. Strengths  

MusicMatch performs best when a user has a clear and specific taste profile. During testing with three distinct user profiles, the system consistently ranked the most relevant songs at the top. For the Pop/Happy profile, Sunrise City scored 5.98 and was an obvious correct match with genre, mood, and energy all aligning. For the Chill Lofi profile, Library Rain achieved a perfect score of 6.50 hitting every scoring category including the acoustic bonus. For the Intense Rock profile, Storm Runner ranked first at 5.99 correctly identifying the only song that matched genre, mood, and high energy together.

The system also handles partial matches well. Songs from other genres can still appear in the top 5 if their mood and energy are a strong fit, as seen with Pixel Rush (electronic) appearing in the Pop/Happy results because its mood and energy were a perfect match. This shows the scoring logic is balanced and not purely dominated by genre.

---

## 6. Limitations and Bias 

MusicMatch has several limitations worth acknowledging. First, users whose favorite genre is not well represented in the catalog will receive unsatisfying results. With only 3 songs per genre and 10 genres total, the system has very little variety to offer within any single genre. A user who loves R&B or hip-hop will find no matches at all since those genres are missing entirely.

Second, the system ignores many features that matter deeply to real listeners. Lyrics are not considered at all. For example, a user might enjoy the rhythm of reggaeton but dislike certain songs due to their lyrical content. The system would recommend those songs anyway because it only sees genre and energy. Artist popularity, release date, and whether a song feels fresh or classic are also completely absent from the scoring.

Third, MusicMatch can create a filter bubble by repeatedly recommending songs that are very similar to what the user already likes. However, the top 5 format gives the user some freedom to explore partial matches from other genres that appear lower in the rankings, which slightly reduces this effect.

---

## 7. Evaluation  

MusicMatch was evaluated by running three distinct user profiles through the recommender: Pop/Happy (genre: pop, mood: happy, energy: 0.8), Chill Lofi (genre: lofi, mood: chill, energy: 0.35, likes acoustic), and Intense Rock (genre: rock, mood: intense, energy: 0.9). For each profile we observed the top 5 results and compared them against what a real listener would expect.

The results largely matched expectations. Each profile correctly surfaced its closest genre and mood matches at the top. The most surprising finding was that songs from completely different genres could still rank in the top 5 purely on mood and energy alignment. Pixel Rush, an electronic song, appeared in the Pop/Happy top 5 because its mood was happy and its energy was a perfect match at 0.80. This was unexpected but actually makes musical sense.

The Chill Lofi profile produced the most satisfying results, with Library Rain achieving a perfect score of 6.50. The Intense Rock profile revealed a limitation — after the 3 rock songs were ranked, the system had to pull from other genres to fill the remaining spots, showing how a small catalog directly impacts recommendation quality.

---

## 8. Future Work  

There are several directions MusicMatch could grow in future versions. First, expanding the catalog to include more genres such as R&B, hip-hop, country, and classical would significantly reduce bias and serve a wider range of listeners. Ideally every genre would have enough songs to fill a full top 5 without pulling from unrelated genres.

Second, adding more scoring metrics would make recommendations more accurate. Features like lyrical content, artist popularity, release date, and tempo ranges would help the system understand taste on a deeper level beyond just genre and energy.

Third, the system could address the filter bubble problem by occasionally introducing songs from outside the user's preferred genre when the mood and energy are a strong match. This would encourage discovery rather than always reinforcing the same taste.

Finally, adding a user-facing interface — such as a simple web form — would make MusicMatch accessible to people who are not comfortable running Python from the command line. The current CLI-only design limits who can actually use the system.

---

## 10. AI Collaboration

**How AI was used during this project**

Claude (Anthropic's AI coding assistant) was used throughout the development of this final project as a collaborative partner. It helped design the structure of `ai_explainer.py`, write the Gemini prompt, implement input validation in `guardrails.py`, and wire all the components together in `main.py`. Rather than just generating code, Claude explained what each piece did and why before writing it, which helped with understanding the design decisions behind the system.

**One helpful suggestion**

The most helpful suggestion was the structure of the Gemini prompt in `ai_explainer.py`. Claude recommended including not just the song titles but also the specific reasons each song scored well (genre match, mood match, energy closeness) so that Gemini had enough context to generate a specific and accurate response. Without those reasons in the prompt, Gemini would produce generic music commentary instead of a personalized explanation tied to the actual recommendations.

**One flawed suggestion**

Early in the project, Claude recommended using the Anthropic API (Claude's own API) instead of Google Gemini. This was incorrect for this course — CodePath AI110 uses Gemini throughout, and students already had Gemini API keys set up from Module 4. Following Claude's suggestion led to confusion about API keys and wasted time before the instructor clarified that Gemini was the right choice. This was a reminder that AI assistants can be confidently wrong, and checking suggestions against course requirements or asking an instructor is always worth doing.

**What this taught me about AI collaboration**

Working with an AI assistant is not the same as having the AI do the work. The best results came from understanding each suggestion before accepting it, asking why before saying yes, and catching mistakes early — like the wrong API recommendation — rather than blindly following along. AI is a powerful tool but it requires an informed human in the loop to catch errors and make final decisions.

---

## 9. Personal Reflection  

The biggest learning moment in this project was realizing that data can be biased even when the algorithm itself is fair. A perfectly written scoring function still produces unfair results if the catalog does not represent all users equally. This was eye-opening because it shifts responsibility from just writing good code to also thinking critically about the data behind it.

Building MusicMatch changed the way I think about apps like Spotify and TikTok. It made me more aware of the choices engineers make when designing these systems and how those choices affect real people. Building an honest system means not just making it work, but making sure it works fairly for everyone.

The most surprising insight was that even a simple algorithm can feel like a real recommendation when it is designed with the user in mind. Just like programming languages help us write better code instead of working in 0s and 1s, we can build tools that connect and interact with users in a more human way. This project made me reflect a lot about user experience and how engineering is not just about logic but also about empathy.
