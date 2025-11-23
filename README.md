# SPELLCHECKER

## SpellChecker Application
A simple and efficient console-based spell checking tool built in Python that helps you identify and correct spelling mistakes in your text.
## Overview
The Spell Checker Application is a Python-based tool designed to automatically detect and correct spelling errors in plain text. Using the pyspellchecker library, it provides quick and reliable spelling corrections through an intuitive command-line interface. Perfect for writers, students, and anyone who needs to quickly proofread text without leaving the terminal.

## Features
- Real-time Spell Checking:  Instantly identifies misspelled words as you type

- Automatic Corrections:  Suggests the most probable corrections for misspelled words

- Interactive Console Interface:  Simple text-based interface that's easy to use

- Continuous Operation:   Check multiple texts in a single session without restarting

- Detailed Feedback:  Shows both the original misspelled word and its correction

- Cross-Platform Compatibility:   Works on any system with Python installed


## Technologies & Tools Used
- `Python 3.x `- Core programming language

- pyspellchecker - Spelling correction library

- Backend: Python, Flask

- Frontend: HTML, CSS, JavaScript

- Spell Checking: Custom SpellCheckerApp module

- API: RESTful JSON API

- Templating: Jinja2 templates


## Installation & Setup
**Prerequisites**
-  `Python 3.6` or higher installed on your system

- `pip` (Python package manager)

**Step-by-Step Installation**
1. Clone the Project
2. Install Required Dependencies
```bash
pip install pyspellchecker
```
3. Create Virtual Environment (Recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```
4. Install Dependencies
```bash
Install Dependencies
```

5. Project Structure
*Ensure your project has the following structure:*
```bash
spellchecker-project/
├── app.py
├── spellchecker_app.py
├── templates/
│   └── index.html
└── spellchecker_app/
    └── static/
        ├── css/
        └── js/
```
6. Run the Application
```bash
python app.py
```
7. Access the Application
Open your web browser and navigate to:
```bash
http://localhost.0.0.1:5000
```




## Instructions for Testing
**Testing the Web Interface**
1. Access the Main Page
 - Open http://localhost.0.0.1:5000 in your browser
 - You should see a text area and a "Check" button
2. Test Spell Checking
 - Enter text with intentional spelling errors:
 ```bash
 Ths is a testt sentense with som spelling erors.
 ```
- Click "Check" button

 - Observe the corrected text in the "Corrected Text" section

- Check the "Corrections" section for a list of changes made

3. Verify Features

- Check that corrections are properly displayed

- Verify the corrections list shows original → corrected format

- Test with different text inputs





`

##  Troubleshooting
 **Common Issues**

  - ```ModuleNotfoundError:``` No Module Named 'flask'  
     Solution: Run ```Pip Install Flask```  
- Port Already In Use 

  Solution: Change The Port In ```App.py ```Or Stop Other                   Applications Using Port 5000  
- Template Not Found  
  Solution: Ensure The ```Templates``` Directory Exists With ```Index.html ``` 
- 404 Errors  
  Solution: Check That All Routes Are Properly Defined In ```App.py```
## Getting Help 
**If you encounter issues:**

 1. Check that all dependencies are installed
 2. Verify the project structure matches the expected layout
 3. Ensure Python version is 3.7+  
 4. Check the browser console for JavaScript errors
 5. Look at the Flask terminal output for backend errors
## License 

This project is for educational purposes. Feel free to modify and distribute as needed.
##

Happy Spell Checking! ✨
