import requests
import json
from concurrent.futures import ThreadPoolExecutor


def fetch_comments(url):
    response = requests.get(url)
    data = response.json()
    return data['data']['children']


def download_comments(subreddit, num_pages=10):
    base_url = 'https://api.pushshift.io/reddit/comment/search/'
    comments = []

    with ThreadPoolExecutor() as executor:
        # Create a list of URLs for each page of comments
        urls = [f'{base_url}?subreddit={subreddit}&sort=asc&size=500&after={i}d' for i in range(num_pages)]

        # Fetch comments concurrently
        results = list(executor.map(fetch_comments, urls))

        # Combine the results into a single list
        for result in results:
            comments.extend(result)

    # Extract comment data from each item in the 'children' list
    comments = [comment['data'] for comment in comments]

    # Sort comments by created_utc to ensure chronological order
    comments.sort(key=lambda x: x['created_utc'])

    # Save comments to a JSON file
    with open(f'{subreddit}_comments.json', 'w', encoding='utf-8') as file:
        json.dump(comments, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    subreddit_name = "YOUR_SUBREDDIT_NAME"
    download_comments(subreddit_name)
