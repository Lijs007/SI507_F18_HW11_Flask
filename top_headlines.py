from flask import Flask, render_template
from secrets import api_key
import json
import requests

app = Flask(__name__)

@app.route('/user/<nm>')
def hello_name(nm):
    url = 'http://api.nytimes.com/svc/topstories/v2/technology.json?api-key={}'.format(api_key)
    resp = json.loads(requests.get(url).text)
    list = []
    for i in range(5):
        list.append(resp['results'][i]['title'] + ' ({})'.format(resp['results'][i]['url']))
    return render_template('user.html', name=nm, headerlist=list)

@app.route('/')
def welcome():
    return render_template('default.html')

if __name__ == '__main__':
    app.run(debug=True)