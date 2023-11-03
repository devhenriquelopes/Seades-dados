from django.test import TestCase

# Create your tests here.

import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    # Create a new figure and plot some data
    plt.figure()
    x = [10, 25, 33, 64, 68]
    y = [20, 31, 45, 57, 80]
    plt.plot(x, y)

    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')

def get_graph_barra():
    # Create a new figure and plot some data
    plt.figure()
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    plt.plot(x, y)


    # Save the figure to a BytesIO object
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())

    return string.decode('utf-8')