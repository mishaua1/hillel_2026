import requests

API_URL = "https://images-api.nasa.gov"


def search_image_ids(query, page_size=20):
    response = requests.get(
        API_URL + "/search",
        params={"q": query, "media_type": "image", "page_size": page_size}
    )
    data = response.json()

    ids = []
    for item in data["collection"]["items"]:
        ids.append(item["data"][0]["nasa_id"])
    return ids


def get_file_list(nasa_id):
    response = requests.get(f"{API_URL}/asset/{nasa_id}")
    return response.json()["collection"]["items"]


def pick_best_jpg(file_list):
    chosen = None
    for file_info in file_list:
        link = file_info["href"]
        if not link.lower().endswith(".jpg"):
            continue
        if "~orig" in link:
            return link
        if chosen is None:
            chosen = link
    return chosen


def download_image(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as out_file:
        out_file.write(response.content)


def main():
    nasa_ids = search_image_ids("Curiosity rover Mars")

    saved_count = 0
    for nasa_id in nasa_ids:
        if saved_count == 2:
            break

        files = get_file_list(nasa_id)
        jpg_url = pick_best_jpg(files)

        if jpg_url is None:
            continue

        saved_count += 1
        filename = "mars_photo" + str(saved_count) + ".jpg"
        download_image(jpg_url, filename)
        print("Saved:", filename)


if __name__ == "__main__":
    main()