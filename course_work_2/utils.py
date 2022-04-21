import json
from pprint import pprint


def get_posts_all():
    with open('data.json', 'r', encoding='utf-8')as file:
        data = json.load(file)

        return data



def get_posts_by_user(user_name):
    return [user for user in get_posts_all() if user_name.lower() in user['poster_name']]



def get_comments_by_post_id(post_id: int):
    with open('comments.json', 'r', encoding='utf-8')as file:
        comments = json.load(file)
        return [post for post in comments if post_id == post["post_id"]]




def search_for_posts(query):
    posts = []
    for post in get_posts_all():
        querys = post["content"]
        if query.lower() in querys.lower():
            posts.append(post)
    return posts




def get_post_by_pk(pk: int) -> dict | None:
    for post in get_posts_all():
        if pk == post["pk"]:
            return post
    return None










