from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
debug = DebugToolbarExtension(app)

@app.route('/')
def story():
    """show form"""
    return render_template("select-story.html", stories=stories.values())

@app.route('/questions')
def questions():
    """form that asks for fill-ins"""
    story_id = request.args['story_id']
    story = stories[story_id]
    prompts = story.prompts
    return render_template('questions.html', story_id=story_id, title=story.title, prompts=prompts)

@app.route('/story')
def reveal():
    """reveal story"""
    story_id = request.args['story_id']
    story = stories[story_id]
    text = story.generate(request.args)
    return render_template('story.html', title=story.title, text=text)
