import os
import io
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

client = speech.SpeechClient()

file_name = os.path.join(
    os.path.dirname(__file__),
    'wudi.flac')

with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=48000,
    language_code='cmn-Hans-CN')

# Detects speech in the audio file
response = client.recognize(config, audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))
    print('Confidence: {}'.format(result.alternatives[0].confidence))
#encoding = enums.RecognitionConfig.AudioEncoding.FLAC
#sample_rate_hertz = 48000
#language_code = 'cmn-Hans-CN'
#config = {'encoding': encoding, 'sample_rate_hertz': sample_rate_hertz, 'language_code': language_code}
#uri = 'C:\\Users\\lorwaysan\\Desktop\\wudi.flac'
#audio = {'uri': uri}
#response = client.recognize(config, audio)
#input()