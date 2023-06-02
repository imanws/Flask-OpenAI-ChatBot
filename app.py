from flask import Flask, render_template, request, jsonify
import openai
app = Flask(__name__)

#OpenAI API KEY
openai.api_key = '.....'

#HOME Page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']

    response  = openai.ChatCompletion.create(
        messages=[{"role": "user", "content":message}],
        model = "gpt-3.5-turbo",
        temperature = 0.7,max_tokens = 4000)
   
    reply = response.choices[0].message["content"].encode('utf-8')

    return (reply.decode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True)
