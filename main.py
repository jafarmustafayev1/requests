import requests
import json
import threading

def fetch_and_save_products():
    url = "https://dummyjson.com/products"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json().get('products', [])
        with open('products.json', 'w') as file:
            json.dump(data, file, indent=4)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

def save_to_json_1():
    url = "https://dummyjson.com/products"
    response = requests.get(url)
    if response.status_code == 200:
        with open('products.json', 'w') as file:
            json.dump(response.json(), file, indent=4)
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")

def save_to_json_2():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        with open('posts.json', 'w') as file:
            json.dump(response.json(), file, indent=4)
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")

if __name__ == "__main__":

    fetch_and_save_products()

    thread1 = threading.Thread(target=save_to_json_1)
    thread2 = threading.Thread(target=save_to_json_2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Ma'lumotlar muvaffaqiyatli saqlandi!")
