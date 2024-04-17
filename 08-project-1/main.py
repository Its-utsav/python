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
    # for index,video in enumerate(videos,start=1):
    #     print(index)
    for i in videos:
        print(i)
 
def add_video(videos):
    name = input("Enter Video Name : ");
    time = input(f"Enter Duration of {name}: ")
    videos.append({"name": name,"time":time})
    save_helper(videos)
     
def update_video_details(videos):
    pass;
    
def delete_video(videos):
    pass;



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