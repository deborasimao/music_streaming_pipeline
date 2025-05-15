import json
import random
import time
from datetime import datetime
from faker import Faker
import uuid

fake = Faker()

actions = ['play', 'pause', 'skip', 'like', 'add_to_playlist']
artists = ['The Beatles', 'Taylor Swift', 'Drake', 'Beyoncé', 'Coldplay']
songs = ['Hey Jude', 'Shake It Off', 'Hotline Bling', 'Halo', 'Yellow']

def generate_event():
    return {
        "event_id": str(uuid.uuid4()),
        "user_id": fake.uuid4(),
        "song_id": random.choice(songs),
        "artist": random.choice(artists),
        "timestamp": datetime.utcnow().isoformat(),
        "action": random.choice(actions),
        "location": fake.city()
    }

def main():
    while True:
        event = generate_event()
        print(json.dumps(event))
        with open("streaming_data.json", "a") as f:
            f.write(json.dumps(event) + "\n")
        time.sleep(1)

if __name__ == "__main__":
    main()
