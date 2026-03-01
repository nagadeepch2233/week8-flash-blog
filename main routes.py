from flask import render_template, request
from app.main import main
from app.models import Post
from app.main.forms import SearchForm

@main.route('/')
@main.route('/page/<int:page>')
def home(page=1):
    form = SearchForm()

    posts = Post.query.order_by(
        Post.date_posted.desc()
    ).paginate(page=page, per_page=5)

    return render_template(
        'main/home.html',
        posts=posts,
        form=form
    )

@main.route('/search', methods=['POST'])
def search():
    form = SearchForm()

    if form.validate_on_submit():
        query = form.query.data

        results = Post.query.filter(
            Post.title.contains(query) |
            Post.content.contains(query)
        ).order_by(Post.date_posted.desc()).all()

        return render_template(
            'main/search_results.html',
            posts=results,
            query=query
        )

    return render_template('main/home.html')
