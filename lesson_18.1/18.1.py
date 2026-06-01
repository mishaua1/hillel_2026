import requests

API_URL = "https://images-api.nasa.gov"

search_response = requests.get(
    API_URL + "/search",
    params={"q": "Curiosity rover Mars", "media_type": "image", "page_size": 20}
)
search_data = search_response.json()

found_ids = []
for item in search_data["collection"]["items"]:
    found_ids.append(item["data"][0]["nasa_id"])

saved_count = 0
for nasa_id in found_ids:
    if saved_count == 2:
        break

    asset_response = requests.get(f"{API_URL}/asset/{nasa_id}")
    file_list = asset_response.json()["collection"]["items"]

    chosen_url = None
    for file_info in file_list:
        link = file_info["href"]
        if not link.lower().endswith(".jpg"):
            continue
        if "~orig" in link:
            chosen_url = link
            break
        if chosen_url is None:
            chosen_url = link

    if chosen_url is None:
        continue

    saved_count += 1
    image_response = requests.get(chosen_url)
    output_name = "mars_photo" + str(saved_count) + ".jpg"

    with open(output_name, "wb") as out_file:
        out_file.write(image_response.content)

    print("Saved:", output_name)