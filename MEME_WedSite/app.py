from flask import Flask,render_template
import json
import requests

app = Flask(__name__)

def get_memes():
    url="https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    memes_large = response["preview"][-2]
    subreddits = response["subreddit"]
    return memes_large,subreddits

@app.route('/')
def  index():
    meme_pic,subreddits = get_memes()
    return render_template('index.html',meme_pic=meme_pic,subreddits=subreddits)

if __name__ == '__main__':
    app.run(debug=True)