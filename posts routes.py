from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app.posts import posts
from app.posts.forms import PostForm
from app import db
from app.models import Post

@posts.route('/create', methods=['GET','POST'])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data,
                    author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.home'))
    return render_template('posts/create_post.html', form=form)

@posts.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('posts/post.html', post=post)
