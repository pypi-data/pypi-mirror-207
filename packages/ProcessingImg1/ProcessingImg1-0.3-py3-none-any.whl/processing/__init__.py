



'''
1- The first function get_list_sorted(main_path , answer) takes the full path of the target image folder,
and takes the user's answer, in order to arrange the images in ascending or descending order. In the entered folder

2- The second function best_image(path_image) takes the full path of the target image folder and then returns the best image in terms
of resolution and it takes only one parameter, which is the full path of the folder containing the images

3- The third function (lowest_image) takes the full path of the target image folder and then returns the lowest image in
terms of resolution and it takes only one parameter, which is the full path of the folder containing the images It
works in contrast to the best_image function


4- Fifth function: (get_bytes) Returns the size of the image in the device's memory, takes the full path of the target image

5- The sixth function: (check_path) It checks the image folder if the entered path is a folder and not a file. In this case, the full path
will be returned, otherwise an error message will be returned.

6- The seventh function: (get_list) It returns a list containing all the images ending with the extension
".png", ".jpg", ".jpeg" and at the same time it is an unordered list

7- The eighth function: (calculate_selected_photos) It counts the number of images that end with the required extension, it takes the full
path of the folder for the images in addition to the name of the extension required for the calculation

8- The ninth function: (similarity_check) Its task is to check the similarity of the images, and it takes the first parameter as the
path of the first image, and the second parameter is the path of the second image.

9- The ninth function: get_information_image fetches the image data and takes the current path of the image

10 - The function converts the image into a thumbnail with the ICO file extension, takes the path of the main image, the new image extension, and the new image size
'''


from PIL import Image
from PIL.ExifTags import TAGS
from prettytable import PrettyTable
from PIL import ImageFilter
from PIL import ImageOps
from PIL import ImageDraw
from PIL import ImageFont
import os
import os
import sys
import io
import shutil


class ImageProcessing:
    @staticmethod
    def check_path(path):
        """ Checking if the path is correct, but it does not represent a file
        , only if the path is real and exists in the device"""
        try:
            if os.path.isfile(path):
                raise FileNotFoundError("Error Please enter the correct folder path and not the file path : {}".format(path))
            elif os.path.isdir(path):
                return path

            else:
                raise NotADirectoryError("The path is incorrect or may not exist :{}".format(path))
        except Exception as erro_path:
            return erro_path
        except AttributeError as error:
            return error

    @staticmethod
    def get_list(path_img):
        """ Returns a list of all images in the target path """
        condition = False
        if os.path.isdir(path_img):
            condition = True
        else:
            condition = False

        if condition == True:
            images = list(filter(lambda x: x.endswith((
                                                            ".jpg" , ".png" , ".gif" , ".webr" ,
                                                            ".tiff" , ".psd" , ".raw" , ".bmp",
                                                            ".heif" , ".indd" , ".jpeg", ".svg",
                                                            ".ai" , ".ebps" , ".pdf"




                                                            )), os.listdir(path_img)))

            print("Table Images".center(1))
            table1 = PrettyTable()
            table1.field_names = ["Name Image"]

            for name in images :
                 table1.add_row([name])
            print(table1);print('\n')
            print("List Images".center(1))

            return images




    @staticmethod
    def get_list_sorted(path, answer):
        """ arrange photos take Full Path And take an answer (True) , (False)"""
        condition_answer = False
        picture_dictionary = dict()
        list_pixels = list()
        list_names = list()
        picture_temp , list_result = dict(),list()


        table2 = PrettyTable()
        table2.field_names = ["Name Image","Total dimensions Image"]

        if not isinstance(answer, (bool)):
            condition_answer = False
        else:
            condition_answer = True

        if condition_answer == False:
            return "Please enter a Boolean value {} or {}".format(True, False)
        list_image = list(filter(lambda x: x.endswith((
                                                            ".jpg" , ".png" , ".gif" , ".webr" ,
                                                            ".tiff" , ".psd" , ".raw" , ".bmp",
                                                            ".heif" , ".indd" , ".jpeg", ".svg",
                                                            ".ai" , ".ebps" , ".pdf"



                                                            )), os.listdir(path)))

        for name in list_image:
            with Image.open(path + '\\' + name) as image :
                width , height = image.size
                picture_dictionary[name] = sum([width,height])


        list_names = sorted(picture_dictionary.keys(),reverse=answer)
        list_pixels = sorted(picture_dictionary.values(),reverse=answer)

        for (name,size) in zip(list_names,list_pixels):
            picture_temp[name] = size

        picture_dictionary = picture_temp

        for (name) in picture_dictionary.keys():
           list_result.append(name)


        print("Table Images Sorted".center(50))


        for (name , size) in picture_dictionary.items() :
           table2.add_row([name , size])

        print(table2);print('\n')
        print("List Sorted Images".center(50))

        return False if len(list_result) < 1 else list_result



    @staticmethod
    def best_image(path):
        """ Returns the best resolution image """
        picture_best = dict()
        list_best = list(filter(lambda x: x.endswith((
                                                            ".jpg" , ".png" , ".gif" , ".webr" ,
                                                            ".tiff" , ".psd" , ".raw" , ".bmp",
                                                            ".heif" , ".indd" , ".jpeg", ".svg",
                                                            ".ai" , ".ebps" , ".pdf"



                                                            )), os.listdir(path)))

        for name_best in list_best:
            with Image.open(path + '\\' + name_best) as image :
                width , height = image.size
                picture_best[name_best] = sum([width,height])

        best_name , best_size = '',0
        for (name,size) in picture_best.items():
            if (best_size < size):
                best_size = size
                best_name = name

        if (best_size) > 0 and (best_name) in picture_best.keys():
            print([best_name , best_size , path])
            print("\n")
            return (f"name Image :{best_name}\ntotal dimensions :{best_size} Pixel\nLocation :{path}")




    @staticmethod
    def lowest_image(path):
        """ Return the lowest image """
        picture_lowest = dict()
        list_lowest = list(filter(lambda x: x.endswith((
                                                            ".jpg" , ".png" , ".gif" , ".webr" ,
                                                            ".tiff" , ".psd" , ".raw" , ".bmp",
                                                            ".heif" , ".indd" , ".jpeg", ".svg",
                                                            ".ai" , ".ebps" , ".pdf"


                                                            )), os.listdir(path)))
        for name in list_lowest :
            with Image.open(path + '\\' + name) as mg :
                width , height = mg.size
                picture_lowest[name] = sum([width,height])

        name_lowest , size_lowest = '' , min(list(sorted(picture_lowest.values(),reverse=False)))

        for (name_lowset,size_lowset) in picture_lowest.items():
            if (size_lowset == size_lowest):
                name_lowest = name_lowset
                size_lowest = size_lowset

        print([name_lowest , size_lowest , path])
        print("\n")
        return (f"name Image :{name_lowest}\ntotal dimensions :{size_lowest} Pixel\nLocation :{path}")




    @staticmethod
    def get_bytes(path_mg):
        """ Returns the size of the image in the device's memory get full path image"""
        if not os.path.exists(path_mg):
            return "The path is wrong, please check it correctly : {}".format(path_mg)
        bytes_image = os.path.getsize(path_mg)

        if bytes_image <=1 :
            return "Error Bytes"
        return "Image size in device memory : {}".format(self.bytes_image)



    @staticmethod
    def calculate_selected_photos(path , stretch):
        """ Count the number of images ending in the extension (PNG, JPEG , JPG)"""

        table3 = PrettyTable()
        table3.field_names = ['Name Image','Path','Image Extension']

        try :
            if not os.path.exists(path):
                if not os.path.isdir(path):
                    raise FileNotFoundError("The path is incorrect or not a true path :{}".format(path))

            if stretch.isupper() == True :
                stretch = stretch.lower()

            for (name_image) in os.listdir(path):
                if name_image.endswith(stretch):
                    table3.add_row([name_image , path + '\\' + name_image , name_image.split('.')[-1]])

                print(table3) ;  print("\n")

            print(f"The number of images that end with the extension :{name_image.split('.')[-1]} is {len(list(filter(lambda count :count.endswith((stretch)),os.listdir(path))))} ")
            return list(filter(lambda count :count.endswith((stretch)),os.listdir(path)))

        except FileNotFoundError as error :
            return ("Invalid Path")
            

    
    @staticmethod
    def similarity_check(path_image_one , path_image_two):
        """ Similarity check if the two images are the same """
        try :
            check_condition = False
            table4 = PrettyTable()
            table4.field_names = ['Image One','Image Two' , 'Result']

            if not os.path.exists(path_image_one) or not os.path.exists(path_image_two):
                raise FileNotFoundError("The path is wrong Please check the path is correct")

            img1 = Image.open(path_image_one)
            img2 = Image.open(path_image_two)


            if list(img1.getdata()) != list(img2.getdata()):
                check_condition = False
            else:
                check_condition = True


            if check_condition == False :
               table4.add_row([path_image_one , path_image_two , "No match"])
               return table4
            else:
                table4.add_row([path_image_one , path_image_two , "There is a match"])
                return table4


        except NotADirectoryError as er :
            return er
        except Exception as error_ex :
            return error_ex


    @staticmethod
    def get_information_image(PATH_IMAGE):
        """ Get All Information Image Take Full Path Image """
        try:
            table5 = PrettyTable()
            table5.field_names = [
                            "Filename" , "Image Size" , "Image Height" , "Image Width" ,
                            "Image Format" , "Image Mode" ,"Image is Animated" ,"Frames in Image"

                            ]


            if not os.path.exists(PATH_IMAGE):
                raise FileNotFoundError("File not found : {} Please check the location is correct".format(PATH_IMAGE))

            with Image.open(PATH_IMAGE) as image_open :
                info_dict = {
                    "Filename": image_open.filename,
                    "Image Size": image_open.size,
                    "Image Height": image_open.height,
                    "Image Width": image_open.width,
                    "Image Format": image_open.format,
                    "Image Mode": image_open.mode,
                    "Image is Animated": getattr(image_open, "is_animated", False),
                    "Frames in Image": getattr(image_open, "n_frames", 1)
                    }


            for (lable,value) in info_dict.items():
                table5.add_row([
                                image_open.filename, image_open.size,image_open.height,
                                image_open.width,image_open.format,image_open.mode,
                                getattr(image_open, "is_animated", False),
                                getattr(image_open, "n_frames", 1)

                                ])
                print(table5) ; print("\n") ; return info_dict

        except Exception as e :
            return e



    @staticmethod
    def convert_image(**kwargs):
        """Convert the image to a thumbnail with ICO File extension"""
        try:
            path = kwargs.get('path')
            extension = kwargs.get('extension')
            size = kwargs.get('size')

            if not os.path.exists(path):
                raise FileNotFoundError("The path is wrong, please check it :{}".format(path))
            elif os.path.isfile(path) and os.path.splitext(path)[1] != extension:
                raise TypeError("The file type is wrong, please check it :{}".format(extension))
            else:
                list_extension = ["path" , "extension" , "size"]
                for (check_key) in list_extension :
                    if check_key not in kwargs.keys():
                        raise KeyError("The key is wrong, you must write the keys correctly (path),(extension),(size)")

                with Image.open(path) as image:
                    image.thumbnail(size, Image.Resampling.BICUBIC)
                    image.save(os.path.splitext(path)[0] + '.ico', format='ICO')

                print("The image has been successfully saved in place :{}".format(os.path.splitext(path)[0] + '.ico', format='ICO'))

        except Exception as error:
            return error
