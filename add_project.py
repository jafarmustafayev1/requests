import requests
import json
import threading

def fetch_and_save(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'w') as file:
            json.dump(response.json(), file, indent=4)
        print(f"Data from {url} successfully saved to {filename}.")
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")

def fetch_products():
    fetch_and_save("https://dummyjson.com/products", "products.json")

def fetch_posts():
    fetch_and_save("https://jsonplaceholder.typicode.com/posts", "posts.json")

def fetch_users():
    fetch_and_save("https://jsonplaceholder.typicode.com/users", "users.json")

def fetch_comments():
    fetch_and_save("https://jsonplaceholder.typicode.com/comments", "comments.json")

def fetch_todos():
    fetch_and_save("https://jsonplaceholder.typicode.com/todos", "todos.json")

def fetch_albums():
    fetch_and_save("https://jsonplaceholder.typicode.com/albums", "albums.json")

def fetch_photos():
    fetch_and_save("https://jsonplaceholder.typicode.com/photos", "photos.json")

def combine_data():
    try:
        with open("products.json", "r") as products_file:
            products_data = json.load(products_file)
        with open("posts.json", "r") as posts_file:
            posts_data = json.load(posts_file)
        with open("users.json", "r") as users_file:
            users_data = json.load(users_file)
        with open("comments.json", "r") as comments_file:
            comments_data = json.load(comments_file)
        with open("todos.json", "r") as todos_file:
            todos_data = json.load(todos_file)
        with open("albums.json", "r") as albums_file:
            albums_data = json.load(albums_file)
        with open("photos.json", "r") as photos_file:
            photos_data = json.load(photos_file)

        combined_data = {
            "products": products_data,
            "posts": posts_data,
            "users": users_data,
            "comments": comments_data,
            "todos": todos_data,
            "albums": albums_data,
            "photos": photos_data
        }

        with open("combined_data.json", "w") as combined_file:
            json.dump(combined_data, combined_file, indent=4)

        print("All data successfully combined and saved to combined_data.json.")
    except Exception as e:
        print(f"Error combining data: {e}")

if __name__ == "__main__":

    threads = [
        threading.Thread(target=fetch_products),
        threading.Thread(target=fetch_posts),
        threading.Thread(target=fetch_users),
        threading.Thread(target=fetch_comments),
        threading.Thread(target=fetch_todos),
        threading.Thread(target=fetch_albums),
        threading.Thread(target=fetch_photos)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Barcha ma'lumotlar muvaffaqiyatli saqlandi!")

    combine_data()
