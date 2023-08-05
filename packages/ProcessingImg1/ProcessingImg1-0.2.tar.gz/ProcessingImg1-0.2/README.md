# ProcessingImg1
Small and simple image processing library

# How to Install The Library?
## pip install ProcessingImg1

## First, this is a simple and compact package for image processing and hardware management developed using the Pillow package
------------------------



1- Now: We start giving examples of the folder *processing* We agree that this folder contains a Python file named *__init__.py* and this file contains several functions. We will now give examples of these functions in this file.


## Let's take an example : about the function <font color='red'>get_list(path)</font> it takes the path of a folder and then returns all the images as a table


```python
from processing import ImageProcessing

my_object = ImageProcessing()
print(my_object.get_list(r"C:\Users\Alaa\Pictures"))

```
# Output

|  Name Image |
| ---------------|
|  33.jpg
|A.jpg
|aesthetic-ocean-cell-phone-art-94x4pcvrtazi8upm.jpg |
|                   palm-tree-1.jpg                   |
|                        rr.jpg                       |
|                       test.jpg                      |
|                      test1.jpg                      |
|                      veidz.jpg             





##### ['33.jpg', 'A.jpg', 'aesthetic-ocean-cell-phone-art-94x4pcvrtazi8upm.jpg', 'palm-tree-1.jpg', 'rr.jpg', 'test.jpg', 'test1.jpg', 'veidz.jpg']

-----
# Example Two

### The first function <font color='red'>get_list_sorted(main_path , answer)</font> takes the full path of the target image folder,
and takes the user's answer, in order to arrange the images in ascending or descending order. In the entered folder


```python
from processing import ImageProcessing
my_object = ImageProcessing()

print(my_object.get_list_sorted(r"C:\Users\Alaa\Pictures",False))

```

# Output
##### ['33.jpg', 'A.jpg', 'aesthetic-ocean-cell-phone-art-94x4pcvrtazi8upm.jpg', 'palm-tree-1.jpg', 'rr.jpg', 'test.jpg', 'test1.jpg', 'veidz.jpg']

------

### The second function <font color='red'>best_image(path_image )</font> takes the full path of the target image folder and then returns the best image in terms
### of resolution and it takes only one parameter, which is the full path of the folder containing the images

```python
from processing import ImageProcessing

my_object = ImageProcessing()
print(my_object.best_image(r"C:\Users\Alaa\Pictures"))

```

# Output
##### ['A.jpg', 6400, 'C:\\Users\\Alaa\\Pictures']


##### name Image :A.jpg
##### total dimensions :6400 Pixel
##### Location :C:\Users\Alaa\Pictures
----


----

### Referring to the example of the convert_image function, the function that converts an image from a PNG or other extension into a thumbnail with the ICO file extension

```python
from processing import ImageProcessing
result = ImageProcessing.convert_image(path="C:\\Alaa.png" , extension=".jpg", size=(50, 50))



```

---

```python
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

```
![Developer](https://lh3.googleusercontent.com/ogw/ADea4I69npfzwotm16-3HpRfSP4VbW87nXPfi5b8FD-mNu4=s32-c-mo)
["Developer"](https://www.facebook.com/alaa.jassim.mohammed)
