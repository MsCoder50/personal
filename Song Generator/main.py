import os
import magenta.music as mm
from magenta.models.music_vae import TrainedModel
from magenta.models.music_vae.configs import configs
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Your lyrics
lyrics = """
In fields of dreams where love does bloom,
There wanders one, fair as the moon.
Her eyes, two stars, they gleam so bright,
Guiding hearts through the darkest night.

With every step, she paints the air,
A masterpiece beyond compare.
Her laughter, like a gentle stream,
Flowing through meadows, a blissful dream.

To conquer her heart, a noble quest,
Requires courage, at its behest.
So let me weave a verse divine,
To make her heart and soul entwine.

Oh maiden fair, with grace untold,
Your beauty shines, a sight to behold.
In your presence, my spirit soars,
Lost in the melody of your whispered chords.

I offer words, sincere and true,
A symphony of love meant just for you.
For in your smile, I find my light,
A beacon shining through the night.

So take my hand, and walk with me,
Together, we'll explore the sea.
Let's chase the stars, let's touch the sky,
Forever bound, you and I.

In this dance of fate, let love prevail,
As we write our story, a timeless tale.
For in your arms, I've found my home,
Forevermore, together we'll roam.
"""

# Load the pre-trained MusicVAE model
checkpoint = '~/magenta_models/cat-mel_2bar_big'
model = TrainedModel(configs['cat-mel_2bar_big'], batch_size=4, checkpoint_dir_or_path=checkpoint)

# Generate a 2-bar melody
melody_sequence = model.sample(n=1, length=32)

# Save the generated melody as a MIDI file
mm.sequence_proto_to_midi_file(melody_sequence[0], 'generated_melody.mid')

# Convert MIDI to WAV using fluidsynth
soundfont_path = '/usr/share/sounds/sf2/default-GM.sf2'
os.system(f"fluidsynth -ni {soundfont_path} generated_melody.mid -F generated_melody.wav -r 44100")

# Save lyrics to speech
tts = gTTS(text=lyrics, lang='en')
tts.save('lyrics.mp3')

# Load the generated melody and lyrics
melody_audio = AudioSegment.from_wav('generated_melody.wav')
lyrics_audio = AudioSegment.from_mp3('lyrics.mp3')

# Combine the melody and lyrics
# You may need to adjust the volume and timing to sync properly
combined_audio = melody_audio.overlay(lyrics_audio)

# Save the final song
combined_audio.export('final_song.wav', format='wav')

# Play the final song
play(combined_audio)
