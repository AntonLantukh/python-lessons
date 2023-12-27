from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)
from werkzeug.exceptions import BadRequest

from models import Post
from dao import posts as posts_dao

diary_app = Blueprint(
    "diary_app",
    __name__,
    url_prefix="/posts"
)


@diary_app.get("/", endpoint="list")
def get_posts_list():
    return render_template(
        "posts/index.html",
        posts=posts_dao.get_posts_list(),
    )


@diary_app.get("/<int:post_id>/", endpoint="details")
def get_post_by_id_or_raise(post_id: int):
    post: Post = posts_dao.get_post_by_id(post_id)

    return render_template(
        "posts/details.html",
        post=post,
    )


@diary_app.route("/create/", endpoint="create", methods=["GET", "POST"])
def create_new_post():
    if request.method == "GET":
        return render_template("posts/create.html")

    post_title = request.form.get("post_title", "")
    post_title = post_title.strip()
    post_content = request.form.get("post_content", "")
    post_content = post_content.strip()

    if not post_title:
        raise BadRequest("`post_title` field required")

    if not post_content:
        raise BadRequest("`post_content` field required")

    post = posts_dao.create_post(title=post_title, content=post_content)
    url = url_for("diary_app.details", post_id=post.id)
    return redirect(url)


@diary_app.route(
    "/<int:post_id>/delete/",
    endpoint="delete",
    methods=["GET", "POST"],
)
def delete_post(post_id: int):
    post = posts_dao.get_post_by_id(post_id)
    if request.method == "GET":
        return render_template(
            "posts/delete.html",
            post=post,
        )

    posts_dao.delete_post(post)
    url = url_for("diary_app.list")
    return redirect(url)
