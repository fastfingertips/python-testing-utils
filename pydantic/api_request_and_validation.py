import requests
from pydantic import BaseModel, ValidationError

class Post(BaseModel):
    """
    Pydantic Model: Represents a post obtained from an API.
    """
    user_id: int
    id: int
    title: str
    body: str

def fetch_post_from_api(post_id):
    """
    Fetches a post from the JSONPlaceholder API.

    :param post_id: ID of the post to be fetched
    :return: Fetched post data
    """
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    return response.json()

def validate_post_data(data):
    """
    Validates the given post data using the Pydantic model.

    :param data: Post data to be validated
    :return: Validated post data represented by the Pydantic model
    """
    try:
        post = Post(**data)
        return post
    except ValidationError as e:
        print(f"Validation Error: {e}")
        return None

if __name__ == "__main__":
    # Post ID to fetch from the API
    post_id_to_fetch = 1

    # Fetch post data from the API
    fetched_post_data = fetch_post_from_api(post_id_to_fetch)

    if fetched_post_data:
        # Validate the fetched post data
        validated_post = validate_post_data(fetched_post_data)

        if validated_post:
            # Print the validated post data
            print("Validated Post Information:")
            print(f"UserID: {validated_post.user_id}")
            print(f"ID: {validated_post.id}")
            print(f"Title: {validated_post.title}")
            print(f"Body: {validated_post.body}")
        else:
            print("Invalid post data.")
    else:
        print(f"Failed to fetch post with ID: {post_id_to_fetch}")