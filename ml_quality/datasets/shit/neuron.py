#!/usr/bin/python

from artificallib.dentrite import Dentrite
from artificallib.utils import sigmoid

class Neuron:
     
    def __init__(self, numberOfDentrites=0, weigths=None):
        self.bias = 0.5
        self.activation = 1
        self.dentrites = []
        self.currentDentrite = 0
        self.sigma = 0

        self.output = 0
        self.deltaBias = 0
        self.error = 0

        if (weigths != None) and (numberOfDentrites == len(weigths)):
            for i in range(len(weigths)):
                self.dentrites.append(Dentrite(weigths[i]))
        else:
            for i in range(numberOfDentrites):
                self.dentrites.append(Dentrite())
    
    def process(self, inputValue):
        if len(self.dentrites) > 0:
            self.output += inputValue * self.dentrites[self.currentDentrite].weight
            self.currentDentrite += 1
            
            if self.currentDentrite == len(self.dentrites):
                self.currentDentrite = 0
        else:
            self.output += inputValue
    
    def activate(self):
        if len(self.dentrites) > 0:
            self.output += self.bias * self.activation
            self.output = sigmoid(self.output)

    def reset(self):
        self.output = 0
        self.error = 0

    def calculateErrorOutput(self, expected):
        self.error = expected - self.output
        self.sigma = self.output * (1 - self.output) * self.error
        return self.error
    
    def reCalculateOutputNeuronWeights(self, learningRate, momentum, outputs):
        self.deltaBias = learningRate * self.sigma + momentum * self.deltaBias
        self.bias += self.deltaBias
        for i in range(len(outputs)):
            delta = learningRate * self.sigma * outputs[i] + momentum * self.dentrites[i].delta
            self.dentrites[i].delta = delta
            self.dentrites[i].weight += delta
        
    def reCalculateNeuronWeights(self, learningRate, momentum, weights, sigmas, inputs):
        summary = 0
        for i in range(len(weights)):
             summary = weights[i] * sigmas[i]
        self.sigma = summary * self.output * (1 - self.output)
        self.deltaBias = learningRate * self.sigma + momentum * self.deltaBias
        self.bias += self.deltaBias
        for i in range(len(inputs)):
            delta = learningRate * self.sigma * inputs[i] + momentum * self.dentrites[i].delta
            self.dentrites[i].delta = delta
            self.dentrites[i].weight += delta




