import os
import glob
import cv2
import numpy as np



def ClusterImage(path, iterations=40, k=5):

    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    #Prepare data for k-means
    # Reshape image into a 2D array of pixels and 3 color values (RGB)
    pixel_vals = image.reshape((-1,3))
    # Convert to float type
    pixel_vals = np.float32(pixel_vals)


    #Implement k-means clustering

    # define stopping criteria
    # you can change the number of max iterations for faster convergence!
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, iterations, 0.2)
    #Perform k-means clustering
    retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, k, cv2.KMEANS_RANDOM_CENTERS)
    # convert data into 8-bit values
    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]

    # reshape data into the original image dimensions
    segmented_image = segmented_data.reshape((image.shape))
    labels_reshape = labels.reshape(image.shape[0], image.shape[1])

    return segmented_image


user_image = glob.glob("static/images/user_img.*")[0]
print(user_image)


art = ClusterImage(user_image, 5, 10)
art = cv2.cvtColor(art, cv2.COLOR_RGB2BGR)
cv2.imshow('Artified Img', art)
cv2.waitKey()