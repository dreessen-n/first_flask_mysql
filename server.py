from flask import Flask, render_template, render_template, request, redirect, session
from friend import Friend

app = Flask(__name__)
app.secret_key="Put something in here"

@app.route('/')
def index():
    """Rendor the home page"""
    friends = Friend.get_all()
    print(friends)
    return render_template('index.html', all_friends = friends)

@app.route('/create_friend', methods=["POST"])
def create_friend():
    """Add friend to db"""
    # First we make a data dict from request form
    # The keys in data need to match up exactly with variables in query string
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'occ': request.form['occ']
    }
    # We pass the data dict into the save method from Friend class
    Friend.save(data)
    # Do not forget to redirect after saving to db
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    """Error handling for page not found"""
    return f'Sorry! No response. Try again.'

# Ensure file is run directly and not from different
# module, and run localhost on port 5001 for mac
if __name__=="__main__":
    app.run(host='localhost', port=5001, debug=True)
