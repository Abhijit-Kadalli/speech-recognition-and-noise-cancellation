from api_communication import *
import sys

filename = sys.argv[1]

audio_url = upload(filename)
save_transcribe(audio_url, filename)