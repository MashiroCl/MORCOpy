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
        print(file_list)
        for eachFile in file_list:
            with open(eachFile) as f:
                lines = f.readlines()
            single_iteration = list()
            for eachLine in lines:
                onePopulation = eachLine.split(" ")
                single_iteration.append(onePopulation)
            fronts.append(single_iteration)
        return fronts

    def plot_all_objectives_in_subplots(self,frontPath,outputPath):
        fronts = self._read_from_Fronts(frontPath)
        objectives_fronts = []

        for i in range(6):
            temp = []
            for eachFront in fronts:
                temp.append(float(eachFront[49][i]))
            objectives_fronts.append(temp)
        plt.figure(figsize=(10, 5))
        for i in range(6):
            # plt.subplot(2, 4, i + 1)
            plt.subplot(2, 3, i + 1)
            plt.scatter(range(len(objectives_fronts[i])), objectives_fronts[i], s=3)
        plt.subplots_adjust(left=0, right=1, wspace=0.3, hspace=0.3)
        plt.tight_layout()
        plt.savefig(outputPath,dpi=500)


if __name__ =="__main__":
    frontPath = sys.argv[1]
    outputPath = sys.argv[2]
    Plot().plot_all_objectives_in_subplots(frontPath,outputPath)
