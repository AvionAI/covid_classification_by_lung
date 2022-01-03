# MODEL
# 
# In this assingment you are expected to implement 
# functions about image.
#
# Here you should import necessary libraries
# ---------------
import os
# ---------------

class avion_model:
    """ 
    [Summary]: 
        This is the class where we'll utilize 
        model functions.
    """

    def __init__(self) -> None:
        # This is set for initial steps. Will be updated later.
        batch_size = self.batch_size
        epochs = self.epochs
        pass

    # @TODO: Set the necessary parameters by changing those in avion_model object
    def set_model_parameters(self, batch_size, epochs, *kwargs):
        # self.batch_size = batch_size ...
        pass

    # @TODO: build the model and return it
    def build_model(self, *kwargs):
        # You should use global attributes in the object
        pass
    
    # @TODO: we'll use another class but we will write a seperate function for this
    # We do this because it's much elegant and easier to have control over the model
    # by using class attributes. It also reduces the coding effort resulting in a cleaner main flow.
    def model_fit(self):
        # i.e. result = model.fit(... , batch_size = self.batch_size, epochs = self.epochs, ...)
        pass

    # @TODO: Conduct at least 2 types of testing in this function
    # @TODO: Report the results and also write them to a file in the local folder.
    # @TODO: Plot confusion matrix and also save it to the local
    # @TODO: Ultimate goal is to show the model performance in detail
    def test_metrics(self):
        pass