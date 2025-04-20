# youyube manager with mongoDB


from bson import ObjectId  # for updating objectID
from pymongo import MongoClient


try:
    client = MongoClient("mongoDBClink")
#  not a good pass and id expose to the other
except:
    raise Exception("unable to connect with mongoDB")

db = client["ytmanager"]
video_collection = db["videos"]
print(video_collection)


def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})


def list_videos():
    for video in video_collection.find():
        print(
            f"video ID:{video['_id']}, video name {video['name']},time {video['time']}"
        )


def update_video_details(v_id, name, time):
    video_collection.update_one(
        {"_id": ObjectId(v_id)},
        {
            "$set": {
                "name": name,
                "time": time,
            }
        },
    )


def delete_video(v_id):
    video_collection.delete_one({"_id": ObjectId(v_id)})


def main():
    while True:
        print("\n youtube manager app with mongoDB \n")
        print("1. List of favourite video: ")
        print("2. Add youtube video: ")
        print("3. Update a youtube video details :")
        print("4. Delete a Youtube video: ")
        print("5. Exit App")
        print("---------------------------")
        choice = int(input("Enter choice : "))
        if choice == 1:
            list_videos()
        elif choice == 2:
            name = input("Enter Video name: ")
            time = input(f"Enter time for {name} video :")
            add_video(name, time)
        elif choice == 3:
            v_id = input("Enter video number to update video detils: ")
            name = input("Enter new Video name: ")
            time = input(f"Enter time for {name} video :")
            update_video_details(v_id, name, time)
        elif choice == 4:
            v_id = input("Enter video ID to delete video : ")
            delete_video(v_id)

        elif choice == 5:
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
