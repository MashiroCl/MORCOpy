import sys
sys.path.append('../')
from jmetal.operator import IntegerPolynomialMutation
from jmetal.operator.crossover import IntegerSBXCrossover
from jmetal.util.solution import get_non_dominated_solutions, print_function_values_to_file, print_variables_to_file
from jmetal.algorithm.multiobjective import NSGAII
from jmetal.algorithm.multiobjective import RandomSearch
from jmetal.util.termination_criterion import StoppingByEvaluations
from utils import readJson
from Jxplatform2.jClass import jClass
from SearchROProblemInteger import SearchROProblemInteger
from jmetal.lab.visualization import Plot,InteractivePlot
from jmetal.util.observer import WriteFrontToFileObserver,PlotFrontToFileObserver,ProgressBarObserver,BasicObserver


'Read Jxplatform2 extraction result'
# jsonFile = "/Users/leichen/Desktop/jedis.json"
# repoPath = "/Users/leichen/ResearchAssistant/InteractiveRebase/data/jedis"
# repoName = "ganttproject-1.10.2"
repoName = sys.argv[1]
max_evaluations = sys.argv[2]
platform = sys.argv[3]

if platform == "1":
    'Local'
    max_evaluations = 500
    repoName = "ganttproject-1.10.2"
    jsonFile = "/Users/leichen/Desktop/" +repoName +".json"
    repoPath = "/Users/leichen/ResearchAssistant/InteractiveRebase/data/" + repoName
    outputPath = "/Users/leichen/Desktop/output"

elif platform == "2":
    'Server'
    jsonFile = "/home/chenlei/MORCO/extractResult/" + repoName + ".json"
    repoPath = "/home/chenlei/MORCO/data/" + repoName
    outputPath = "/home/chenlei/MORCO/output_all_objectives_positive/"


load = readJson(jsonFile)
jClist = []
for each in load:
    jClist.append(jClass(load=each))
# print(jClist)

problem = SearchROProblemInteger(jClist,repoPath)

# max_evaluations=5000
algorithm = RandomSearch(
    problem=problem,
    # population_size=50,
    # offspring_population_size=50,
    # mutation=IntegerPolynomialMutation(probability=0.15),
    # crossover=IntegerSBXCrossover(probability=0.8),
    termination_criterion=StoppingByEvaluations(max_evaluations=int(max_evaluations))
)
# algorithm.observable.register(observer=PlotFrontToFileObserver('dynamic_front_vis'))
# algorithm.observable.rfegister(observer=WriteFrontToFileObserver('dynamic_front'))
# algorithm.observable.register(observer=WriteFrontToFileObserver(output_directory="/Users/leichen/Code/pythonProject/pythonProject/salabResearch/jMetal/FrontData"))
algorithm.observable.register(observer=BasicObserver())
# algorithm.observable.register(observer=ProgressBarObserver(max=max_evaluations))
algorithm.observable.register(observer=WriteFrontToFileObserver(
    output_directory=outputPath+repoName+"/front"))
algorithm.run()

front = algorithm.get_result()
# solutionObjectives = "/Users/leichen/Code/pythonProject/pythonProject/salabResearch/jMetal/solutionObjectives.txt"
# with open(solutionObjectives,"w") as f:
#     json.dump(problem.mySolutions,f)


# problem.reference_front = problem.initial_front
# plot_front = Plot(title='Pareto front approximation'
#                   , axis_labels=problem.obj_labels
#                   , reference_front=problem.reference_front)
# plot_front.plot(front, label='NSGAII', filename=algorithm.get_name())


# save to files
print_function_values_to_file(front, outputPath+repoName+'/FUN.NSGAII.SearchRO')
print_variables_to_file(front, outputPath+repoName+'/VAR.NSGAII.SearchRO')

print('Algorithm (continuous problem): ' + algorithm.get_name())
print('Problem: ' + problem.get_name())
print('Computing time: ' + str(algorithm.total_computing_time))