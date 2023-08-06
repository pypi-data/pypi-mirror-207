# What is the "ProcessingImg1" library?

```bash

```

A simple Pythonic library for image manipulation and hardware configuration that you can use alongside your project to save you time and effort

---

# How to Install The Library?

```bash
pip install ProcessingImg1

```

---

# Example One

for the ImageProcessing class Let's take an example : about the function get_list(path) it takes the path of a folder and then returns all the images as a table

```python
from processing import ImageProcessing
result = ImageProcessing.get_list(r"C:\Users\Alaa\Pictures")
```

---

# Example Two

The first function get_list_sorted(main_path , answer) takes the full path of the target image folder,
and takes the user's answer, in order to arrange the images in ascending or descending order. In the entered folder

```python
from processing import ImageProcessing
print(ImageProcessing.get_list_sorted(r"C:\Users\Alaa\Pictures", False))
```

---

# Example Three

The second function best_image(path_image ) takes the full path of the target image folder and then returns the best image in terms
of resolution and it takes only one parameter, which is the full path of the folder containing the images

```python
from processing import ImageProcessing
result = ImageProcessing.best_image(r"C:\Users\Alaa\Pictures")

```

---

# Example Four

Referring to the example of the convert_image function, the function that convert_image(path , eextension , size) an image from a PNG or other extension into a thumbnail with the ICO file extension

```python
from processing import ImageProcessing
result = ImageProcessing.convert_imagepath="C:\\Alaa.png" , extension=".jpg", size=(50, 50))

```

## Developer information
# ![Developer](https://lh3.googleusercontent.com/ogw/ADea4I69npfzwotm16-3HpRfSP4VbW87nXPfi5b8FD-mNu4=s32-c-mo)
# ["Developer"](https://www.facebook.com/alaa.jassim.mohammed)
