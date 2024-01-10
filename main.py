import requests
import smtplib
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

app = Flask(__name__)

load_dotenv()

my_email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

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
        name = request.form["username"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]

        # send email
        with smtplib.SMTP("smtp.gmail.com") as connection:  # create an object from SMTP class
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="maheshchaulagain8@gmail.com",
                                msg="Subject:Hello\n\n"
                                    f"Name:{name}\n"
                                    f"Email:{email}\n"
                                    f"Phone:{phone}\n"
                                    f"Message:{message}")
        connection.close()

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
