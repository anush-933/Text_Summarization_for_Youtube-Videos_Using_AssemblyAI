from summarizer import TransformerSummarizer
from transcribe import get_youtube_transcribe

# perform transcription by getting youtube URL
URL = input('Enter Youtube URL :')
get_youtube_transcribe(URL)

#open the transcription txt file in read mode
text_file = open(r'C:\Users\Anushree\PycharmProjects\IITB_internship\Youtube_transcript.txt', 'r')
transcript = text_file.read()

# perform summarization using xlnet model
model = TransformerSummarizer(transformer_type="XLNet", transformer_model_key="xlnet-base-cased")
summary = ''.join(model(transcript, min_length=60))
print(summary)

# convert to text file
summary_text_file = open('SummaryTextFile.txt','w')
summary_text_file.write(summary)
summary_text_file.close()

