# ai_meeting_assistant_python
Python project to use meeting transcripts and create MOM, action and task list.

##Features
- Extract actions items
- Detect deadlines with NLP
- Generate meeting summaries
- Stores meetings locally

  ##Tech Stack
  - Python
  - #spaCy (NLP) -- removed for Issue #1 - doesnt support python 3.14 or greater
  - re
  - Dateparser
 
##How to Run
#1. Install dependencies
pip install -r requirements.txt
#python -m spacy dpwnload en_core_web_sm

#2. Run
python app.py
  
