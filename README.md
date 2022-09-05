# Store-Sales-Prediction
This is the repository for the Ineuron Project of predicting the sales of any individual item in a supermarket using a machine learning model, 
which is accessed using a web app.

Test.csv - data set for testing the accuracy of the model in .csv format.

Train.csv - data set for training the model in .csv format.

Project Python File.ipynb - This is the python file in which i imported my data and trained my ML model. I trained 3 algorithms(Linear regression, Decision trees and Random forest ) and saved them on my desktop using pickle library. I then used all 3 models (in my webapp) and used the mean of the values obtained using the 3 models to get my final MRP of a store item.

Requirements.txt - This file contains all the python libraries used in the project with their versions.

WEBAPP.py - Python code used to create the streamlit webapp using the streamlit python library.

Setup.sh - This is the file used in deploying the webapp on heroku.
