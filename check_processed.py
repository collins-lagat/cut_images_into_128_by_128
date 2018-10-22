from multiprocessing import Process, Manager
import glob, os

def all_raw_photos():
    raw_data = glob.glob("./raw/*.jpg")
    new_data = []
    for data in raw_data:
        new_data.append(data[6:-4])
    return new_data

def all_processed_photos():
    raw_data = glob.glob("./processed/*.jpg")
    new_data = []
    for data in raw_data:
        new_data.append(data[12:27])
    return new_data

def count_images (photo):
    raw_dataset = all_processed_photos()
    number = raw_dataset.count(photo)
    percent = (number/350)*100
    # return_dict[photo] = percent
    print("Photo: "+photo+" has " +str(percent)+"%")


if __name__ == "__main__":
    photos = all_raw_photos()
    # manager = Manager()
    # return_dict = manager.dict()
    # results = []
    # for i in range(0,3):
    #     p = Process( target = count_images, args = (photos[i], return_dict))
    #     results.append(p)
    #     p.start()
    # for result in results:
    #     p.join()
    # print( return_dict.values())
    for photo in photos:
        p = Process( target = count_images, args = (photo,))
        p.start()
    
    
    
