import seaborn as sns
import matplotlib.pyplot as plt

def plot_bar(data, tema):
    # x = data.keys
    fig, ax = plt.subplots()
    ax.bar(data.keys(), data.values())
    ax.set_ylabel("Cantidades")
    ax.set_title(tema)
    figure = plt.show()
    return figure

def plot_scatter(data, tema):
    # x = data.keys
    fig, ax = plt.subplots()
    ax.scatter(data.keys(), data.values())
    ax.set_ylabel("Cantidades")
    ax.set_title(tema)
    figure = plt.show()
    return figure