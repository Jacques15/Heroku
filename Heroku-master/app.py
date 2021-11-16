from flask import Flask,flash,redirect,request, url_for, render_template,jsonify
#from azure.cognitiveservices.search.customsearch import CustomSearchClient
#from msrest.authentication import CognitiveServicesCredentials

app = Flask(__name__)

def remove_punctuation(word):
    for x in word:
        # Checks every letter in a word to see if it is punctuation by looking at its ASCII number
        if ((ord(x) >= 33 and ord(x) <= 47) or (ord(x) >= 58 and ord(x) <= 64) or (ord(x) >= 91 and ord(x) <= 96) or (ord(x) >= 123 and ord(x) <= 127)): 
            word = word.replace(x," ") # If word is punctuation, replace with space
    return word

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        user_input = request.form["input"]
        user_input = remove_punctuation(user_input)
        return render_template('index.html',user_input=user_input)
    else:
        return render_template('index.html')

@app.route("/foo")
def foo():
    return jsonify({"hello": "world", "from": "foo"})

if __name__ == '__main__':
    app.run(debug=True)