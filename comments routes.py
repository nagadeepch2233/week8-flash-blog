from flask import redirect, url_for, flash, abort
from flask_login import login_required, current_user
from app.comments import comments
from app.comments.forms import CommentForm
from app import db
from app.models import Comment, Post

@comments.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def add_comment(post_id):
    form = CommentForm()
    post = Post.query.get_or_404(post_id)

    if form.validate_on_submit():
        comment = Comment(
            content=form.content.data,
            user_id=current_user.id,
            post_id=post.id
        )

        db.session.add(comment)
        db.session.commit()

        flash("Comment added successfully!", "success")

    return redirect(url_for('posts.view_post', post_id=post.id))

@comments.route('/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    # Only comment owner can delete
    if comment.user_id != current_user.id:
        abort(403)

    post_id = comment.post_id

    db.session.delete(comment)
    db.session.commit()

    flash("Comment deleted.", "info")

    return redirect(url_for('posts.view_post', post_id=post_id))
