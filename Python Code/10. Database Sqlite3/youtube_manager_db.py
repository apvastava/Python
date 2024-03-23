import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGERS PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_videos(name, time):
        cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
        conn.commit()

def update_videos(video_id, new_name, new_time):
        cursor.execute("UPDATE videos SET name = ?, time = ? WHERE ID = ?",(new_name, new_time, video_id))
        conn.commit()

def delete_videos(video_id):
        cursor.execute("DELETE FROM videos where id = ?",(video_id,))
        conn.commit()

def main():
    while True:
        print("\nYoutube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. Exit App")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_videos(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_videos(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to update: ")
            delete_videos(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice!")

    conn.close()
if __name__ == "__main__":
    main()