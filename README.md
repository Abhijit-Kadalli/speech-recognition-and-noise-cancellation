# Speech recognition and noise cancellation
Making this repo to make a speech recognition and then noise cancellation program using python

## Python modules
1. wave
2. pyaudio
3. matplotlib
4. numpy
5. pydub
6. requests
7. time
8. sys

## Speech input 
Input of speech using pyaudio and wave python modules. 
Using pydub we can convert the wav file to mp3 and add various tweeks to it like 
1. increasing volume in dB
2. repeating audio
3. adding fade in and fade out ...

## Analysis of input speech
Using the inputed audio we graph the audio as frames vs time 

## Transcribing the inputed speech
After recording the audio we use use assembly ai api to transcribe the inputed speech and save it to a text file
you can get ur api token here : https://www.assemblyai.com/
