# AI Story / Content Generator

## Project Overview
The AI Story / Content Generator is a Python application that uses the Google Gemini API to generate creative content based on user-provided topics or keywords.

Users can generate short stories, blog posts, and poems by selecting their preferred genre and tone.

## Features
- Accepts topics or keywords from users.
- Generates short stories, blog posts, and poems.
- Supports genre selection, such as Fantasy, Mystery, and Adventure.
- Supports tone selection, such as Funny, Inspirational, and Emotional.
- Allows users to regenerate content with the same settings.
- Saves generated content to a text file.

## Technologies Used
- Python
- Google Gemini API
- `google-genai` Python SDK

## How to Run

1. Install Python.
2. Install the required package:

   `pip install google-genai`

3. Set your Gemini API key as an environment variable:

   PowerShell:
   `$env:GEMINI_API_KEY="YOUR_API_KEY"`

4. Run the application:

   `python main.py`

## Project Files
- `main.py` — Main application code.
- `README.md` — Project documentation.
- `generated_content.txt` — Saved AI-generated content (created when the user saves an output).

## Security
Keep your Gemini API key private. Never store it in the source code or upload it to GitHub.

## Learning Outcomes
This project provides practical experience with Python, API integration, prompt engineering, creative content generation, and file handling.
