# AnushreeK_IITB_ML_Internship_Assignment_Dec2022
Problem statement 4 - Panel Discussion Summarization

APPROACH:

The project consists of 2 python files 
          
          1. transcribe.py      
          2. textsummarize.py
          
In transcribe.py, the following approch is done
		
    STEP 1: The function get_youtube_transcribe() will use URL to get audio of the video only and is downloaded in '.mp4' file. (Takes Time)
    STEP 2: Connects to AssemblyAI platform with authorization key
    STEP 3: Uploads the '.mp4' file 
    STEP 4: The transcript returned as json type in variable 'transcript_output_response'
    STEP 5: Convert the json to '.txt' 
    
In textsummarize.py, the following approach is done

    STEP 1: Gets Youtube Url from user to get transcript by using 'transcribe.py' as python module 
    STEP 2: The text file from 'STEP 5' in transcribe.py is used to read and stored in variable 'transcript'
    STEP 3: Performs summarization on this file using xlnet model and prints the summary(Takes Time)
    STEP 4: The summary is written in another text file.
		
![image](https://user-images.githubusercontent.com/82230179/206616612-b6cbc600-92fe-4a71-9b99-84488f4f9d5d.png)

ABOUT XLNET:

The XLNet model was proposed in XLNet: Generalized Autoregressive Pretraining for Language Understanding by Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell, Ruslan Salakhutdinov, Quoc V. Le. XLnet is an extension of the Transformer-XL model pre-trained using an autoregressive method to learn bidirectional contexts by maximizing the expected likelihood over all permutations of the input sequence factorization order. It overcomes the drawbacks of BERT model.

For more: https://huggingface.co/xlnet-base-cased

HOW TO RUN THE CODE:

       Run textsummarization.py file. It asks for URL. Enter the URL.
       SAMPLE INPUT:
       Enter Youtube URL : https://youtu.be/OkR7Ddl0DKA
       
       SAMPLE OUTPUT:
       Careers in Tech - Panel Discussion.mp4   //First output 
       Youtube_transcript.txt                        //Second Output
       SummaryTextFile.txt                   //Third Output
 
 HOW TO TEST THE CODE:
   
 Input different URLs of panel discussion videos.
