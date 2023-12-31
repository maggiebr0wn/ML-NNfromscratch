from __future__ import print_function
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation, Dropout
from tensorflow.keras.layers import LeakyReLU


class CNN(object):
    def __init__(self):
        # change these to appropriate values
        self.batch_size = 16 #number of images passed to model in each pass - a power of 2
        self.epochs = 2 #number of epochs to train over
        self.init_lr= 1e-2 #learning rate - this will be a small number

        # No need to modify these
        self.model = None

    def get_vars(self):
        return self.batch_size, self.epochs, self.init_lr

    def create_net(self):
        '''
        In this function you are going to build a convolutional neural network based on TF Keras.
        First, use Sequential() to set the inference features on this model. 
        Then, use model.add() to build layers in your own model
        Return: model
        '''

        #TODO: implement this

        print("create_net")

        model = tf.keras.Sequential()
        #model.add(tf.keras.Input(shape=(32, 32, 3)))
        model.add(Conv2D(16, (3, 3), activation=LeakyReLU(), padding="same", input_shape=(32, 32, 3)))
        model.add(LeakyReLU(0.1))
        model.add(Conv2D(32, (3, 3), activation=LeakyReLU(), padding="same", input_shape=(32, 32, 3)))
        model.add(LeakyReLU(0.1))
        model.add(MaxPooling2D((2, 2)))
        model.add(Dropout(0.25))
        model.add(Conv2D(32, (3, 3), activation=LeakyReLU(), padding="same", input_shape=(32, 32, 3)))
        model.add(LeakyReLU(0.1))
        model.add(Conv2D(64, (3, 3), activation=LeakyReLU(), padding="same", input_shape=(32, 32, 3)))
        model.add(LeakyReLU(0.1))
        model.add(MaxPooling2D((2, 2)))
        model.add(Dropout(0.25))
        model.add(Flatten())
        model.add(Dense(256))
        model.add(LeakyReLU(0.1))
        model.add(Dropout(0.25))
        model.add(Dense(10))
        model.add(Activation('softmax'))
          
        self.model = model     

        return self.model

    def compile_net(self, model):
        '''
        In this function you are going to compile the model you've created.
        Use self.model.compile() to build your model.
        '''
        self.model = model

        #TODO: implement this
        
        print("compile_net")

        self.model.compile(optimizer='rmsprop', loss="sparse_categorical_crossentropy", metrics="accuracy", loss_weights=None,
            weighted_metrics=None, run_eagerly=None, steps_per_execution=None)

        return self.model







