from pytube import YouTube
from pytube.cli import on_progress
import os
import requests
from time import sleep


def get_youtube_transcribe(URL):
    video = YouTube(URL,n_progress_callback=on_progress)
    yt = video.streams.get_audio_only()
    yt.download()

    current_dir = os.getcwd()

    for file in os.listdir(current_dir):
        if file.endswith(".mp4"):
            mp4_file = os.path.join(current_dir, file)
    filename = mp4_file

    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    headers = {'authorization': '4527be6845394eb7992b05b15a******'}
    response = requests.post('https://api.assemblyai.com/v2/upload',
                             headers=headers,
                             data=read_file(filename))
    audio_url = response.json()['upload_url']
    endpoint = "https://api.assemblyai.com/v2/transcript"
    json = {
        "audio_url": audio_url
    }

    headers = {
        "authorization": '4527be6845394eb7992b05b15a******',
        "content-type": "application/json"
    }

    transcript_input_response = requests.post(endpoint, json=json, headers=headers)
    transcript_id = transcript_input_response.json()["id"]
    endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
    headers = {
        "authorization": '4527be6845394eb7992b05b15a6768ff',
    }
    transcript_output_response = requests.get(endpoint, headers=headers)

    while transcript_output_response.json()['status'] != 'completed':
        sleep(5)
        transcript_output_response = requests.get(endpoint, headers=headers)

    yt_txt = open('Youtube_transcript.txt', 'w')
    yt_txt.write(transcript_output_response.json()["text"])
    yt_txt.close()


