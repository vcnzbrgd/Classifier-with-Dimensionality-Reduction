import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler

def plot_2d(x, y, title='title', xlabel='X axis', ylabel='Y axis'):
    """
    Creates a 3D scatter plot with points colored based on a gradient.
    
    Parameters:
    - x: array-like, the x coordinates of the points.
    - y: array-like, the y coordinates of the points.
    - gradient: array-like, values that determine the color gradient of the points.
    - title: str, the title of the plot.
    - xlabel: str, the label for the x-axis.
    - ylabel: str, the label for the y-axis.
    """
    # gradient is the distance from origin
    gradient = np.sqrt(x**2 + y**2)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='2d')
    scatter = ax.scatter(x, y, c=gradient, cmap='viridis')
    plt.colorbar(scatter, label='Gradient Value')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


def plot_3d(x, y, z, title='title', xlabel='X axis', ylabel='Y axis', zlabel='Z axis'):
    """
    Creates a 3D scatter plot with points colored based on a gradient.
    
    Parameters:
    - x: array-like, the x coordinates of the points.
    - y: array-like, the y coordinates of the points.
    - z: array-like, the z coordinates of the points.
    - gradient: array-like, values that determine the color gradient of the points.
    - title: str, the title of the plot.
    - xlabel: str, the label for the x-axis.
    - ylabel: str, the label for the y-axis.
    - zlabel: str, the label for the z-axis.
    """
    # gradient is the distance from origin
    gradient = np.sqrt(x**2 + y**2, z**2)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(x, y, z, c=gradient, cmap='viridis')
    plt.colorbar(scatter, label='Gradient Value')
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    plt.show()


