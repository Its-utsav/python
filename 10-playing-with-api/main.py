import requests


def fetch_data(part_url) -> dict:
    url = f"https://api.freeapi.app/api/v1/public/{part_url}"
    res = requests.get(url)
    json_data = res.json()
    return json_data


def random_joke() -> str:
    data = fetch_data("randomjokes/joke/random")
    if data["success"] and "data" in data:
        joke_data = data["data"]
        return joke_data["content"]
    else:
        raise Exception("Failed to load fetch joke")


def random_user_data() -> str:
    data = fetch_data("randomusers/user/random")

    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        user_location = user_data["location"]["country"]
        return user_name, user_location
    else:
        raise Exception("Failed to load fetch user data")


def random_book() -> str:
    data = fetch_data("books/book/random")
    if data["success"] and "data" in data:
        book_data = data["data"]
        book_name = book_data["volumeInfo"]["title"]
        book_des = book_data["volumeInfo"]["description"]
        return book_name, book_des
    else:
        raise Exception("Failed to load fetch books data")


def main():
    try:
        joke = random_joke()
        print(f"joke is {joke}")

        user_name, country = random_user_data()
        print(f"user name {user_name} \ncountry {country}")
        book_name, book_des = random_book()
        print(f"book name {book_name} \n Book Description is {book_des}")
    except Exception as e:
        print(f"exp  {str(e)}")


if __name__ == "__main__":
    main()
