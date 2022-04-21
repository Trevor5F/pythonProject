from flask import Flask, render_template, request
from utils import *

app = Flask(__name__)

posts = get_posts_all()


@app.route('/')
def index():
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:postid>')
def profile(postid):
    comments = get_comments_by_post_id(postid)
    post = get_post_by_pk(postid)
    return render_template('post.html', comments=comments, post=post)


@app.route('/search/')
def search_post():
    search_word = request.args.get('s')
    querys = search_for_posts(search_word)
    return render_template('search.html', querys=querys)


@app.route('/users/<username>')
def name_post(username):
    names = get_posts_by_user(username)
    return render_template('user-feed.html', names=names)


app.run()