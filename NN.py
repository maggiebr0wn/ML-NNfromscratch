import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.preprocessing import MinMaxScaler

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import plot_confusion_matrix

'''
We are going to use Boston house-prices dataset provided by sklearn
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html
To train a 2 layer fully connected neural net. We are going to build the neural network from scratch. 
'''


class dlnet:

    def __init__(self, x, y, lr = 0.003):
        '''
        This method initializes the class, it is already implemented for you. 
        Args:
            x: data
            y: labels
            Yh: predicted labels
            dims: dimensions of different layers
            param: dictionary of different layer parameters
            ch: Cache dictionary to store forward parameters that are used in backpropagation
            loss: list to store loss values
            lr: learning rate
            sam: number of training samples we have

        '''        
        self.X=x # features
        self.Y=y # ground truth labels

        self.Yh=np.zeros((1,self.Y.shape[1])) # estimated labels
        self.dims = [13, 20, 1] # dimensions of different layers

        self.param = { } # dictionary for different layer variables
        self.ch = {} # cache for holding variables during forward propagation to use them in backprop
        self.loss = [] # list to store loss values 

        self.iter = 0 # iterator to index into data for making a batch 
        self.batch_size = 64 # batch size 
        
        self.lr=lr # learning rate
        self.sam = self.Y.shape[1] # number of training samples we have
        self._estimator_type = 'regressor'
        self.neural_net_type = "Tanh -> Relu" 


    def nInit(self): 
        '''
        This method initializes the neural network variables, it is already implemented for you. 
        Check it and relate to the mathematical description above.
        You are going to use these variables in forward and backward propagation.
        '''   
        np.random.seed(1)
        self.param['theta1'] = np.random.randn(self.dims[1], self.dims[0]) / np.sqrt(self.dims[0]) 
        self.param['b1'] = np.zeros((self.dims[1], 1))        
        self.param['theta2'] = np.random.randn(self.dims[2], self.dims[1]) / np.sqrt(self.dims[1]) 
        self.param['b2'] = np.zeros((self.dims[2], 1))     


    def Relu(self, u):
        '''
        In this method, you are going to implement element wise Relu. 
        Make sure that all operations here are element wise and can be applied to an input of any dimension. 
        Input: u of any dimension
        return: Relu(u) 
        '''
        #TODO: implement this 

        return np.maximum(0, u)

    def Tanh(self, u):
        '''
        In this method you are going to implement element wise Tanh. 
        Make sure that all operations here are element wise and can be applied to an input of any dimension. 
        Input: u of any dimension
        return: Tanh(u) 
        '''
        #TODO: implement this 

        return np.tanh(u)
    
    
    def dRelu(self, u):
        '''
        This method implements element wise differentiation of Relu, it is already implemented for you.  
        Input: u of any dimension
        return: dRelu(u) 
        '''
        u[u<=0] = 0
        u[u>0] = 1
        return u

    def dTanh(self, u):
        '''
        This method implements element wise differentiation of Tanh, it is already implemented for you.
        Input: u of any dimension
        return: dTanh(u) 
        '''
        o = np.tanh(u)
        return 1-o**2
    
    
    def nloss(self,y, yh):
        '''
        In this method you are going to implement mean squared loss. 
        Refer to the description in the notebook and implement the appropriate mathematical equation.
        Input: y 1xN: ground truth labels
               yh 1xN: neural network output after Relu 

        return: MSE 1x1: loss value 
        '''
        
        #TODO: implement this 

        mse = (np.square(np.subtract(y, yh)).mean())/2

        return mse
        

    def forward(self, x):
        '''
        Fill in the missing code lines, please refer to the description for more details.
        Check nInit method and use variables from there as well as other implemented methods.
        Refer to the description in the notebook and implement the appropriate mathematical equations.
        do not change the lines followed by #keep. 
        '''
        
        #TODO: implement this 
            
        self.ch['X'] = x #keep

        u1 = np.matmul(self.param['theta1'], x) + self.param['b1']
        o1 = self.Tanh(u1)

        u2 = np.matmul(self.param['theta2'], o1) + self.param['b2']
        o2 = self.Relu(u2)

        self.ch['u1'],self.ch['o1']=u1,o1 #keep 
    
        self.ch['u2'],self.ch['o2']=u2,o2 #keep

        return o2 #keep

    def backward(self, y, yh):
        '''
        Fill in the missing code lines, please refer to the description for more details
        You will need to use cache variables, some of the implemented methods, and other variables as well
        Refer to the description in the notebook and implement the appropriate mathematical equations.
        do not change the lines followed by #keep.  
        '''
        #TODO: implement this 

        # set dLoss_o2     
        
        dLoss_o2 = (1/y.shape[1])*(yh - y) # (1, 379)
            
        # Implement equations for getting derivative of loss w.r.t u2, theta2 and b2
        # set dLoss_u2, dLoss_theta2, dLoss_b2 
        
        dLoss_u2 = dLoss_o2*(self.dRelu(self.ch['u2'])) # (1, 379)

        dLoss_theta2 = np.matmul(dLoss_u2, (self.ch['o1'].T)) # (1, 20)

        dLoss_b2 = np.matmul(dLoss_u2, np.ones((y.shape[1], 1), dtype=int)) # (1, 1)

        # set dLoss_o1
        
        dLoss_o1 = np.matmul(dLoss_u2.T, self.param['theta2']).T # (20, 379)

        #Implement equations for getting derivative of loss w.r.t u1, theta1 and b1
        # set dLoss_u1, dLoss_theta1, dLoss_b1

        dLoss_u1 = dLoss_o1 * (1 - np.square(self.ch['o1'])) # (20, 379)

        dLoss_theta1 = np.matmul(dLoss_u1, self.ch['X'].T) # (20, 13)

        dLoss_b1 = np.matmul(dLoss_u1, np.ones((y.shape[1], 1), dtype=int)) # (20, 1)       
            
        #parameters update, no need to change these lines
        self.param["theta2"] = self.param["theta2"] - self.lr * dLoss_theta2 #keep
        self.param["b2"] = self.param["b2"] - self.lr * dLoss_b2 #keep
        self.param["theta1"] = self.param["theta1"] - self.lr * dLoss_theta1 #keep
        self.param["b1"] = self.param["b1"] - self.lr * dLoss_b1 #keep
        return dLoss_theta2, dLoss_b2, dLoss_theta1, dLoss_b1 #keep
        
        

    def gradient_descent(self, x, y, iter = 60000):
        '''
        This function is an implementation of the gradient descent algorithm.
        Note:
        1. GD considers all examples in the dataset in one go and learns a gradient from them. 
        2. One iteration here is one round of forward and backward propagation on the complete dataset. 
        3. Append loss at multiples of 2000 i.e. at 0th, 2000th, 4000th .... iterations
        ''' 
        #Todo: implement this 
        
        self.nInit()
        for i in range(0, iter):
            yh = self.forward(x)
            loss = self.nloss(y, yh)
            dloss_W2, dLoss_b2, dLoss_W1, dLoss_b1 = self.backward(y, yh)
            self.loss.append(loss)

            if i % 2000 == 0:
                print("Loss after iteration", i, ":", loss)
            else:
                pass

        return


    
    #bonus for undergrdauate students 
    def batch_gradient_descent(self, x, y, iter = 60000):
        '''
        This function is an implementation of the batch gradient descent algorithm

        Note: 
        1. Batch GD loops over all mini batches in the dataset one by one and learns a gradient 
        2. One iteration here is one round of forward and backward propagation on one minibatch. 
           You will use self.iter and self.batch_size to index into x and y to get a batch. This batch will be
           fed into the forward and backward functions.
        3. Append loss at multiples of 1000 iterations i.e. at 0th, 1000th, 2000th .... iterations  
        4. It is fine if you get a noisy plot since learning on a batch adds variance to the 
           gradients learnt
        '''
        
        #Todo: implement this 

        self.nInit()
        for i in range(0, iter):

            ind = []
            for j in range(0, self.batch_size):
                ind.append(np.random.randint(0, x.shape[1]))

            xbatch = x[:, ind]
            #print(xbatch.shape)
            ybatch = y[:, ind]
            #print(ybatch.shape)

            yh = self.forward(xbatch)
            loss = self.nloss(ybatch, yh)
            dloss_W2, dLoss_b2, dLoss_W1, dLoss_b1 = self.backward(ybatch, yh)

            if i % 1000 == 0:
                print("Loss after iteration", i, ":", loss)
                self.loss.append(loss)
            else:
                pass

    def predict(self, x): 
        '''
        This function predicts new data points
        It is already implemented for you
        '''
        Yh = self.forward(x)
        return Yh
