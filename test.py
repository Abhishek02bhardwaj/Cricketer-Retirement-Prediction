import math
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import openpyxl


class Retirement():

    def __init__(self):
        self.param1 = 0
        self.param2 = 0

    def predict_retirement(self):
        rage = self.param1+self.param2


class Calculation():

    def write_excel(self):
        df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                          index=['one', 'two', 'three'], columns=['a', 'b', 'c'])
        df.to_excel('param.xlsx', sheet_name='new_sheet_name')


# Main class for all the functions
class Main():

    # this function defines variable which will be further used in the code
    def __init__(self, player_name):
        self.dataframe1 = pd.read_excel(
            'India/Batter/'+player_name+'.xlsx', sheet_name="Test")
        self.scores = []
        self.innings = []
        self.ages = []
        self.count = 1
        self.age_num = []
        self.moving_avg = []

    # this function opens the player excel file while and returns the following data in the form of list - 1. Age of Player at every inning, 2. Runs scored in every inning, 3. Number of Inning
    def file_open(self):
        try:
            while (True):
                self.count += 1
                if self.dataframe1['Column7'][self.count][-1] == "*":
                    add = ''
                    for i in self.dataframe1['Column7'][self.count]:
                        if (i != "*"):
                            add += i
                elif (self.dataframe1['Column7'][self.count] == '-'):
                    continue
                else:
                    add = self.dataframe1['Column7'][self.count]
                if (str(self.dataframe1['Column18'][self.count]) != "nan"):
                    self.ages.append(self.dataframe1['Column18'][self.count])
                else:
                    self.ages.append(self.ages[-1])
                self.scores.append(float(add))
                self.innings.append(
                    int(self.dataframe1['Column2'][self.count]))
        except:
            return (self.ages, self.scores, self.innings)
            # pass

    # this function converts the age from "24 years 213 days" format to a float number which tells the age of player and returns the list of that age
    def age_list(self, ages_list):
        for i in ages_list:
            self.age = float(i[0]+i[1])
            if (i[11] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
                self.age += (float(i[9]+i[10]+i[11])/365)
            elif (i[10] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
                self.age += (float(i[9]+i[10])/365)
            else:
                self.age += (float(i[9])/365)
            self.age_num.append(self.age)
        return self.age_num

    # this function plots the graph between x and y values passed in the argument and name the axis as x_axis and y_axis
    def plot_graph(self, x, y, x_axis, y_axis):
        plt.plot(x, y)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.title('My first graph!')
        plt.show()

    # this function calculates the moving average of the player by considering "ini" innings at a time and returns the list of moving average and one more list to plot at x-axis
    def cal_mov_avg(self, runs_scored, ini):
        self.for_x_axis = []
        for i in range(len(runs_scored)-ini):
            self.avg = 0
            for j in range(ini):
                self.avg += runs_scored[i+j]
            self.avg = self.avg/ini
            self.moving_avg.append(self.avg)
            self.for_x_axis.append(len(self.moving_avg))
        return (self.moving_avg, self.for_x_axis)

    # this function takes the list of age of the player at every inning and returns the list of gap between two consecutive innings in days
    def gap_innings(self, ini):
        ini_gap = []
        for i in range(len(ini)-1):
            ini_gap.append(round((ini[i+1]-ini[i])*365))
        return (ini_gap)


# Creating object of Main class and calling its function
main = Main("Suresh Raina")
ag, sc, ini = main.file_open()
fin_ag = main.age_list(ag)
ma, xa = main.cal_mov_avg(sc, 15)
# main.plot_graph(xa, ma, "Innings", "Moving Averages")
# print(main.gap_innings(fin_ag),"\n",sum(main.gap_innings(fin_ag))/len(main.gap_innings(fin_ag)))
print(sum(main.gap_innings(fin_ag))/len(main.gap_innings(fin_ag)),
      "\n", np.std(main.gap_innings(fin_ag)))
