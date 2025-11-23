
from flask import Flask, request, jsonify, render_template
from spellchecker_app import SpellCheckerApp

# Use the project `templates/` directory and keep static files under the
# previously-created `spellchecker_app/static` folder.
app = Flask(__name__, template_folder='templates', static_folder='spellchecker_app/static')
sc = SpellCheckerApp()


@app.route('/api/correct', methods=['POST'])
def correct():
    data = request.get_json() or {}
    text = data.get('text', '')
    corrected_text, corrections = sc.correct_text(text)
    return jsonify({'corrected_text': corrected_text, 'corrections': corrections})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
