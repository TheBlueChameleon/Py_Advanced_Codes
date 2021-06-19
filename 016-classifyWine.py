# This example follows the tutorial found on
# https://www.datacamp.com/community/tutorials/deep-learning-python
# Go and check it out as there's some additional explanations and extra code!

# To have everything in a file, run with:
# python3 016-classifyWine.py > classifyWine-Output.txt 2>&1

# ============================================================================ #
# Dependencies

# Deep Learning Classes and functions
from keras.models import Sequential
from keras.layers import Dense

# SciKit Deep Learning Utilities
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Our "standard libraries"
import pandas as pd
import numpy as np

# ============================================================================ #
# Load data...

print("\n", "#" * 80, sep="")           # Importing keras already gives some debug lines (e.g. no Graphics Card Detected). Separate this from our desired output

# ... from the web ...
#white = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv", sep=';')
#red   = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv", sep=';')

# ... or from the hard disl  ...
white = pd.read_csv("./winequality-white.csv", sep=';')
red   = pd.read_csv("./winequality-red.csv", sep=';')

# ============================================================================ #
# Classify data and combine them into a single source

red  ['type'] = 1
white['type'] = 0

wines = red.append(white, ignore_index=True)

# some output on screen, so we know what we're feeding into the ML machinery
print("SOURCE DATA SUMMARY:\n")

print("White Wines:")
white.info()
print()

print("Red Wines:")
red.info()
print()

print("All Wines:")
wines.info()

# ============================================================================ #
# Select input data (X) and desired output data (y):

X = wines[ wines.columns[0:11] ]        # this is a pd.DataFrame ...
y = np.ravel(wines.type)                # ... while this is a np.ndarray

# Split the data up in train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y,                               # input and output
    test_size=0.33,                     # fraction that should be used for testing
    random_state=42                     # seed value for RNG -- fixed for reproducibility, usually by default None (use a different seed every time)
)

# again, check what train_test_split gave us:
print("\n", "#" * 80, sep="")
print("TRAINING DATA ANALYSIS\n")

print("Training Input Data:")
print(X_train)
X_train.info()
print(type(X))
print()

print("Training Output Data:")
print(y_train)
print(y_train.shape)                    # remember: y was generated from a np.ndarray and hence has to obey its syntax -- there is no .info method for y.

# ============================================================================ #
# Rescale the input data so the learning process performs better

scaler = StandardScaler().fit(X_train)

X_train = scaler.transform(X_train)
X_test  = scaler.transform(X_test)

# ============================================================================ #
# Define the Model

print("\n", "#" * 80, sep="")           # again: defining a model triggers debug output on screen
print("KERAS DEBUG OUTPUT\n")

model = Sequential()

# X_train is the input layer.

# First hidden layer of neurons
model.add(Dense(
    12,                                 # output dimension of this layer. More or less arbitrary number
    activation='relu',                  # "rectilinear unit" -- fast and good for learning
    input_shape=(11,)                   # input dimension of this layer (X has 11 components!)
))

# Second hidden layer 
model.add(Dense(
    8,                                  # again: somewhat arbitrary size of the output of this layer.
    activation='relu'                   # same reasoning as last time
                                        # no input dimension -- inferred automatically from previous layer
))

# Add an output layer 
model.add(Dense(
    1,                                  # our output is a single number: 0..100% confidence whether a given wine is red.
    activation='sigmoid'                # The sigmoid gives exactly this range 0..1 ~> 0.. 100%
))


print("\n", "#" * 80, sep="")
print("MODEL DESCRIPTION\n")

print("Shape:", model.output_shape, "\n" )          # Model output shape
model.summary()                                     # Model summary
print()

print("Configuration:", model.get_config(), "\n")   # Model config
print("Weights:\n", model.get_weights())            # List all weight tensors 

# ============================================================================ #
# Start the learning process!

print("\n", "#" * 80, sep="")
print("BEGIN MODEL DEFINITION\n")

# create fast running code in the background
model.compile(loss='binary_crossentropy',           # name of the loss function
              optimizer='adam',                     # refinement of the gradient descent method. Other methods are SGD (Stochastic gradient descent) and RMSprop
              metrics=['accuracy']                  # what to monitor during the learning process
)

# do the actual learning
model.fit(X_train, y_train,                         # what to learn with
          epochs=20,                                # how often to repeat the learning process
          batch_size=15,                            # how many wines to group together in a single learning step -- makes things faster
          verbose=1
)

# ============================================================================ #
# See how good we are

print("\n", "#" * 80, sep="")
print("EVALUATION\n")

score = model.evaluate(X_test, y_test, verbose=1)
print(f"Loss Function Value: {score[0]:5.2f}\nOverall Accuracy   : {score[1]*100:5.2f}%")

print("-" * 80)
print("an own, very simple measure of performance:")

y_pred_raw = model.predict(X_test)
y_pred = y_pred_raw[:,0]

print(y_pred.shape, y_pred)
print(y_test.shape, y_test)
print(np.sum(np.abs(y_pred[0] - y_test)))
