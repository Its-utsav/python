import json

# data_file = open('data.txt')


def load_data():
    try:
        with open('data.txt','r') as file:
            json_data = json.load(file) # load data in to json
            print(type(json_data)) #list aka json list
            return json_data;
    except FileNotFoundError: # here we define file not found except name
        return [];

# when we add video or change data of a video or delete a video than we need to save a that operations data or changes


def save_helper(videos):
    with open('data.txt','w') as file:
        json.dump(videos,file)

def list_of_videos(videos):
    print('*'*50);   
    for index,video in enumerate(videos,start=1):    
        print(f'\n {index} video name: {video['name']} duration {video['time']}');
    print('*'*50);   

 
def add_video(videos):
    name = input("Enter Video Name : ");
    time = input(f"Enter Duration of {name}: ")
    print(f"video name : {name} and time {time} added. ");
    videos.append({"name": name,"time":time})
    save_helper(videos)
     
def update_video_details(videos):
    list_of_videos(videos);
    index = int(input("Enter the video number to update video details: "));
    
    if 1<=index <= len(videos):
        name = input("Enter a new video name: ");
        time = input("Enter a new video time: ");        
        
        videos[index-1] = {'name':name,'time':time};
        save_helper(videos)
    else:
        print("Invalid Index selected");
        
    
def delete_video(videos):
    list_of_videos(videos);
    index = int(input("Enter the video number to delete: "));
    
    if 1<= index <=len(videos):
        print(f'video at {index} is deleted .');
        del videos[index-1]
        save_helper(videos)
    else:
        print("invalid number");

def main():
    videos = load_data()
    while True:
        print("\n youtube manager \n")
        print('1. List of favourite video: ');
        print('2. Add youtube video: ');
        print("3. Update a youtube video details :")
        print("4. Delete a Youtube video: ");
        print("5. Exit App");
        print("---------------------------");
        
        option = int(input("Give me from 1 to 5: "));
        
        match option:
            case 1:
                list_of_videos(videos);
            case 2:
                add_video(videos);
            case 3:
                update_video_details(videos);
            case 4:
                delete_video(videos);
            case 5:
                break;
            case _: # when other than 1 to 5
                print("invalid choice");
                
                

if __name__ == '__main__':
    main()