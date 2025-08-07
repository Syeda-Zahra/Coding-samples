import os
import random
from tkinter import *
from tkinter import ttk

from PIL import Image, ExifTags, ImageTk
from PIL.ExifTags import TAGS

def get_all_images(directory):
    image_name_lst = []
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            image_name_lst.append(filename)
    return image_name_lst


def get_image_meta_data(image_lst):
    img_meta_data = []
    for img in image_lst:
        image_file = f"SampleImages/{img}"
        image = Image.open(image_file)
        exif = {ExifTags.TAGS[k]: v for k, v in image.getexif().items() if k in ExifTags.TAGS}
        temp_dict = {
            'UserComment': exif['UserComment'],
            'img': img
        }
        img_meta_data.append(temp_dict)
    return img_meta_data


def bubbleSort(image_list):
    element_swapped = False
    for i in range(len(image_list)):
        for j in range(0, len(image_list) - i - 1):
            if image_list[j].lower() > image_list[j + 1].lower():
                image_list[j], image_list[j + 1] = image_list[j + 1], image_list[j]
                element_swapped = True
            if not element_swapped:
                break
    return image_list


def sort_images_by_name(image_list):
    """used the shuffled images function to test
    out bubbleSort function as images were already sorted by name"""
    # shuffled = shuffle_images(image_list)
    sorted_images = bubbleSort(image_list)
    print("Sort Image By Name:")
    print("===================")
    for image_name in sorted_images:
        print(image_name)
    return sorted_images


def sort_images_by_user_input_tag(image_meta_data):
    # using bubble sort again
    element_swapped = False
    for i in range(len(image_meta_data)):
        for j in range(0, len(image_meta_data) - i - 1):
            if image_meta_data[j]['UserComment'].lower() > image_meta_data[j + 1]['UserComment'].lower():
                image_meta_data[j], image_meta_data[j + 1] = image_meta_data[j + 1], image_meta_data[j]
                element_swapped = True
            if not element_swapped:
                break
    sorted_images = []
    print('Image Names sorted by UserComments exif tag:')
    print('============================================')
    for data_dict in image_meta_data:
        print(data_dict['img'])
        sorted_images.append(data_dict['img'])
    return sorted_images


def shuffle_images(image_list):
    shuffled_image_names = [''] * 8
    index_list = random.sample(range(0, 8), 8)
    for i in range(len(index_list)):
        shuffled_image_names[i] = image_list[index_list[i]]

    print_shuffled_images(shuffled_image_names)
    return shuffled_image_names


def print_shuffled_images(shuffled_imgs):
    print("Shuffled Images:")
    print("================")
    for img in shuffled_imgs:
        print(img)


def display_images_on_gui(gui_data):
    gui_data_dict = get_image_meta_data(gui_data)
    # Display all images on Tkinter GUI
    root = Tk()
    for data_dict in gui_data_dict:
        data_dict['tk_img'] = ImageTk.PhotoImage(Image.open(f"SampleImages/{data_dict['img']}").resize((50, 50)))
    for data_dict in gui_data_dict:
        label_1 = ttk.Label(root, image=data_dict['tk_img'])
        label_1.pack(side=LEFT, pady=15)

        name_str = 'Filename: ' + data_dict['img']
        label_3 = ttk.Label(root, text=name_str)
        label_3.pack(side='bottom')

        meta_data_str = 'UserComment: ' + data_dict['UserComment']
        label_3 = ttk.Label(root, text=meta_data_str)
        label_3.pack(side='bottom')
    root.mainloop()
    return


def main():
    print("Please choose one of the following options:")
    user_input = input("1: sort by image name\n2: sort by image UserComment tag\n3: shuffle images\n>> ")
    function_dict = {'1': sort_images_by_name, '2': sort_images_by_user_input_tag, '3': shuffle_images}
    
    directory = "SampleImages"
    
    image_names_list = get_all_images(directory)
    image_meta_data = get_image_meta_data(image_names_list)
    if user_input == '1':
        data = image_names_list
    elif user_input == '2':
        data = image_meta_data
    elif user_input == '3':
        data = image_names_list
    else:
        print('Incorrect Input!')
        exit(1)
    
    gui_data =function_dict[user_input](data)
    
    display_images_on_gui(gui_data)


if __name__ == "__main__":
    main()
