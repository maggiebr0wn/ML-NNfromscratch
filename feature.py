import numpy as np


def create_nl_feature(X):
    '''
    TODO - Create additional features and add it to the dataset
    
    returns:
        X_new - (N, d + num_new_features) array with 
                additional features added to X such that it
                can classify the points in the dataset.
    '''

    mean = X.mean(axis=1)
    Xc = X - mean[:, np.newaxis]

    #X_new = np.square(X)

    #X = np.square(X)
    #return np.asarray((X[:,0]**2, X[:,1]**2, Xc[:,0]**2 + Xc[:,1]**2)).T
    #return np.asarray((X[:,0], X[:,1], np.exp( -(X[:,0]**2 + X[:,1]**2)))).T

    return np.asarray((X[:,0], X[:,1], np.sqrt(2) * Xc[:,0] * Xc[:,1], X[:,0]**2, X[:,1]**2)).T

    """
    X_og = X


    # 0.9

    #print(X.mean(axis=0))

    #X = X - X.mean(axis=0, keepdims=True)

    # sum
    Xsum = np.sum(X, axis = 1)[:, np.newaxis]

    print(Xsum.shape)

    #X = X - col_mean
    #X_new = np.concatenate((X, np.square(X), Xsum), axis = 1)


    X_new = np.concatenate((X, np.square(X)), axis = 1)

    print(X_new.shape)

    #X_new = X

    return X_new 
    """

    #  Delete this line when you implement the function
    
    #raise NotImplementedError