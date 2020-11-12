# perceptron.py
# -------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


# Perceptron implementation
import util
PRINT = True

class PerceptronClassifier:
    """
    Perceptron classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """
    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "perceptron"
        self.max_iterations = max_iterations
        self.weights = {}
        for label in legalLabels:
            self.weights[label] = util.Counter() # this is the data-structure you should use

    def setWeights(self, weights):
        assert len(weights) == len(self.legalLabels);
        self.weights = weights;

    def train( self, trainingData, trainingLabels, validationData, validationLabels ):
        """
        The training loop for the perceptron passes through the training data several
        times and updates the weight vector for each label based on classification errors.
        See the project description for details.

        Use the provided self.weights[label] data structure so that
        the classify method works correctly. Also, recall that a
        datum is a counter from features to values for those features
        (and thus represents a vector a values).
        """

        self.features = trainingData[0].keys() # could be useful later
        # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
        # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.
        """
        Implement thuật toán perceptron phân loại chữ số
        So sánh feature vector của dữ liệu với feature vector của label và chọn ra cái giống nhất
        Thực hiện duyệt nhiều lần và mỗi lần sẽ predict trên tập data train 
        Sau đó sẽ thay đổi vector trọng số tùy thuộc vào predict đúng hay là sai như theo guide
        """
        for iteration in range(self.max_iterations):
            print "Starting iteration ", iteration, "..."
            for (X, y) in zip(trainingData, trainingLabels):
                "*** YOUR CODE HERE ***"
                y_pred = self.classify([X])[0]
                if y_pred != y:
                    self.weights[y] += X
                    self.weights[y_pred] -= X



    def classify(self, data ):
        """
        Classifies each datum as the label that most closely matches the prototype vector
        for that label.  See the project description for details.

        Recall that a datum is a util.counter...
        """
        guesses = []
        for datum in data:
            vectors = util.Counter()
            for l in self.legalLabels:
                vectors[l] = self.weights[l] * datum
            guesses.append(vectors.argMax())
        return guesses


    def findHighWeightFeatures(self, label):
        """
        Return 100 features với trọng số cao nhất trong các label
        Xem xem nó giống với list a hay list b và viết đáp số vào file answer.py
        Duyệt 100 lần mỗi lần tìm ra argMax
        Append argMax vào output và update lại trọng số 
        (gán cho trọng số một giá trị thật nhỏ)
        """
        featuresWeights = []

        "*** YOUR CODE HERE ***"
        weights = self.weights[label]
        for i in range(100):
            id = weights.argMax()
            featuresWeights.append(id)
            weights[id] = -1e9
        return featuresWeights
