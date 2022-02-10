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

    def __init__(self,path:str) -> None:
        self.path=path

    #Returns pathList of the dataset
    def get_pathList(self):
        pathList=[]
        for subdir, dirs, files in os.walk(self.path):
            liste=list()
            for file in files:
                filestr=file
                filePath=subdir+os.sep+file
                if filestr.split(".")[-1] in ['png','jpg','jpeg']:
                    liste.append(filePath)
            if len(liste)!=0:
                pathList.append(liste)
        train,validation,test=[],[],[]
        for i in range(len(pathList)):
            if pathList[i][0].split('/')[1]=='train':
                train.append(pathList[i])
            elif pathList[i][0].split('/')[1]=='validation':
                validation.append(pathList[i])
            elif pathList[i][0].split('/')[1]:
                test.append(pathList[i])

        return [train,validation,test]

    #TODO: Make this work with splitted data
    #Returns metadata of the dataset
    def summary_of_data(self,isSplitted=True):

        if isSplitted:
            for elem in self.get_pathList():
                print(elem[0][0].split("/")[1]+":")
                samplePath=self.get_pathList()[0][0][0]
                self.dataType=samplePath.split(".")[-1]
                sampleimage=cv2.imread(samplePath)
                self.shape=sampleimage.shape
                self.numbers=[len(elem[i]) for i in range(len(elem))]
                infostr="""Data Type: {}
    Image shape: {}
    Number of data :
                """.format(self.dataType,self.shape)
                print(infostr)
                for i in range(len(self.numbers)):
                    print("\tclass "+str(i)+": "+str(self.numbers[i]))
                print("\n")
        else:
            print(self.get_pathList[0].split("/")[1]+":")
            samplePath=self.get_pathList()[0][0]
            self.dataType=samplePath.split(".")[-1]
            sampleimage=cv2.imread(samplePath)
            self.shape=sampleimage.shape
            self.numbers=[len(self.get_pathList[i]) for i in range(len(self.get_pathList))]
            infostr="""Data Type: {}
Image shape: {}
Number of data :
            """.format(self.dataType,self.shape)
            print(infostr)
            for i in range(len(self.numbers)):
                print("\tclass "+str(i)+": "+str(self.numbers[i]))
            print("\n")

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
   



