#!/usr/bin/env python

import countdistros as countd
import matplotlib.pyplot as plt

def run():
    data = countd.get_data()
    
    labels = []
    values = []
    for x, y in data.items():
        labels.append(x)
        values.append(y)

    plt.pie(values, labels=labels)
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':
    run()
