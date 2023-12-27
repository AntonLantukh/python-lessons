from models import db, Post


def get_posts_list() -> list[Post]:
    return Post.query.all()


def get_post_by_id(post_id: int) -> Post:
    return Post.query.get_or_404(
        post_id,
        f"post #{post_id} not found",
    )


def create_post(title: str, content: str) -> Post:
    post = Post(title=title, content=content)
    db.session.add(post)
    db.session.commit()
    return post


def delete_post(post: Post) -> None:
    db.session.delete(post)
    db.session.commit()
