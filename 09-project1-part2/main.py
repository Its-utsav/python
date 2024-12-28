# youtube manager project with DB
import sqlite3

# from tabulate import tabulate   ## run pip install tabulate

con = sqlite3.connect("data.db")
cursor = con.cursor()
cursor.execute(
    """
               CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL   
               )
               """
)


def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    # print(rows)
    total_data = len(rows)
    print(total_data)
    if total_data > 0:
        for row in rows:
            print(row)
        # table = rows
        # print(tabulate(table, headers=['id','name','time'], tablefmt='fancy_grid'))
    else:
        print("No data in the table")


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name,time) VALUES (? , ?)", (name, time))
    con.commit()


def update_video_details(v_id, new_name, new_time):
    cursor.execute(
        "UPDATE videos SET name = ?,time = ? WHERE id = ?", (new_name, new_time, v_id)
    )
    con.commit()
    pass


def delete_video(v_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (v_id,))
    # here comma require dut to tuple if we write simple then it take as single variable
    con.commit()
    pass


def main():
    while True:
        print("\n youtube manager app with db \n")
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
            v_id = input("Enter video number to update video detils")
            name = input("Enter new Video name: ")
            time = input(f"Enter time for {name} video :")
            update_video_details(v_id, name, time)

        elif choice == 4:
            v_id = int(input("Enter video ID to delete video : "))
            delete_video(v_id)

        elif choice == 5:
            break

        else:
            print("Invalid choice")

    con.close()  # prevent from curope data and close the data base


if __name__ == "__main__":
    main()
