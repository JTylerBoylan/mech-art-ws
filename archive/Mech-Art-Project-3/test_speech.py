import sounddevice as sd
from scipy.io.wavfile import write
from openai import OpenAI

client = OpenAI()

def record_audio(duration=5, sample_rate=44100):
    """
    Record audio from the microphone for a given duration and sample rate.
    """
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='int16')
    sd.wait()  # Wait until recording is finished
    return recording, sample_rate

def save_audio_to_file(recording, sample_rate, filename='output.wav'):
    """
    Save the recording to a WAV file.
    """
    write(filename, sample_rate, recording)
    print(f"Audio saved to {filename}")

def transcribe_audio_with_whisper(filename='output.wav'):
    """
    Transcribe the audio file using OpenAI's Whisper API.
    """
    # Load the audio file and encode it
    audio_file= open(filename, "rb")

    # Send the audio file to the Whisper API for transcription
    transcript = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
        response_format="text"
    )
    
    return transcript

# Main process
if __name__ == "__main__":
    duration = 30  # Duration to record in seconds
    sample_rate = 44100  # Sample rate for the recording
    
    # Record and save audio
    recording, sr = record_audio(duration, sample_rate)
    audio_filename = 'output.wav'
    save_audio_to_file(recording, sr, audio_filename)
    
    # Transcribe audio
    transcription = transcribe_audio_with_whisper(audio_filename)
    print("Transcription:", transcription)
