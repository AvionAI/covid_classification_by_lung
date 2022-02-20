# COVID DIAGNOSIS BY LUNG X-RAY IMAGES
<strong>Problem:</strong> In this project, the aim was classifying Lung X-Ray images into 4 classes, namely Covid-19,Lung Opacity, Viral Pneumonia and Healthy. 

The <strong>dataset</strong> used for training and test can be found in Kaggle: https://www.kaggle.com/tawsifurrahman/covid19-radiography-database

<strong>Solution:</strong> We developed an object-oriented system consisting of image,preprocessing,model classes. Utilizing these classes, we used the architecture VGG16 and pretrained weights of imagenet to increase the accuracy. In addition, we used CLAHE in the image enhancement part. 

<em>You can see the demonstration with data in the IPython notebook we placed to the repository.</em>

<b>Results -->> Training Accuracy: %98.2, Validation Accuracy: %95.3, Test Accuracy: %94.1 
