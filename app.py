from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/short_url', methods=['POST'])
def shorten_url():
    long_url = request.form['long_url']
    
    # Create a Shortener object
    shortener = pyshorteners.Shortener()

    # Shorten the URL
    short_url = shortener.tinyurl.short(long_url)

    return render_template('results.html', short_url=short_url)

if __name__ == '__main__':
    app.run()