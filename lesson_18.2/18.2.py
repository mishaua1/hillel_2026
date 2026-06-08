import requests
from urllib.parse import quote
import os

BASE_URL = "http://127.0.0.1:8080"
IMAGE_PATH = "test_image.jpg"

print("\n=== POST /upload ===")
with open(IMAGE_PATH, "rb") as img_file:
    response_post = requests.post(
        url=f"{BASE_URL}/upload",
        files={"image": (os.path.basename(IMAGE_PATH), img_file, "image/jpeg")},
    )
print(f"Статус: {response_post.status_code}")
post_data = response_post.json()
print(f"Відповідь: {post_data}")

image_url = post_data["image_url"]
filename = image_url.split("/")[-1]
print(f"Ім'я файлу на сервері: {filename}")

print("\n=== GET /image/<filename> ===")
encoded_filename = quote(filename, safe="")
response_get = requests.get(
    url=f"{BASE_URL}/image/{encoded_filename}",
    headers={"Content-Type": "text"},
)
print(f"Статус: {response_get.status_code}")
get_data = response_get.json()
print(f"Відповідь: {get_data}")
print(f"URL зображення: {get_data['image_url']}")

print("\n=== DELETE /delete/<filename> ===")
response_delete = requests.delete(
    url=f"{BASE_URL}/delete/{encoded_filename}",
)
print(f"Статус: {response_delete.status_code}")
delete_data = response_delete.json()
print(f"Відповідь: {delete_data}")