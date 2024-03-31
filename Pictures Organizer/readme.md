# Pictures Organizer

This is a symple Python program to organize pictures inside a folder based on the number of face each pictures has. The code uses an opencv pre-trained [model](https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml), so some pictures maybe placed on the wrong folder.

# Usage

Example code using some pictures (The pictures are from [Pixabay](https://pixabay.com/) and are free to use):

``python3 main.py images/ jpg``

**Expected result**

Three folders should have been created inside the 'images' folder: 1_face/ 2_face/ 4_face

# Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. You can also open an issue if you find a bug or have a suggestion for improvement.

# Future features

- Add a simple GUI
- Use other model to organize the pictures.