import matplotlib.pyplot as plt
import numpy as np

def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            if not line.startswith('#'): # If 'line' is not a header
                data.append([int(word) for word in line.split(',')])
    return data

if __name__ == '__main__':
    # Load score data
    class_kr = read_data('Assignment 05/data/class_score_kr.csv')
    class_en = read_data('Assignment 05/data/class_score_en.csv')


    # TODO) Prepare midterm, final, and total scores
    midterm_kr, final_kr = zip(*class_kr)
    total_kr = [40/125*midterm + 60/100*final for (midterm, final) in class_kr]
    midterm_en, final_en = zip(*class_en)
    total_en = [40/125*midterm + 60/100*final for (midterm, final) in class_en]

    # TODO) Plot midterm/final scores as points

    plt.scatter(midterm_kr,final_kr,color="red",label="Korean")
    plt.scatter(midterm_en,final_en,color="blue",label="English",marker='+')
    

    plt.legend()
    plt.title("Midterm/Final Test Score Scatter Plot")
    plt.xlabel("Midterm Scores")
    plt.xlim(0,125)
    plt.ylim(0,100)
    plt.ylabel("Final Scores")
    
    plt.grid()
    plt.savefig("Assignment 05/data/Final_Test_Score_Scatter_Plot.png",dpi=300,bbox_inches='tight')

    plt.show()
    
    

    # TODO) Plot total scores as a histogram

    plt.figure()

    bin_width = 5
    bins = np.arange(0, 101, bin_width)

    plt.title("Total Test Score Histogram")
    plt.hist(total_kr,bins=bins,label="Korean",color="red",alpha=0.5)
    plt.hist(total_en,bins=bins,label="English",color="blue",alpha=0.5)
    plt.xlabel("Total Scores")
    plt.ylabel("The numbers of students")
    plt.xlim(0,100)
    plt.savefig("Assignment 05/data/Total_Test_Score_Histogram.png",dpi=300,bbox_inches='tight')
    plt.legend()
    plt.show()

    