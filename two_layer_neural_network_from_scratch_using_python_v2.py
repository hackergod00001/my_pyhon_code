# -*- coding: utf-8 -*-
import gzip
import numpy as np #Linear algebra and mathematical operations
import pandas as pd #importing and loading data
import matplotlib.pyplot as plt # Graph genration
from pyimkernel import ApplyKernels # For applying some image kernel(s) on a grayscale or RGB color-scale image

def load_mnist_images(filename):
    with gzip.open(filename, 'rb') as file:
        data = np.frombuffer(file.read(), np.uint8, offset=16)
    #return data.reshape(-1, 28, 28) / 255.0  # Reshape to 28x28 (ValueError: shapes (60000,28,28) and (784,128) not aligned: 28 (dim 2) != 784 (dim 0))
    return data.reshape(-1, 28 * 28) / 255.0  # Flatten the images to (num_samples, 784)

def load_mnist_labels(filename):
    with gzip.open(filename, 'rb') as file:
        data = np.frombuffer(file.read(), np.uint8, offset=8)
    return data

# Load the MNIST dataset
X_train = load_mnist_images('train-images-idx3-ubyte.gz') #train-images-idx3-ubyte.gz
y_train = load_mnist_labels('train-labels-idx1-ubyte.gz') #train-labels-idx1-ubyte.gz
X_test = load_mnist_images('t10k-images-idx3-ubyte.gz') #t10k-images-idx3-ubyte.gz
y_test = load_mnist_labels('t10k-labels-idx1-ubyte.gz') #t10k-labels-idx1-ubyte.gz

# Display the first few images from the training dataset
num_samples_to_display = 5  # You can change this to view more or fewer images

for i in range(num_samples_to_display):
    plt.subplot(1, num_samples_to_display, i + 1)
    #plt.imshow(X_train[i], cmap='gray')  #  Reshape and Display the image in grayscale
    plt.imshow(X_train[i].reshape(28, 28), cmap=plt.cm.gray) #  Reshape and Display the image in grayscale using pyimkernel
    plt.title(f"Label: {y_train[i]}")

plt.show()  # Show the images

# Display the first few images from the test dataset
num_samples_to_display = 5  # You can change this to view more or fewer images

for i in range(num_samples_to_display):
    plt.subplot(1, num_samples_to_display, i + 1)
    #plt.imshow(X_test[i], cmap='gray')  #  Reshape and Display the image in grayscale
    plt.imshow(X_test[i].reshape(28, 28), cmap=plt.cm.gray) #  Reshape and Display the image in grayscale using pyimkernel
    plt.title(f"Label: {y_test[i]}")

plt.show()  # Show the images

# Print the shapes of the loaded data
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("X_test shape:", X_test.shape)
print("y_test shape:", y_test.shape)

def create_image_dataframe_and_save(X_data, filename):
    # Create a DataFrame to store image data with image numbers
    image_numbers = np.arange(len(X_data))
    image_data = np.concatenate((image_numbers.reshape(-1, 1), X_data), axis=1)

    # Create column names for the DataFrame
    columns = ['Image_Number'] + [f'Pixel {i}' for i in range(1, 28*28 + 1)]

    # Create a DataFrame
    df = pd.DataFrame(image_data, columns=columns)

    # Convert the 'Image_Number' column to integer type
    df['Image_Number'] = df['Image_Number'].astype(int)
    #df = df.astype(int)  # Convert pixel values to integers

    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)

# Create and save the training image DataFrame
create_image_dataframe_and_save(X_train, 'mnist_images.csv')

# Create and save the test image DataFrame
create_image_dataframe_and_save(X_test, 'mnist_test_images.csv')

data = pd.read_csv('mnist_images.csv')

data_t10k = pd.read_csv('mnist_test_images.csv')

data = np.array(data)
m, n = data.shape # m and n are used to store the number of rows and columns in data.
np.random.shuffle(data) # shuffle before splitting into dev and training sets

data_t10k = np.array(data_t10k)
m1, n1 = data_t10k.shape # m1 and n1 are used to store the number of rows and columns in data_t10k.
np.random.shuffle(data_t10k) # shuffle before splitting into dev and training sets

# Normalizing pixel values by dividing them by 255, thus you ensure that the resulting values fall within the range [0, 1]
data_test = data_t10k[0:m1].T # we transpose to make each column a example rather than each row
Y_test = data_test[0]
X_test = data_test[1:n1]
X_test = X_test / 255.0

# Normalizing pixel values by dividing them by 255, thus you ensure that the resulting values fall within the range [0, 1]
data_train = data[0:m].T # we transpose to make each column a example rather than each row
Y_train = data_train[0]
X_train = data_train[1:n]
X_train = X_train / 255.0

# Assuming Y_train is a NumPy array
unique_values, counts = np.unique(Y_train, return_counts=True)

# Print unique values and their counts
for value, count in zip(unique_values, counts):
    print(f"Value: {value}, Count: {count}")

# Check for NaN values in X_train and X_test
nan_in_X_train = np.isnan(X_train)
nan_in_X_test = np.isnan(X_test)

# Check if any NaN values are present
nan_summary_train = np.any(nan_in_X_train)
nan_summary_test = np.any(nan_in_X_test)

print("NaN values in X_train:")
print(nan_summary_train)

print("\nNaN values in X_test:")
print(nan_summary_test)


class NeuralNetwork:
    def __init__(self, input_size, hidden_size1, hidden_size2, output_size):
        self.input_size = input_size
        self.hidden_size1 = hidden_size1
        self.hidden_size2 = hidden_size2
        self.output_size = output_size

        # Initialize weights and biases for the input layer and the first hidden layer
        self.weights_input_hidden1 = np.random.normal(size=(input_size, hidden_size1)) * np.sqrt(1. / input_size)
        self.bias_hidden1 = np.random.normal(size=(1, hidden_size1)) * np.sqrt(2. / hidden_size1)  # He initialization

        # Initialize weights and biases for the first hidden layer and the second hidden layer
        self.weights_hidden1_hidden2 = np.random.normal(size=(hidden_size1, hidden_size2)) * np.sqrt(2. / hidden_size1)  # He initialization
        self.bias_hidden2 = np.random.normal(size=(1, hidden_size2)) * np.sqrt(2. / hidden_size2)  # He initialization

        # Initialize weights and biases for the second hidden layer and the output layer
        self.weights_hidden2_output = np.random.normal(size=(hidden_size2, output_size)) * np.sqrt(2. / hidden_size2)  # He initialization
        self.bias_output = np.zeros((1, output_size))

        # Initialize the cost history list
        self.cost_history = []

    def forward(self, X):
        # Forward propagation
        # Perform forward propagation through the neural network
        # Compute activations for each layer and return the final output

        # Input layer to first hidden layer
        self.hidden_layer1_input = np.dot(X, self.weights_input_hidden1) + self.bias_hidden1 # Linear Hypothesis
        self.hidden_layer1_output = ReLU(self.hidden_layer1_input) # Applying ReLU on linear hypothesis

        # First hidden layer to second hidden layer
        self.hidden_layer2_input = np.dot(self.hidden_layer1_output, self.weights_hidden1_hidden2) + self.bias_hidden2 # Linear Hypothesis
        self.hidden_layer2_output = ReLU(self.hidden_layer2_input) # Applying ReLU on linear hypothesis

        # Second hidden layer to output layer
        self.output_layer_input = np.dot(self.hidden_layer2_output, self.weights_hidden2_output) + self.bias_output # Linear Hypothesis
        self.output_layer_output = softmax(self.output_layer_input) # Applying softmax on linear hypothesis

        return self.output_layer_output

    def backward(self, X, y, output, learning_rate):
        # Backpropagation
        # Perform backpropagation to update weights and biases

        # Calculate error and deltas for each layer
        output_error = output - y

        hidden_layer2_error = output_error.dot(self.weights_hidden2_output.T)
        hidden_layer2_delta = hidden_layer2_error * ReLU_derivative(self.hidden_layer2_output)

        hidden_layer1_error = hidden_layer2_delta.dot(self.weights_hidden1_hidden2.T)
        hidden_layer1_delta = hidden_layer1_error * ReLU_derivative(self.hidden_layer1_output)

        # Clip gradients to prevent exploding gradients
        max_grad_norm = 1.0  # You can adjust this value as needed
        hidden_layer1_delta = np.clip(hidden_layer1_delta, -max_grad_norm, max_grad_norm)
        hidden_layer2_delta = np.clip(hidden_layer2_delta, -max_grad_norm, max_grad_norm)

        # Update weights and biases for each layer
        self.weights_hidden2_output -= self.hidden_layer2_output.T.dot(output_error) * learning_rate
        self.bias_output -= np.sum(output_error, axis=0, keepdims=True) * learning_rate
        self.weights_hidden1_hidden2 -= self.hidden_layer1_output.T.dot(hidden_layer2_delta) * learning_rate
        self.bias_hidden2 -= np.sum(hidden_layer2_delta, axis=0, keepdims=True) * learning_rate
        self.weights_input_hidden1 -= X.T.dot(hidden_layer1_delta) * learning_rate
        self.bias_hidden1 -= np.sum(hidden_layer1_delta, axis=0, keepdims=True) * learning_rate

    def train(self, X, y, epochs, learning_rate, use_soft_labels=False):
        # Train the neural network using backpropagation

        for epoch in range(epochs):
            if use_soft_labels:
                output = self.forward(X)
            else:
                output = self.forward(X)
                y = np.eye(self.output_size)[y]  # Convert hard labels to one-hot encoding

            self.backward(X, y, output, learning_rate)


    def predict(self, X):
        # Make predictions for input data X
        return np.argmax(self.forward(X), axis=1)

    def get_accuracy(self, X, y):
        # Calculate the accuracy of the model on the given data.
        y_pred = self.predict(X)
        return np.mean(y_pred == np.argmax(y, axis=1))

    # calculates the cross-entropy loss with label smoothing and subtracts the label smoothing term from it
    def cost_function_with_label_smoothing(self, predicted_probs, true_labels, alpha): # alpha is the label smoothing hyperparameter.
        num_samples = true_labels.shape[1]  # Number of training samples
        num_classes = predicted_probs.shape[0]  # Number of classes

        # Cross-entropy loss
        cross_entropy_loss = - (1 / num_samples) * np.sum(true_labels * np.log(predicted_probs + 1e-9) + (1 - true_labels) * np.log(1 - predicted_probs + 1e-9))

        # Label smoothing term
        label_smoothing_term = (alpha / num_classes) * np.sum(predicted_probs * np.log(predicted_probs + 1e-9))

        # Final cost
        cost = cross_entropy_loss - label_smoothing_term

        return cost

    def one_hot(self, labels, num_classes):
        return np.eye(num_classes)[labels]



# Define the sigmoid activation function and its derivative
# Z (linear hypothesis) - Z = W*X + b ,
# W - weight matrix, b- bias vector, X- Input

# Define the ReLU activation function and its derivative
def ReLU(Z):
    return np.maximum(Z, 0)

def ReLU_derivative(Z):
    return Z > 0

# Define the softmax activation function
def softmax(Z):
    exp_Z = np.exp(Z - np.max(Z, axis=1, keepdims=True))
    return exp_Z / np.sum(exp_Z, axis=1, keepdims=True)

def gradient_descent(self, X_train, y_train, X_test, y_test, learning_rate=0.01, epochs=100, use_soft_labels=False):
    train_costs = []
    test_costs = []
    train_accuracies = []
    test_accuracies = []

    for epoch in range(epochs):
        if use_soft_labels:
            output_train = self.forward(X_train)
            output_test = self.forward(X_test)
        else:
            output_train = self.forward(X_train)
            output_test = self.forward(X_test)
            y_train = self.one_hot(y_train, self.output_size)
            y_test = self.one_hot(y_test, self.output_size)

        # Calculate training and validation costs
        train_cost = self.cost_function_with_label_smoothing(output_train, y_train, alpha=0.1)
        test_cost = self.cost_function_with_label_smoothing(output_test, y_test, alpha=0.1)

        train_costs.append(train_cost)
        test_costs.append(test_cost)

        # Calculate training and testing accuracies
        train_accuracy = self.get_accuracy(X_train, y_train)
        test_accuracy = self.get_accuracy(X_test, y_test)
        train_accuracies.append(train_accuracy)
        test_accuracies.append(test_accuracy)

        # Backpropagation
        self.backward(X_train, y_train, output_train, learning_rate)

        print(f"Epoch {epoch + 1}/{epochs} - Training Cost: {train_cost:.4f} - Validation Cost: {test_cost:.4f}")

    return train_costs, test_costs, train_accuracies, test_accuracies

"""Define the network parameters and create the neural network instance as you have done earlier:"""

# Define network parameters
input_size = 28 * 28 # Number of input features (e.g., for MNIST, 28x28 = 784)
hidden_size1 = 128  # Number of neurons in the first hidden layer
hidden_size2 = 64   # Number of neurons in the second hidden layer
output_size = 10   # Number of output classes (e.g., for MNIST, 10 digits)

# Create the neural network instance
nn = NeuralNetwork(input_size, hidden_size1, hidden_size2, output_size)

# Train the neural network
nn.train(X_train, y_train, epochs, learning_rate, use_soft_labels=False)

# Evaluate the model on the test data
test_accuracy = nn.get_accuracy(X_test, y_test)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")