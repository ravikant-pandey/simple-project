from pymongo import MongoClient
from bson import ObjectId
# import pymongo
client = MongoClient('mongodb+srv://<db_username>:<db_password>@cluster0.mp4ybfo.mongodb.net/')

#  Not a good idea to include id and password in code file
db = client.yt_manager # Connect to "yt_manager"
video_collection = db.videos # Connect to "videos" collection

# try:
#     client.admin.command('ping')
#     print("Connected to MongoDB successfully!")
# except Exception as e:
#     print("Failed to connect to MongoDB:", e)
# print(video_collection)

# video add method
def add_video(name,time,channel_name):
    video = {
        'name' : name,
        'time' : time,
        'channel_name': channel_name,
    }
    result = video_collection.insert_one(video)    
    print(f'Task is created with id: {result.inserted_id}')

# all video list method
def list_videos():
    videos = list(video_collection.find())
    if len(videos) == 0:
        print("No videos to display.")
    else:
        print("\nAll Videos:")
        for i, video in enumerate(videos, start=1):
            ID = video.get('_id','[No ID]')
            name = video.get('name', '[No Name]')
            time = video.get('time', '[No Time]')
            channel = video.get('channel_name', '[No Channel]')
            print(f"{i}. - {name} | Time: {time} | Channel Name: {channel} | ID: {ID}")

# upadate the video method
def update_video(video_id,new_name,new_time,channel_name):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set":{'name':new_name,'time':new_time,'channel_name':channel_name}}
    )
    print("Video update successfully....")

# delete the video method
def delete_video(video_id):
   video_collection.delete_one({'_id': ObjectId(video_id)})
   print("Video Delete successfully....")
# main function
def main():
    while True:
        print("\n Youtube Manager App")
        print("1. List all Videos")
        print("2. Add a new video")
        print("3. Update a Video")
        print("4. Delete a video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if(choice=='1'):
            list_videos()
        elif(choice=='2'):
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            channel_name = input("Enter the channel name: ")
            add_video(name,time,channel_name)
        elif(choice=='3'):
            list_videos()
            video_id = input("Enter the video id to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            channel_name = input("Enter the channel name: ")
            update_video(video_id,name,time,channel_name)
        elif(choice=='4'):
            list_videos()
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id)
        elif(choice=='5'):
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == '__main__':
    main()