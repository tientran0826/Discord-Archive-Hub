from app import app
from app.models import Channel,Post,User
from flask import render_template,url_for,redirect,flash
from datetime import datetime
from flask_login import current_user,login_user,logout_user,login_required
from app.forms import LoginForm
@app.route('/')
@app.route('/channels/')
@app.route('/home')
def index():
    channel_dict = {}
    channels = Channel.query.all()
    if channels:
        for channel in channels:
            channel_dict[channel.id] = channel.channel_name
    return render_template('home.html', channel_dict= channel_dict)

@app.route("/channels/<channel_id>/")
@app.route("/channels/<channel_id>/all")
def show_post(channel_id):
    posts = Post.query.filter_by(channel_id=channel_id).order_by(Post.created_at.desc()).all()
    channel_dict = {}
    channels = Channel.query.all()
    if channels:
        for channel in channels:
            channel_dict[channel.id] = channel.channel_name
    return render_template('posts.html',posts=posts, channel_dict=channel_dict,cur_channel = int(channel_id))

@app.route("/channel/<channel_id>/images-and-videos")
def show_img_vd(channel_id):
    posts = Post.query.filter_by(channel_id=channel_id).order_by(Post.created_at.desc()).all()
    channel_dict = {}
    channels = Channel.query.all()
    if channels:
        for channel in channels:
            channel_dict[channel.id] = channel.channel_name

    return render_template('images.html',posts=posts, channel_dict=channel_dict,cur_channel = int(channel_id))


@app.route("/channel/<channel_id>/documents")
def show_document(channel_id):
    posts = Post.query.filter_by(channel_id=channel_id).order_by(Post.created_at.desc()).all()
    channel_dict = {}
    channels = Channel.query.all()
    if channels:
        for channel in channels:
            channel_dict[channel.id] = channel.channel_name
    return render_template('documents.html',posts=posts, channel_dict=channel_dict,cur_channel = int(channel_id))


@app.route('/login/<next_page>',methods = ['GET','POST'])
def login(next_page):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(user)
        if user is None or form.password.data != user.password:
            return redirect(url_for('login',next_page=next_page))
        login_user(user)
        return redirect(url_for(next_page))
    return render_template('login.html',title = "Login",form = form)


@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
        print("Logout")
        return redirect(url_for('index'))



