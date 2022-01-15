import glob
import matplotlib.pyplot as plt
import sys
class Plot():
    def _read_from_Fronts(self,frontPath):
        '''
        read data in front files
        :param frontPath:
        :return:
        '''
        file_list = glob.glob(frontPath+"/*.*")
        file_list.sort(key=lambda s:int(s.split(".")[-1]))
        fronts=list()
        # print(file_list)
        for eachFile in file_list:
            with open(eachFile) as f:
                lines = f.readlines()
            single_iteration = list()
            for eachLine in lines:
                onePopulation = eachLine.split(" ")[:-1]
                single_iteration.append(onePopulation)
            fronts.append(single_iteration)
        return fronts

    def _extract_feature(self,list_of_list):
        '''
        eg. [[1,2],[a,b],[c,d]] ->[[1,a,c],[2,b,d]]
        :param list_of_list:
        :return:
        '''
        res_list = None
        try:
            res_list = [list() for i in range(len(list_of_list[0]))]
            for row in range(len(list_of_list)):
                for column in range(len(res_list)):
                    res_list[column].append(list_of_list[row][column])
        except TypeError:
            print("Input type error, it should be a 2d array")

        return res_list

    def plot_all_objectives_in_subplots_2(self,frontPath,outputPath):
        fronts = self._read_from_Fronts(frontPath)
        objectives_fronts = []
        for i in range(2):
            temp = []
            for eachFront in fronts:
                temp.append(float(eachFront[119][i]))
            objectives_fronts.append(temp)
        plt.figure(figsize=(10, 5))
        for i in range(2):
            plt.subplot(1, 2, i + 1)
            plt.scatter(range(len(objectives_fronts[i])), objectives_fronts[i], s=3)
            plt.xlabel("iteration number")
            plt.ylabel("value of 199th population")
        plt.subplots_adjust(left=0, right=1, wspace=0.3, hspace=0.3)
        plt.tight_layout()
        plt.savefig(outputPath,dpi=500)


    def plot(self,frontPath, titles,show=False):
        fronts = self._read_from_Fronts(frontPath)
        # print(fronts[0])
        front_49 = [ front[49] for front in fronts]
        metrics = self._extract_feature(front_49)
        # print(metrics)
        num_of_subplot = len(metrics)
        fig = plt.figure(figsize=(8, 6))
        for i in range(num_of_subplot):
            ax = fig.add_subplot(2,4,i+1)
            # print(metrics[i])
            ax.scatter(range(len(metrics[i])),metrics[i])

            ax.set_title("objective ".format(titles[i]),size=10)
            ax.set_xlabel("iteration number", size = 8)
            ax.set_ylabel("value of 199th population")

        if show:
            plt.show()

        return fig


if __name__ =="__main__":
    frontPath = sys.argv[1]
    outputPath = sys.argv[2]
    Plot().plot_all_objectives_in_subplots_2(frontPath,outputPath)
