import pandas as pd
import numpy as np
import os

class Assingment(object):
    def __init__(self):
        os.system('cls')
        self.data1 = pd.read_csv("cars.csv", sep=';')
        self.data2 = pd.read_csv("COVID19.csv")
        self.data3 = pd.read_csv("film.csv", sep=';',encoding='cp1252')
        self.data4 = pd.read_csv("Population.csv",encoding='cp1252')
        self.data5 = pd.read_csv("UKBank.csv")
        self.columnintvalue_list=[]
        self.columnfvalue_list = []
        self.sum_list = []
        self.valuelist =[]
        self.valuelist2 = []
        self.nlargestlist = []
        self.num_col_list =[]
        self.main()

    def main(self):
        os.system('cls')
        print('What do you want to do?\n1) Print Dataframe with Additional Information\n2) Print All Data File Summary Stats\n3) Rename A Column\n4) Convert dataframe to Series\n5) Normalize dataframe' + 
        '\n6) Min, 25th Percentile, Median, 75th Percentile & Max of Numeric Series\n7) Print dataframe as percentages\n8) Get the row number of the nth largest value in a column' + 
        '\n9) Create a bin of numeric series to 10 groups of equal size\n10) Get stack visualization of two series vertically and horizontally' + 
        '\n11) Get frequency counts of unique items of a series' + 
        '\n12) Compute the maximum possible correlation value of each column against other columns' + 
        '\n13) Create a column containing the minimum by maximum of each row\n99) More Pandas Examples\n00) Exit\n')
        main_option = int(input(''))
        if main_option == 1:
            self.print()
        elif main_option == 2:
            self.summary()
        elif main_option == 3:
            self.rename()
        elif main_option == 4:
            self.convertSeries()
        elif main_option == 5:
            self.normalize()
        elif main_option == 6:
            self.minMax()
        elif main_option == 7:
            self.percentage()
        elif main_option == 8:
            self.getRow()
        elif main_option == 9:
            self.createBin()
        elif main_option == 10:
            self.stackVisual()
        elif main_option == 11:
            self.freqUni()
        elif main_option == 12:
            self.correlation()
        elif main_option == 13:
            self.minByMax()
        elif main_option == 99:
            Examples().main()
        elif main_option == 00:
            quit
            os.system('cls')
        else:
            os.system('pause')
            self.main()

    def print(self):
        os.system('cls')
        r_option = int(input("How many rows do you want to display?\n"))
        c_option = int(input("\nHow many columns do you want to display?\n"))
        print_option = int(input('\nWhich data file do you want to load?\n1) Cars.csv\n2) Effects of COVID-19 on trade.csv\n3) Films.csv\n4) US Cities Population.csv\n5) UK Bank Customers.csv\n0) Return to menu\n'))
        if print_option == 1:
            df = self.data1
        elif print_option == 2:
            df = self.data2
        elif print_option == 3:
            df = self.data3
        elif print_option == 4:
            df = self.data4
        elif print_option == 5:
            df = self.data5
        elif print_option == 0:
            self.main()
        else:
            print('\nPlease select from the options provided!\n')
            os.system('pause')
            self.print()
        pd.set_option("display.max_columns", c_option)
        pd.set_option("display.max_rows", r_option)
        print('\n', df)
        print("\nOur df has a total of {} null values".format(df.isnull().sum().sum()))
        print("\nNull values:\n{}".format(df.isnull().sum()))
        print("\nDatatype:\n",df.dtypes)
        os.system('pause')
        self.print()

    def summary(self):
        os.system('cls')
        print("Cars.csv\n",self.data1.info)
        print("\nEffects of COVID-19 on trade.csv\n",self.data2.info)
        print("\nFilm.csv\n",self.data3.info)
        print("\nUS Cities Population.csv\n",self.data4.info)
        print("\nUK Bank Customers.csv\n",self.data5.info)
        os.system('pause')
        self.main()

    def rename(self):
        os.system('cls')
        option = int(input('Please select a datafile:\n1) Cars.csv\n2) Effects of COVID-19 on trade.csv\n3) Films.csv\n4) US Cities Population.csv\n5) UK Bank Customers.csv\n0) Return to menu\n'))
        if option == 1:
            df = self.data1
        elif option == 2:
            df= self.data2
        elif option == 3:
            df= self.data3
        elif option == 4:
            df= self.data4
        elif option == 5:
            df= self.data5
        elif option == 0:
            self.main()
        else:
            print('\nPlease select from the options provided!\n')
            os.system('pause')
        print("\nPlease select a column:\n")
        print(list(df.columns.values))
        col_option = int(input("\n"))
        new_name = str(input("\nNew column name:\n"))
        print('\n',df.rename(columns={ df.columns[col_option]: new_name }))
        os.system('pause')
        self.rename()

    def percentage(self):
        os.system('cls')
        print_option = int(input('Which data file do you want to load?\n1) Cars.csv\n2) US Cities Population.csv\n0) Return to menu\n'))
        if print_option == 1:
            df = self.data1
        elif print_option == 2:
            df = self.data5
        elif print_option == 0:
            self.main()
        else:
            print('\nPlease select from the options provided!\n')
            os.system('pause')
        self.findYear = pd.Series(df.columns).str.contains("Year").any()
        self.findCummulative = pd.Series(df.columns).str.contains("Cumulative").any()
        self.findCustomerID = pd.Series(df.columns).str.contains("Customer ID").any()
        self.findFLOATdtypes = df.dtypes[df.dtypes == np.float64]
        self.listofColumnsNames_float = list(self.findFLOATdtypes.index)
        self.findINTdtypes = df.dtypes[df.dtypes == np.int64]
        self.listofColumnsNames_int = list(self.findINTdtypes.index)
        if self.findYear == True:
            self.listofColumnsNames_int.remove("Year")
        else:
            pass
        if self.findCummulative == True:
            self.listofColumnsNames_int.remove("Cumulative")
        if self.findCustomerID ==True:
            self.listofColumnsNames_int.remove("Customer ID")
        if not self.listofColumnsNames_float:
            print("no decimal value")
        else:
            for i in range(len(self.listofColumnsNames_float)):
                self.columnfvalue = np.array(df[self.listofColumnsNames_float[i]])
                self.columnfvalue_list.append(self.columnfvalue)
                for j in range (len(self.columnfvalue_list)):
                    for k in range (len(self.columnfvalue_list[j])):
                        if self.columnfvalue_list[j][k]<1 :
                            self.valuelist.append(self.columnfvalue_list[j]*100)
                        else:
                            self.valuelist.append((self.columnfvalue_list[j]/df[self.listofColumnsNames_float[i]].sum())*100)
                df[self.listofColumnsNames_float[i]] = self.valuelist[i]
                df[self.listofColumnsNames_float[i]] =df[self.listofColumnsNames_float[i]].map(lambda n: "{0:.2f}%".format(n))
        if not self.listofColumnsNames_int :
            print("no integar value")
        else:
            for m in range(len(self.listofColumnsNames_int)):
                self.columnintvalue = np.array(df[self.listofColumnsNames_int[m]])
                self.columnintvalue_list.append(self.columnintvalue)
                for n in range(len(self.columnintvalue_list)):
                    self.sum = np.array(df[self.listofColumnsNames_int[n]].sum())
                self.sum_list.append(self.sum)
                self.valuelist2.append((self.columnintvalue_list[m]/self.sum_list[m])*100)
                df[self.listofColumnsNames_int[m]] = self.valuelist2[m]
                df[self.listofColumnsNames_int[m]] =df[self.listofColumnsNames_int[m]].map(lambda x: "{0:.2f}%".format(x))
        print(df)
        os.system('pause')
        self.percentage()

    def normalize(self):
        os.system('cls')
        print_option = int(input('Which data file do you want to load?\n1) Cars.csv\n2) Effects of COVID-19 on trade.csv\n3) Films.csv\n4) US Cities Population.csv\n5) UK Bank Customers.csv\n0) Return to menu\n'))
        if print_option == 1:
            df = self.data1
        elif print_option == 2:
            df = self.data2
        elif print_option == 3:
            df = self.data3
        elif print_option == 4:
            df = self.data4
        elif print_option == 5:
            df = self.data5
        elif print_option == 0:
            self.main()
        else:
            print('\nPlease select from the options provided!\n')
            os.system('pause')
            self.normalize()
        self.findFLOATdtypes = df.dtypes[df.dtypes == np.float64]
        self.listofColumnsNames_float = list(self.findFLOATdtypes.index)

        self.findINTdtypes = df.dtypes[df.dtypes == np.int64]
        self.listofColumnsNames_int = list(self.findINTdtypes.index)

        self.Comb_listofColumnsNames = self.listofColumnsNames_int + self.listofColumnsNames_float
        df[self.Comb_listofColumnsNames] = df[self.Comb_listofColumnsNames].apply(lambda x: ((x - np.mean(x)) / np.std(x)), axis=0)
        df[self.Comb_listofColumnsNames]=df[self.Comb_listofColumnsNames].apply(lambda x: ((x.max() - x)/(x.max() - x.min())).round(2))
        print(df)
        os.system('pause')
        self.normalize()

    def convertSeries(self):
        os.system('cls')
        print_option = int(input('Which data file do you want to load?\n1) Cars.csv\n2) Effects of COVID-19 on trade.csv\n3) Films.csv\n4) US Cities Population.csv\n5) UK Bank Customers.csv\n0) Return to menu\n'))
        if print_option == 1:
            df = self.data1
        elif print_option == 2:
            df = self.data2
        elif print_option == 3:
            df = self.data3
        elif print_option == 4:
            df = self.data4
        elif print_option == 5:
            df = self.data5
        elif print_option == 0:
            self.main()
        else:
            print('\nPlease select from the options provided!\n')
            os.system('pause')
            self.convertSeries()
        selection = int(input('\nConvert from:\n1) Dict to Series\n2) List to Series\n3) Array to Series\n'))
        dct = df.to_dict('dict')
        List = [df.columns.values.tolist()] + df.values.tolist()
        arr = np.array(List)
        if selection == 1:
            series = pd.Series(dct)
        elif selection == 2:
            series  = pd.Series(List)
        elif selection == 3:
            series = pd.Series(arr.tolist())
        print('\n', series)
        print('\nIndex of series as a column in dataframe:\n', series.to_frame().reset_index())
        os.system('pause')
        self.convertSeries()

    def minMax(self):
        os.system('cls')
        print_option = int(input('Which data file do you want to load?\n1) Cars.csv\n2) Effects of COVID-19 on trade.csv\n3) Films.csv\n4) US Cities Population.csv\n5) UK Bank Customers.csv\n0) Return to menu\n'))
        if print_option == 1:
            df = self.data1
        elif print_option == 2:
            df = self.data2
        elif print_option == 3:
            df = self.data3
        elif print_option == 4:
            df = self.data4
        elif print_option == 5:
            df = self.data5
        elif print_option == 0:
            self.main()
        else:
            print('\nPlease select from the options provided!\n')
            os.system('pause')
            self.minMax()
        self.serr_state_list=[]
        self.percentile_list =[]
        self.findFLOATdtypes = df.dtypes[df.dtypes == np.float64]
        self.listofColumnsNames_float = list(self.findFLOATdtypes.index)
        self.findINTdtypes = df.dtypes[df.dtypes == np.int64]
        self.listofColumnsNames_int = list(self.findINTdtypes.index)
        self.Comb_listofColumnsNames = self.listofColumnsNames_int + self.listofColumnsNames_float
        for i in range (len(self.Comb_listofColumnsNames)):
            self.serr_state = np.array(df[self.Comb_listofColumnsNames[i]])
            self.serr_state_list.append(self.serr_state)
            self.serr = pd.Series(self.serr_state_list[i])
            self.percentile_list.append(np.percentile(self.serr,q=[0, 25, 50, 75, 100]))
            print('\n',str(self.Comb_listofColumnsNames[i])+ " : "+ str(self.percentile_list[i]))
        os.system('pause')
        self.minMax()

    def getRow(self):
        os.system('cls')
        print_option = int(input('Which data file do you want to load?\n1) Cars.csv\n2) Effects of COVID-19 on trade.csv\n3) Films.csv\n4) US Cities Population.csv\n5) UK Bank Customers.csv\n0) Return to menu\n'))
        if print_option == 1:
            df = self.data1
        elif print_option == 2:
            df = self.data2
        elif print_option == 3:
            df = self.data3
        elif print_option == 4:
            df = self.data4
        elif print_option == 5:
            df = self.data5
        elif print_option == 0:
            self.main()
        else:
            print('\nPlease select from the options provided!\n')
            os.system('pause')
            self.getRow()
        self.Comb_listofColumnsNames =[]
        self.nlargestlist = []
        self.rowindexlist=[]
        self.findFLOATdtypes = df.dtypes[df.dtypes == np.float64]
        self.listofColumnsNames_float = list(self.findFLOATdtypes.index)
        self.findINTdtypes = df.dtypes[df.dtypes == np.int64]
        self.listofColumnsNames_int = list(self.findINTdtypes.index)
        self.Comb_listofColumnsNames=self.listofColumnsNames_int + self.listofColumnsNames_float
        print("Enter the n-th largest value in a column : ")
        x =int(input())
        for i in range (len(self.Comb_listofColumnsNames)):
            nlargest = df[self.Comb_listofColumnsNames[i]].nlargest(x).iloc[-1]
            self.nlargestlist.append(nlargest)
            self.rowindexlist.append(df[df[self.Comb_listofColumnsNames[i]]==self.nlargestlist[i]].index[0])
        print("Largest value : " + str(self.nlargestlist))
        print("Row Index Number : " + str(self.rowindexlist)+"\n")
        os.system('pause')
        self.getRow()

    def createBin(self):
        os.system('cls')
        option = int(input('Please select a datafile:\n1) Cars.csv\n2) Effects of COVID-19 on trade.csv\n3) Films.csv\n4) US Cities Population.csv\n5) UK Bank Customers.csv\n0) Return to menu\n'))
        if option == 1:
            df = self.data1
        elif option == 2:
            df= self.data2
        elif option == 3:
            df= self.data3
        elif option == 4:
            df= self.data4
        elif option == 5:
            df= self.data5
        elif option == 0:
            self.main()
        else:
            print('\nPlease select from the options provided!\n')
            os.system('pause')
        self.Comb_listofColumnsNames = []
        self.findFLOATdtypes = df.dtypes[df.dtypes == np.float64]
        self.listofColumnsNames_float = list(self.findFLOATdtypes.index)
        self.findINTdtypes = df.dtypes[df.dtypes == np.int64]
        self.listofColumnsNames_int = list(self.findINTdtypes.index)
        self.Comb_listofColumnsNames = self.listofColumnsNames_int + self.listofColumnsNames_float
        for i in range (len(self.Comb_listofColumnsNames)):
            print(pd.qcut(df[self.Comb_listofColumnsNames[i]],q=10,duplicates='drop'))
        os.system('pause')
        self.createBin()

    def stackVisual(self):
        os.system('cls')
        option = int(input('Please select a datafile:\n1) Cars.csv\n2) Effects of COVID-19 on trade.csv\n3) Films.csv\n4) US Cities Population.csv\n5) UK Bank Customers.csv\n0) Return to menu\n'))
        if option == 1:
            df = self.data1
        elif option == 2:
            df= self.data2
        elif option == 3:
            df= self.data3
        elif option == 4:
            df= self.data4
        elif option == 5:
            df= self.data5
        elif option == 0:
            self.main()
        else:
            print('\nPlease select from the options provided!\n')
            os.system('pause')
        dfforstack = df
        List = [df.columns.values.tolist()] + df.values.tolist()
        List2 = [dfforstack.columns.values.tolist()] + dfforstack.values.tolist()
        series1 = pd.Series(List)
        series2 = pd.Series(List2)
        series1.append(series2)
        print(pd.concat([series1,series2],axis=1))
        os.system('pause')
        self.stackVisual()

    def freqUni(self):
        os.system('cls')
        option = int(input('Please select a datafile:\n1) Cars.csv\n2) Effects of COVID-19 on trade.csv\n3) Films.csv\n4) US Cities Population.csv\n5) UK Bank Customers.csv\n0) Return to menu\n'))
        if option == 1:
            df = self.data1
        elif option == 2:
            df= self.data2
        elif option == 3:
            df= self.data3
        elif option == 4:
            df= self.data4
        elif option == 5:
            df= self.data5
        elif option == 0:
            self.main()
        else:
            print('\nPlease select from the options provided!\n')
            os.system('pause')
        self.seriesforDATA_list=[]
        for i in range(len(df.columns)):
            self.seriesforDATA = pd.Series(np.array(df[df.columns[i]]))
            self.seriesforDATA_list.append(self.seriesforDATA)
            self.result = self.seriesforDATA_list[i].value_counts()
            print(df.columns[i])
            print(self.result)
        os.system('pause')
        self.freqUni()

    def correlation(self):
        os.system('cls')
        option = int(input('Please select a datafile:\n1) Cars.csv\n2) Effects of COVID-19 on trade.csv\n3) Films.csv\n4) US Cities Population.csv\n5) UK Bank Customers.csv\n0) Return to menu\n'))
        if option == 1:
            df = self.data1
        elif option == 2:
            df= self.data2
        elif option == 3:
            df= self.data3
        elif option == 4:
            df= self.data4
        elif option == 5:
            df= self.data5
        elif option == 0:
            self.main()
        else:
            print('\nPlease select from the options provided!\n')
            os.system('pause')
        df_corr =np.abs(df.corr())
        max_corr = df_corr.apply(lambda x: sorted(x)[-2], axis=0)
        print(max_corr)
        os.system('pause')
        self.correlation()

    def minByMax(self):
        os.system('cls')
        option = int(input('Please select a datafile:\n1) Cars.csv\n2) Effects of COVID-19 on trade.csv\n3) Films.csv\n4) US Cities Population.csv\n5) UK Bank Customers.csv\n0) Return to menu\n'))
        if option == 1:
            df = self.data1
        elif option == 2:
            df= self.data2
        elif option == 3:
            df= self.data3
        elif option == 4:
            df= self.data4
        elif option == 5:
            df= self.data5
        elif option == 0:
            self.main()
        else:
            print('\nPlease select from the options provided!\n')
            os.system('pause')
        self.findFLOATdtypes = df.dtypes[df.dtypes == np.float64]
        self.listofColumnsNames_float = list(self.findFLOATdtypes.index)
        self.findINTdtypes = df.dtypes[df.dtypes == np.int64]
        self.listofColumnsNames_int = list(self.findINTdtypes.index)
        self.Comb_listofColumnsNames = self.listofColumnsNames_int + self.listofColumnsNames_float
        min_by_max = np.min(df[self.Comb_listofColumnsNames], axis=1) / np.max(df[self.Comb_listofColumnsNames], axis=1)
        print(min_by_max)
        os.system('pause')
        self.minByMax()

class Examples(object):
    def main(self):
        os.system('cls')
        print('Which example do you want to see?\n1) Replace missing spaces in a string with the least frequent character\n2) Find the position of the nth largest value greater than a give value\n3) Reshape dataframe to the largest possible square after removing the negative values' + 
        '\n4) Compute columns with the highest number of row-wise maximum values\n5) Replace missing values with mean\n99)Back\n00) Quit\n')
        example_option = int(input(''))
        if example_option == 1:
            self.replaceString()
        elif example_option == 2:
            self.findPosition()
        elif example_option == 3:
            self.reshape()
        elif example_option == 4:
            self.rowWiseMax()
        elif example_option == 5:
            self.replaceByMean()
        elif example_option == 99:
            Assingment().main()
        elif example_option == 00:
            quit
        else:
            os.system('pause')
            self.main()

    def replaceString(self):
        my_str = "dbc deb abed ggade"
        ser = pd.Series(list(my_str.replace(" ","")))
        ser.value_counts()
        minimum = list(ser.value_counts().index)[-1]
        print("\nOriginal string: " + my_str)
        print("New string: " + my_str.replace(" ",minimum))
        os.system('pause')
        self.main()

    def findPosition(self):
        ser = pd.Series(np.random.randint(1, 100, 15))
        print('\nLets find the position of the 2nd largest value greater than the mean')
        print('ser: ', ser.tolist(), '\nmean: ', round(ser.mean()))
        print(ser[ser > ser.mean()].index[1])
        os.system('pause')
        self.main()

    def reshape(self):
        df = pd.DataFrame(np.random.randint(-20, 50, 100).reshape(10,-1))
        my_array = np.array(df.values.reshape(-1, 1))
        my_array = my_array[my_array > 0]
        lar_square = int(np.floor(my_array.shape[0]**0.5))
        arg_sort = np.argsort(my_array)[::-1][0:lar_square**2]
        my_array = np.take(my_array, sorted(arg_sort)).reshape(lar_square, lar_square)
        print('Before reshape:\n', df)
        print('\nAfter reshape:\n', my_array)
        os.system('pause')
        self.main()

    def rowWiseMax(self):
        df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1))
        print(df)
        print('\nColumn with highest row maxes: ', df.apply(np.argmax, axis=1).value_counts().index[0])
        os.system('pause')
        self.main()

    def replaceByMean(self):
        df = pd.read_csv('Cars93.csv')
        print('Original Null Values: ', df.isnull().sum().sum())
        df[["Luggage.room"]] = df[["Luggage.room"]].apply(lambda x: x.fillna(x.mean()))
        print('Final Null Values: ', df.isnull().sum().sum())
        os.system('pause')
        self.main()

Assingment()
