# MODEL
# 
# In this assingment you are expected to implement 
# functions about image.
#
# Here you should import necessary libraries
# ---------------
from tensorflow.keras.layers import Input, Dense, Dropout, GlobalAveragePooling2D, MaxPooling2D, Conv2D, Flatten
from tensorflow.keras import Model
from keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications.vgg16 import VGG16,preprocess_input
import matplotlib.pyplot as plt
from tensorflow.keras import Model
from keras.constraints import max_norm
# ---------------


class avion_model:
    """ 
    [Summary]: 
        This is the class where we'll utilize 
        model functions.
    """

    def __init__(self) -> None:
        # Set Default params
        self.model = None
        self.model_name = ""
        self.trainable = True
        self.shape = None
        self.hist = None
        self.steps_per_epoch = 20
        self.validation_steps = 10
        self.epochs = 20
        self.patience = 20
        self.min_delta = 0
        self.verbose_mode = 1
        self.max_norm_value = 2.0
        # DEFAULT ERRORS
        self._MODEL_NAME_ERROR = "ModelName Error: Model name not found. You should set a valid model name with set_model_parameter()."


    def set_model_parameters(self, model_name, shape, number_of_train, number_of_test, learning_rate = .01 ,number_of_classes = 2, batch_size = 64, epochs = 10):
        # self.batch_size = batch_size ...
        self.model_name = model_name
        self.batch_size = batch_size
        self.shape = shape
        self.steps_per_epoch = number_of_train // self.batch_size
        self.validation_steps = number_of_test // self.batch_size
        self.epochs = epochs
        self.activation = "softmax"
        self.number_of_classes = number_of_classes
        self.lr = learning_rate


    def build_model(self):
        # Creating the convolution
        if (self.shape == None): 
            print("Error: Shape undefined.")
            return None
        if (self.model_name.lower() == "vgg16"):
            first_input=Input(shape=self.shape,name='firstImage')
            prep1=preprocess_input(first_input)
            conv1=VGG16(input_tensor=prep1,weights='imagenet',include_top=False)
            model1 = Model(inputs = conv1.input,outputs=conv1.output,name='conv1')
            model1.trainable=self.trainable
            x = GlobalAveragePooling2D()(model1.output)
            x = Dropout(0.5)(x)
            x = Flatten()(x)
            x = Dense(64,activation='relu')(x)
            pred = Dense(self.number_of_classes,activation='softmax')(x)
            self.model = Model(inputs=[first_input],outputs=pred)
            return self.model
        if (self.model_name.lower() == "ordinary_cnn"):
            model = Sequential()
            model.add(Conv2D(64, kernel_size=(3, 3), kernel_constraint=max_norm(self.max_norm_value), activation='relu', input_shape=self.shape, kernel_initializer='he_uniform'))
            model.add(MaxPooling2D(pool_size=(2, 2)))
            model.add(Dropout(0.50))
            model.add(Conv2D(64, kernel_size=(3, 3), kernel_constraint=max_norm(self.max_norm_value), activation='relu', kernel_initializer='he_uniform'))
            model.add(MaxPooling2D(pool_size=(2, 2)))
            model.add(Dropout(0.50))
            model.add(Flatten())
            model.add(Dense(256, activation='relu', kernel_constraint=max_norm(self.max_norm_value), kernel_initializer='he_uniform'))
            model.add(Dense(self.number_of_classes, activation='softmax'))
            self.model = model
            return self.model
        else:
            print(self._MODEL_NAME_ERROR)
        

    def model_compile(self):
        self.model.compile(optimizer = 'adam' ,loss="categorical_crossentropy", metrics=['categorical_accuracy','acc'])

    
    def model_fit(self,x_traindata, x_testdata, y_traindata=None, y_testdata=None):
          self.model.fit(
                        x=x_traindata,
                        y=y_traindata,
                        batch_size = self.batch_size,
                        epochs=self.epochs,
                        verbose=1,
                        validation_data=(x_testdata, y_testdata),
                        validation_batch_size=self.batch_size,
                      )


    def get_model(self):
        return self.model

    def get_model_summary(self):
        return self.model.summary()

    def show_model_history(self):
        if (self.hist):
            plt.plot(self.hist.history["acc"])
            plt.plot(self.hist.history['val_acc'])
            plt.plot(self.hist.history['loss'])
            plt.plot(self.hist.history['val_loss'])
            plt.title("model accuracy")
            plt.ylabel("Accuracy")
            plt.xlabel("Epoch")
            plt.legend(["Accuracy","Validation Accuracy","loss","Validation Loss"])
            plt.show()

    def test_metrics(self):
        pass