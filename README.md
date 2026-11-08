# Transition GIF 

#### Video Demo: [YouTube](https://youtu.be/_fpCmk1QL0c?si=MIERPWMafdpJMAqW)
#### Description:

<p>Ever wanted to create a small video out of just the given images? This project is an attempt to make that possible.</p>
Although this cannot generate a meaningful sequence from the images, it does create a GIF from the given images by adding a transition between each of the given images. 
<p>Have fun playing with it!</p>

#### How to generate a GIF?
<ul>
<li>
Clone the repository into your local folder.
</li>
<li>
Run this in your terminal/cmd to install the required libraries:

`pip install -r requirements.txt`
</li>
<li>Then run this in your terminal/cmd to generate your GIF:

`python project.py <image_1_path> <image_2_path> ... -o <output_gif_path>`
</li>
</ul>

Your GIF will be created in the chosen path!

#### Code Explanation:

*project.py*
<p>This file contains the following methods:</p>
<ul>
<li> 

`to_images` : Creates Image objects from given filenames and returns them in a list.
</li>
<li> 

`get_frames` : Generates transition frames between the given images and returns them in a tuple. We can pass in two other parameters:
<ul>
    <li>
    
frames (`fr`) : The number of frames we want added between each pair of images.</li>
    <li>
size (`size`): The size we want to reduce the actual image to so that the final GIF has all frames of uniform size.</li>
</ul>
</li>
<li> 

`generate_gif` : Generates a .gif file in the chosen path using the given list of images. (An additional int argument, `fr`, can be passed to specify the interval at which transition for each pair of images happen.)
</li>
<li> 

`set_duration` : Generates a list of numbers representing duration in milliseconds of each frame in the gif. It gives a frame at given intervals (`fr`) a duration of 750ms, and 20ms for the rest of frames.
    
</li>
<li> 

`main` : Takes in the system arguments (or the image paths we pass), creates their Image objects using `to_images` method, then generates all the frames needed for the GIF using `get_frames` method, and finally saves this as GIF using `generate_gif` method.
</li>
</ul>

<br>

*animator.py*

Fields:
<ul>
<li>

`images`
</li>
<li>

`fr`
</li>
<li>

`size`
</li>
</ul>

Methods:
<ul>
<li>

*`__init__`* : Resizes and converts the given Image objects to the given size and into "1" mode, where each pixel is only black or white (False or True), and stores them in the images field.
</li>
<li>

`get_blacks_path` : Given two image arrays, it stores the indices of the black pixels in the first image array and maps each of these pixels to the nearest black pixel in the second array based on Euclidean distance.
</li>
<li>

`create_frames` : Given a list generated using `get_blacks_path`, it creates a list of image arrays of size `fr` and return it.
</li>
<li>

`join_frames` : Given two lists of frames generated, it combines first list with the reversed second list using `&` operator and returns the resulting list.
</li>
<li>

`convert_to_images` : Given a list of image arrays, it converts each of these arrays into Image objects using `Image.fromarray` method and returns the list.
</li>
<li>

`animate` : Given two image objects, it first converts them into numpy arrays and passes them to `get_blacks_path` method twice in different order. Each of the resulting two lists are then converted to lists of image arrays using `create_frames` method. These two resulting lists of image arrays are joined using `join_frames` method and the resulting final list of image arrays is converted to list of Image objects using `convert_to_images` method, and is returned.
</li>
<li>

`generate` : It creates the final list of Image objects from the Image objects in `images` field, by passing consecutive image pairs to `animate` method, and adding the resulting lists to a final list. It returns this final list as a tuple.
</li>
</ul>

<br>

*test_project.py* is for testing some methods in the *project.py* file using *pytest*.



## Acknowledgments

This project is built with the help of the following awesome open-source libraries:

*   [NumPy](https://numpy.org) - The fundamental package for scientific computing with Python.
*   [Pillow (PIL Fork)](https://python-pillow.org) - The friendly PIL fork for powerful image processing capabilities.
*   [pytest](https://pytest.org) - The robust framework that makes it easy to write small, readable tests.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## Contact & Support

If you encounter any bugs, have questions about the NumPy/Pillow implementation, or want to suggest new tests, please feel free to reach out! 

The best way to contact me is by opening a new thread in the [Issues](../../issues) tab of this repository.
