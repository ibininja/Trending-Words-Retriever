'''
import matplotlib.pyplot as plt

radius = [1.0, 2.0, 3.0, 4.0]
area = [3.14159, 12.56636, 28.27431, 50.26544]

plt.plot(radius, area)
plt.show()
'''
 
import matplotlib.pyplot as plt

def PlotGraph(wordcounts):
    
    #v=list(D.values())    
    print("Starting to plot a graph: ")
    plt.bar(range(len(wordcounts)), wordcounts.values(), align='center')
    plt.xticks(range(len(wordcounts)), list(wordcounts.keys()))
    plt.show()
    
if __name__ == "__main__":
    test = {'unbelievable': 1, 'was': 3, 'no': 1, 'Battle': 1, 'on': 1, 'dude': 1, 'October': 1, 'and': 1, 'Concepcion': 1, 'done': 1, 'fought': 5, 'of': 1, 'The': 1, 'won': 1}
    PlotGraph(test)