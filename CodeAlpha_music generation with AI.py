import random
from music21 import stream, note, midi


def generate_random_music(num_notes=20):
    melody = stream.Stream()
    pitches = [
        'C4', 'D4', 'E4', 'F4',
        'G4', 'A4', 'B4',
        'C5', 'D5', 'E5', 'F5', 'G5'
    ]
    durations = [0.25, 0.5, 1.0]
    for _ in range(num_notes):
        pitch = random.choice(pitches)
        dur = random.choice(durations)

        melody.append(
            note.Note(pitch, quarterLength=dur)
        )
    midi_file = midi.translate.streamToMidiFile(melody)
    midi_file.open("generated_music.mid", "wb")
    midi_file.write()
    midi_file.close()

    print("Music generated and saved as 'generated_music.mid'")
if __name__ == "__main__":

    try:
        generate_random_music(num_notes=50)

    except Exception as e:
        print(f"Error: {e}")