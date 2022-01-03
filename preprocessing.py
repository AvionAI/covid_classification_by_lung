# PREPROCESSING
# 
# In this assingment you are expected to implement 
# functions about preprocessing.
#
# Here you should import necessary libraries
# ---------------
import os
# ---------------

class avion_preprocessing:
    """ 
    [Summary]: 
        This is the class where we'll utilize 
        preprocessing functions.
    """

    def __init__(self) -> None:
        # For the beginning you don't have to 
        # implement init function
        # We will complete this later
        pass

    # @TODO: Read in the data from the path 
    # @TODO: Return it
    def read_data(self, path):
        pass
    
    # @TODO: using the data output summary, shape, and other necessary information
    # @TODO: Return these summary as a metadata in any format you like (etc. list, dictionary)
    def summary_of_data(self, data):
        pass

    # @TODO: split the data into train test validation
    # Note: Feel free to change arguments
    # Note: You can either use libraries or you can implement your own.
    def train_test_validation_split(self, data):
        pass

    # @TODO: you are expected to generate at least 2 more data from given image
    # Note: The augmented images shouldn't cause the model to be overfitted, 
    # so make your research accordingly 
    def image_augmentation(self, test_img):
        pass



