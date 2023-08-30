import os
from pytube import YouTube
import moviepy.editor as mp
import speech_recognition as sr

# Function to download a YouTube video


def download_youtube_video(video_url, output_path):
    yt = YouTube(video_url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path=output_path)

# Function to convert video to audio


def video_to_audio(video_path, audio_path):
    video_clip = mp.VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)
    audio_clip.close()

# Function to convert audio to text


def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)  # Record the entire audio file
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition; {e}"


# YouTube video URL
youtube_url = "https://www.youtube.com/watch?v=FbIh98acWIw&t=6s"

# Set output paths
output_directory = "speech_recognition_output"
video_file = os.path.join(output_directory, "video.mp4")
audio_file = os.path.join(output_directory, "audio.wav")

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Download the YouTube video
download_youtube_video(youtube_url, video_file)

# Convert the video to audio
video_to_audio(video_file, audio_file)

# Convert the audio to text
result = audio_to_text(audio_file)

# Print the result
print("Text from audio:", result)
