!pip install pydub
from pydub import AudioSegment
from pydub.silence import split_on_silence

class AudioSpeechToText:

	MIN_SILENCE_LENGTH = 100
	SILENCE_THRESHOLD = -35
	KEEP_SILENCE = 50

	def audio_silence(self, audio_url, file_type):
		audio = AudioSegment.from_file(audio_url, format=file_type)
		chunks = split_on_silence(audio,
      min_silence_len=AudioSpeechToText.MIN_SILENCE_LENGTH,
      silence_thresh=AudioSpeechToText.SILENCE_THRESHOLD,
      keep_silence=AudioSpeechToText.KEEP_SILENCE
    )

		output = sum(chunks)
		output.export("/content/output.mp3", format="mp3")

audio_processor = AudioSpeechToText()
audio_processor.audio_silence("/content/tempo-de-aprender.mp3", "mp3")