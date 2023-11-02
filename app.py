from flask import Flask, render_template

from events import events_dict


app = Flask(__name__)


@app.route('/events', strict_slashes=False)
def events():
    return render_template('events.html', events=events_dict)


@app.route('/event/<id>', strict_slashes=False)
def event(id):
    event_dict = None
    for event in events_dict:
        if int(id) == int(event['id']):
            event_dict = event
            break
    
    if event_dict is None:
        return 'Event Not found'
        
    return render_template('event.html', event=event_dict)


@app.route('/event/<id>/purchase-ticket')
def buy_ticket(id):
    return render_template('ticket.html')


@app.route('/', strict_slashes=False)
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()