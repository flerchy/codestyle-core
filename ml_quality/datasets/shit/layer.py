#!/usr/bin/python

from artificallib.neuron import Neuron

class Layer:

    def __init__(self, numberOfNeurons, numberOfDentrits = 0):
        self.neurons = []

        for i in range(numberOfNeurons):
            self.neurons.append(Neuron(numberOfDentrits))
    
    def process(self, inputValues):
        outputs = []

        for i in range(len(self.neurons)):
            self.neurons[i].reset()

            for inputValue in inputValues:
                self.neurons[i].process(inputValue)

            self.neurons[i].activate()

            outputs.append(self.neurons[i].output)

        return outputs


    def getErrors(self):
        errors = []

        for neuron in self.neurons:
            errors.append(neuron.error)

        return errors

    def getSigmas(self):
        errors = []

        for neuron in self.neurons:
            errors.append(neuron.sigma)

        return errors

    def getOutputs(self):
        outputs = []

        for neuron in self.neurons:
            outputs.append(neuron.output)

        return outputs

    def getWeights(self, index):
        weights = []

        for  neuron in self.neurons:
            weights.append(neuron.dentrites[index].weight)

        return weights
