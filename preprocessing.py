# PREPROCESSING
# 
# In this assingment you are expected to implement 
# functions about preprocessing.
#
# Here you should import necessary libraries
# ---------------
import os
import cv2
import splitfolders
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# ---------------

class avion_preprocessing:
    """ 
    
    [Summary]: 
        This is the class where we'll utilize 
        preprocessing functions.
    """

    def __init__(self) -> None:
        # @ TODO: Change the constructor in the proper way (add path arguments etc.)
        # For the beginning you don't have to 
        # implement init function
        # We will complete this later
        pass

    #Returns pathList of the dataset
    def get_pathList(self, path:str):
        self.pathList=[]
        for subdir, dirs, files in os.walk(path):
            liste=list()
            for file in files:
                filestr=file
                filePath=subdir+os.sep+file
                if filestr.split(".")[-1] in ['png','jpg','jpeg']:
                    liste.append(filePath)
            if len(liste)!=0:
                self.pathList.append(liste)
        return self.pathList

    #TODO: Make this work with splitted data
    #Returns metadata of the dataset
    def summary_of_data(self):
        samplePath=self.pathList[0][0]
        self.dataType=samplePath.split(".")[-1]
        sampleimage=cv2.imread(samplePath)
        self.shape=sampleimage.shape
        self.numbers=[len(self.get_pathList[i]) for i in range(len(self.get_pathList))]
        infostr="""
        Data Type: {}
        Image shape: {}
        Number of data :
        """.format(self.dataType,self.shape)
        print(infostr)
        for i in range(len(self.numbers)):
            print(" class "+str(i)+": "+str(self.numbers[i]))

        return infostr
    
    # @TODO: Add augmentation arguments
    # Read the data with keras image data generator
    # Returns a list consisting of train,validation and test generators
    def get_data(self,path,validPath,size,colormode,batch_size,seed=42):
        dataGenTrain=ImageDataGenerator(rescale=1./255)
        dataGenValid=ImageDataGenerator(rescale=1./255)
        trainGen=dataGenTrain.flow_from_directory(path,target_size=size,color_mode=colormode,batch_size=batch_size,seed=seed)
        validationGen=dataGenValid.flow_from_directory(validPath,target_size=size,color_mode=colormode,batch_size=batch_size,seed=seed)
        testGen=dataGenValid.flow_from_directory(validPath,target_size=size,color_mode=colormode,batch_size=batch_size,seed=seed)
        return [trainGen,validationGen,testGen]
    

   
    # Splits the original data into train,test,split and output
    def train_test_validation_split(self, path:str, outputpath:str, seed:int, ratio:tuple):
        splitfolders.ratio(path, output=outputpath, seed=seed, ratio=ratio) 
   



