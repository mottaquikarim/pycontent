<img src="https://s3.amazonaws.com/python-ga/images/GA_Cog_Medium_White_RGB.png"/>

# Flask 1: Intro to Flask

<!-- duration: 30 min -->

## Learning Objectives

In this lesson, students will:

* Write a basic Flask application.

**Make sure you have Flask installed!**

## Intro

<img src="https://qph.fs.quoracdn.net/main-qimg-cd83cf9ee7ad51b8af4d0c4d5220f534.webp" width="100px"/>

Some quick notes about Flask:

- It's a Python micro web framework.
- It can create and write the entire back-end in Python!
- It can do small tasks (e.g., create a microblog or stand up a simple API).
- It can do complex tasks (e.g., Pinterest's API or create a Twitter clone).


<aside class="notes">

**Talking Points:**

- Flask is classified as a microframework because it does not require particular tools or libraries.
- Open the lesson by describing what students are going to do (build a Flask app), and why this is so exciting ("We are using Flask to actually put your stuff on the internet!").
- Why do we use a lighter web framework like Flask?
- Talk about how these sites work (lots of interaction and data) and why it is helpful to use Flask for these (get to focus on the interactivity/data and not just getting the thing up on to the internet and staying there).

</aside>

---

## Flask Syntax

How?

We just make a normal Python app.

It looks like:

```python
# Import Flask class from flask library. (Note the upper/lowercase convention.)
from flask import Flask

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

# The default URL ends in / ("my-website.com/").
# Could be instead "my-website.com/about" or anything - more on this later.
@app.route('/')

# Function that returns the page: Display "Hello, World!"
def index():
  return 'Hello, World!'

# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=True)

```


<aside class="notes">


**Teaching Tips:**

- Walk through this line by line.
- The code includes comments for students' reference, but be sure to still talk through it. There's a lot more to say than what's written!
- Give URL examples — pull up websites.

**Talking Points:**

*<Note: This is copied from the Flask docs.>*

- First we imported the Flask class.
- Next, we create an instance of this class. We use `__name__` so that Flask knows where to look for templates, static files, and so on.
- We then use the `route()` decorator to tell Flask what URL should trigger our function.
- The function is given a name, which is also used to generate URLs for that particular function and returns the message we want to display in the user’s browser.

</aside>

---

## We Do: Let's Try!

We'll run the Flask app like any other app.

- We need to install Flask!
  - `pip install flask`

Create a file called `my_website.py`.

Start with:

```python
# Import Flask class from flask library.
from flask import Flask
```


<aside class="notes">

**Talking Points:**

- Flask (and lots of web frameworks) can be launched on the command line, giving developers more control and clarity into what is going on.
- Set global variable (so Flask knows where our main application logic lives).

**Teaching Tips:**

- Make sure everyone has done these steps!
- If there are difficulties with `pip`, check `sudo`.
- Demo these so students have the idea, then let them experiment on their own.
- For more advanced students, write longer scripts in the `index()` function, or, if time, assign them the task.
</aside>

---

## We Do: The Main Flask App

Let's add:

```python
# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

# The default URL ends in / ("my-website.com/").
@app.route('/')

# Function that returns the page: Display "Hello, World!"
def index():
  return 'Hello, World!'

# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=True)
```


<aside class="notes">

**Teaching Tip:**

- Continuously walk through the code.
</aside>


---

## We Do: Flask App — Try it!

Run the app like normal:

`python my_website.py`

Go to:

`http://localhost:5000/`

You made a web app!

Let's change the string:

```python
def index():
  # The "return" determines what's displayed.
  return 'Hello, World!'
```


<aside class="notes">

**Teaching Tip:**

- Change around what's returned in `index()`, so they can see that that's what makes the display.

</aside>

---


## I Do: Displaying the App

It's just Python — we can write any code.

- But `return` essentially just takes strings.

```python
def index():
  my_list = ["Hey", "check", "this", "out"]
  return my_list[0] # Works!
```

Conversely:

```python
def index():
  my_list = ["Hey", "check", "this", "out"]
  return my_list # WON'T WORK
```


<aside class="notes">

**Teaching Tips:**

- Change around what's returned in `index()` in a more advanced way.
- They can follow along if they'd like.
</aside>


---

## We Do: Flask Variations

`app` and `index` are just naming conventions.

- `def index():` could be `def monkey():`.
- `app` could be `guitar`.
    - Be sure to change it in all places!

But, naming variables sensibly is important!

```python
from flask import Flask

guitar = Flask(__name__)
@guitar.route('/')

def monkey():
  return 'Hello, World!'

if __name__ == '__main__':
    guitar.run(debug=True)
```


<aside class="notes">

**Teaching Tip:**

- Show this.
</aside>


---

## Flask History

Let's back up. Where did Flask come from?

- Before 2010:
    - No easy method for Python websites.
- 2010:
    - A few developers built Flask to fix this.

Flask is built on two libraries:

- *Werkzeug*:
    - Interfaces with the web.
    - Helps handle request and connections.
- *Jinja*:
    - We'll be using this later!
    - We can write templates for all pages across our web app.


<aside class="notes">

**Teaching Tips:**
- Some students might not care about history, but go over it for those who do.
- Don't spend too much time on the libraries — we're hitting Jinja later!

**Talking Points:**

* Around 2010, a group of open-source Python developers release the first version of Flask!.
* Before this, there was no easy way to use Python on the internet/for web apps.
* Flask is built using two libraries (already written bundles of code).
1. *Werkzeug* is a library to interface with the web. It helps to handle request and connections.
2. *Jinja* is a templating engine, which lets us write an HTML file once and then apply that file to all of our site.
</aside>


---

## Summary: Flask

- A Python micro web framework
- Developed in 2010

Looks like this:

```python
# Import Flask class from flask library.
from flask import Flask

# Initialize an instance of the Flask class.
app = Flask(__name__)

# The default URL ends in / ("my-website.com/").
@app.route('/')

# Function that returns the page: Display "Hello, World!"
def index():
  return 'Hello, World!'

# Run the app when the program starts!
if __name__ == '__main__':
    app.run(debug=True)
```

<aside class="notes">

**Teaching Tip:**

- Be sure everyone has a basic Flask app at the end and understands why.
</aside>

---

## Additional Reading

- [Flask Documentation](http://flask.pocoo.org/docs/0.11/)
- [A Flask Tutorial to Follow Along With](https://github.com/miguelgrinberg/flask-pycon2014)
- [The Flask Mega-Tutorial](http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)
- [A Great Guide to Those Weird "Decorators"](http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/)