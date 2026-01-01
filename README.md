# AI-Powered Meeting Assistant

Hey there! Welcome to the AI-Powered Meeting Assistant project. This is a fun little tool that helps make meetings easier by turning spoken words into text and pulling out the key points. No more scrambling to take notes – let AI do the heavy lifting!

## What's the Problem?
Meetings can be a drag. People talk a lot, and it's hard to keep up with everything said. Taking notes manually is time-consuming, and you might miss important details. We need a smarter way to capture and summarize conversations, especially in long or complex discussions.

## How We Solve It
Our solution uses AI to listen to audio recordings of meetings, convert speech to text, and then analyze that text to highlight the main ideas. It's like having a super-smart assistant who never gets tired and always pays attention.

The app is built with a simple web interface where you upload an audio file, and it gives you back a summary of the key points. Easy peasy!

## Key Features
- **Speech-to-Text**: Turns audio into written words using advanced AI models.
- **Key Points Extraction**: Analyzes the transcript to pull out the most important bits.
- **User-Friendly Interface**: Upload files and get results quickly with Gradio.
- **Customizable**: You can tweak settings for different needs.

## Requirements
To run this project, you'll need:
- Python 3.8 or higher
- A computer with a decent CPU/GPU (for faster processing)
- Internet connection (for downloading models and API calls)
- IBM Watsonx account (for the LLM part – it's free to try)

### Dependencies
We use these libraries – install them with pip:
- torch
- transformers
- gradio
- ibm-watson-machine-learning
- requests (for downloading sample files)

## Installation
1. Clone this repo to your computer.
2. Open a terminal and go to the project folder.
3. Install the required packages: `pip install -r requirements.txt`.
4. Set up your IBM Watsonx credentials in the code (check the scripts for details).
5. Run the app: `python speech_analyzer.py`

That's it! The app will start a local web server, and you can access it in your browser.

## How to Use
1. Open the app in your browser (usually at http://localhost:7860).
2. Upload an audio file (like an MP3 of your meeting).
3. Hit the button, and wait a bit – AI is working!
4. Get your summary of key points back as text.

Try it with the sample audio file we download in one of the scripts.

## How the Tools Are Implemented
Let's break it down simply:

### Speech-to-Text with Whisper
We use OpenAI's Whisper model, which is great at understanding spoken language. In the code, we load the "whisper-tiny.en" model (a lightweight version for English). It processes audio in chunks to handle long files without crashing. The result? A clean transcript of what was said.

### Analyzing with LLM
For the smart part, we use IBM's Watsonx service with the Llama-3 model. It's a powerful language model that can understand and summarize text. We feed it the transcript and ask it to list key points. It's like asking a friend to summarize a long story.

### The Interface with Gradio
Gradio makes it all user-friendly. It's a library that turns Python functions into web apps. Upload audio, process it, and show the results – no coding needed on the user's end.

### Putting It Together
In `speech_analyzer.py`, we chain it all: transcribe the audio, then analyze the text. Other files are simpler versions or tests, like `speech2text_app.py` for just transcription.

## Project Structure
- `speech_analyzer.py`: The main app with full features.
- `speech2text_app.py`: Just for transcription.
- `simple_llm.py`: Testing the LLM.
- `simple_speech2text.py`: Basic speech-to-text.
- `pre_project.py`: Examples and setup notes.
- `hello.py`: A quick Gradio test.
- `simple_speech2text_01.py`: Downloads a sample audio file.

## Contributing
Got ideas? Feel free to fork the repo and make changes. Pull requests are welcome – let's make this even better!

## License
This project is open-source. Use it freely, but give credit where due.

Enjoy your smarter meetings! 🚀
