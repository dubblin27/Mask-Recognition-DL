import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy
import tensorflow as tf 
# classifierLoad = tf.keras.models.load_model('model/modeltest.h5')


model = tf.keras.models.load_model('mainmodel.h5')