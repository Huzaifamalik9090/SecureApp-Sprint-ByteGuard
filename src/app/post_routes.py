from flask import Blueprint, abort, redirect, render_template, url_for
from flask_login import current_user, login_required
from . import db
from .forms import PostForm
from .models import Post

post_bp = Blueprint("posts", __name__)


@post_bp.route("/")
def index():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template("posts/index.html", posts=posts)


@post_bp.route("/post/new", methods=["GET", "POST"])
@login_required
def create_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, owner_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for("posts.index"))
    return render_template("posts/post_form.html", form=form, title="Create Post")


def _get_owned_post_or_403(post_id: int) -> Post:
    post = Post.query.get_or_404(post_id)
    # IDOR fix: enforce object-level authorization on every object access.
    if post.owner_id != current_user.id:
        abort(403)
    return post


@post_bp.route("/post/<int:post_id>/edit", methods=["GET", "POST"])
@login_required
def edit_post(post_id: int):
    post = _get_owned_post_or_403(post_id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        return redirect(url_for("posts.index"))
    return render_template("posts/post_form.html", form=form, title="Edit Post")


@post_bp.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id: int):
    post = _get_owned_post_or_403(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("posts.index"))
