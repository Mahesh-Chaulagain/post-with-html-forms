import requests
from flask import Flask, render_template, request

app = Flask(__name__)

url = "https://api.npoint.io/74f87b8a4eaa06fd0a4a"
response = requests.get(url)
data = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        pass_item = "Successfully send your message"
        return render_template("contact.html", item=pass_item)



@app.route('/post/<int:num>')
def get_post(num):
    required = ""
    for post in data:
        if post['id'] == num:
            required = post

    return render_template("post.html", post=required)


if __name__ == "__main__":
    app.run(debug=True)
