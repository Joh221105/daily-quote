from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_daily_quote():
    url = 'https://zenquotes.io/api/today'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        quote_data = data[0]
        quote = quote_data.get('q', 'No quote available.')
        author = quote_data.get('a', 'Unknown author')
        return f'"{quote}" - {author}'
    else:
        return 'Failed to retrieve quote'

@app.route('/')
def home():
    quote = get_daily_quote()
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)