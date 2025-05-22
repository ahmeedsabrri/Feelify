import os
import requests
import json
# from dotenv import load_dotenv

# Load .env variables (if not already loaded in your Django settings)
# load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../.env'))

def get_playlist_tracks_from_ai(mood, genres, artists, playlist_name, num_tracks=20):
    # api_key = os.environ.get("OPEN_ROUTE_API_KEY")
    # if not api_key:
    #     raise Exception("OPEN_ROUTE_API_KEY not set in environment.")
    api_key = "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"
    # Build the prompt
    prompt = (
        f"Generate a list of {num_tracks} {mood} songs for a playlist called '{playlist_name}'. "
        f"The genres should be {', '.join(genres)}. "
        f"Include songs by {', '.join(artists)} if possible. if no artists provided use genres to find theme "
        "Return only a JSON array of track names and artists, like this: "
        '[{"track": "Song Name", "artist": "Artist Name"}, ...]'
    )

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "meta-llama/llama-4-maverick:free",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code != 200:
        raise Exception(f"OpenRouter API error: {response.status_code} {response.text}")

    # Extract and parse the AI's reply
    ai_reply = response.json()["choices"][0]["message"]["content"]
    try:
        tracks = json.loads(ai_reply)
    except Exception:
        # If the AI returns extra text, try to extract the JSON part
        import re
        matches = re.findall(r'\[\s*{.*?}\s*\]', ai_reply, re.DOTALL)
        if matches:
            tracks = json.loads(matches[0])
        else:
            raise Exception("AI response is not valid JSON:\n" + ai_reply)
    return tracks

# Example usage:
tracks = get_playlist_tracks_from_ai(
    mood="i feel sad",
    genres=["rap","rock"],
    artists=[],
    playlist_name="My playlist",
    num_tracks=20
)
print(tracks)