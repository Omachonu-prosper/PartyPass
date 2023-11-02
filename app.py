from flask import Flask, render_template

app = Flask(__name__)


@app.route('/events', strict_slashes=False)
def events():
    return render_template('events.html')


@app.route('/event/<id>', strict_slashes=False)
def event(id):
    return render_template('event.html')


@app.route('/event/<id>/purchase-ticket')
def buy_ticket(id):
    return render_template('ticket.html')


@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()