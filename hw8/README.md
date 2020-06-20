# W251 - Summer 2020
## Homework 8
## Tom Goter


# Part 1: Image Annotation

## In the time allowed, how many images did you annotate?
I was able to annotate all images in about 100 minutes. It was not a pleasant or relaxing experience, but it does clearly help to convey the subjectivity and noise in labelled datasets, especially those that are labelled through non-experts (e.g., Amazon Mechanical Turk). Examples of the subjectivity include things like 1) when there is just a blur that is supposed to be a TIE Fighter, but it is just a noisy mess in the image do we really want to label it as a TIE Fighter or does that do more harm than good when building an accurate and precise object detector, or 2) when the TIE Fighter explodes into two parts, is it still a single TIE Fighter, or is it two TIE Fighters, or is it zero? I think the experience gave me a better appreciation for how much random noise there is likely to be in most of these very large datasets.

## Home many instances of the Millennium Falcon did you annotate? How many TIE Fighters?
I labelled 308 instances of tie fighters, but toward the end when the second tie fighter blows up I labelled each piece as a TIE fighter. I labelled 311 instances of the Millenium Falcon.

## Based on this experience, how would you handle the annotation of large image data set?
I would crowdsource the heck out of it, but I would also provide very clear guidelines for questionable labelling and provide examples to those doing the labelling to help minimize some of the subjectivity.

## Think about image augmentation? How would augmentations such as flip, rotation, scale, cropping, and translation effect the annotations?
Assuming you are starting with a labelled dataset and applying transformations at runtime, you need to appropriately change the bounding boxes when you are flipping, rotating, etceter. When you are cropping the image, you need to be wary you aren't completely erasing the object of interest (unless that is your intent). Clearly data augmentation for a classification problem is a much easier beast to handle because you just care about the one class of the image, and the intest of the augmentation is to maintain that class. With object detection, it is much more challenging to keep labels, annotations and images synchronized.

# Part 2: Image Augmentation

## Describe the following augmentations in your own words
- **Flip:** A flip is simply a mirroring of the image along the x or y-axis. This can simply be done by reversing the order of the pixel data (easy to do if loaded in as a numpy array). This will not change the class. If you are doing object detection, you will need to modify your coordiantes as well. For example if you flip across the y-axis (i.e., horizontal flip), your y-coordinates will not change, but your x-coordinates will be change from x1, x2 to (xmax-x1), (xmax-x2).
- **Rotation:** This is just as it sounds the image is rotated about its center point some number of degrees. A 90 degree rotation is easy to perform as it just requires one to switch x and y-coordinates. Again for object detection this will similary change the bounding box coordinates.
- **Scale:** This basically is zooming in or out from an image. 
- **Crop:** - From the base image, randomly cut-out just a smaller piece of the image while retaining its class. This will change all of your coordinates, but clearly result in a new image for training with.
-**Translation:** In this case you are maintaining the dimensions and orientation of the image and the object(s); however, your goal is to shift the object within the image.
-**Noise:** In this case you are perturbing individual pixel values throughout the image. This could be in a systematic matter such as a Gaussian blur, or could be a random adjustement from something like a uniform distribution. It will result in grainier photos.

# Part 3: Audio Annotation
## Image annotations require the coordinates of the objects and their classes; in your option, what is needed for an audio annotation?

I think that one would need the timestamp and duration of the event along with the label. Alternatively if one is working with spectograms, audio annotation could also use coordinates just like image annotation.
