import requests
from api_secrets import API_KEY_ASSEMBLYAI
import sys

#upload file
upload_endpoint = "https://api.assemblyai.com/v2/upload"
filename = "D:\git\Speech-Recognition-Course\02-simple-speech-recognition\output.wav"
def read_file(filename, chunk_size=5242880):
    with open(filename, 'rb') as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

headers = {'authorization':API_KEY_ASSEMBLYAI}
response = requests.post(upload_endpoint, headers=headers, data=read_file(filename))

print(response.json())
# transcribe file

# poll

# save transcript