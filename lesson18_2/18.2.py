import requests
from urllib.parse import quote
import os

BASE_URL = "http://127.0.0.1:8080"
IMAGE_PATH = os.path.join(os.path.dirname(__file__), "test_image.jpg")


def upload_image(image_path):
    with open(image_path, "rb") as img_file:
        response = requests.post(
            url=f"{BASE_URL}/upload",
            files={"image": (os.path.basename(image_path), img_file, "image/jpeg")},
        )
    print(f"Статус: {response.status_code}")
    print(f"Відповідь: {response.json()}")
    return response.json()["image_url"]


def get_image_url(filename):
    encoded_filename = quote(filename, safe="")
    response = requests.get(
        url=f"{BASE_URL}/image/{encoded_filename}",
        headers={"Content-Type": "text"},
    )
    print(f"Статус: {response.status_code}")
    print(f"Відповідь: {response.json()}")
    return response.json()["image_url"]


def get_image_file(filename):
    encoded_filename = quote(filename, safe="")
    response = requests.get(
        url=f"{BASE_URL}/image/{encoded_filename}",
        headers={"Content-Type": "image"},
    )
    print(f"Статус: {response.status_code}")
    print(f"Розмір файлу: {len(response.content)} байт")
    return response.content


def delete_image(filename):
    encoded_filename = quote(filename, safe="")
    response = requests.delete(
        url=f"{BASE_URL}/delete/{encoded_filename}",
    )
    print(f"Статус: {response.status_code}")
    print(f"Відповідь: {response.json()}")


print("\n=== POST /upload ===")
image_url = upload_image(IMAGE_PATH)
filename = image_url.split("/")[-1]
print(f"Ім'я файлу на сервері: {filename}")

print("\n=== GET /image/<filename> (text) ===")
get_image_url(filename)

print("\n=== GET /image/<filename> (image) ===")
get_image_file(filename)

print("\n=== DELETE /delete/<filename> ===")
delete_image(filename)