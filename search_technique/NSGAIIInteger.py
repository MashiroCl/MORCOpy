import sys
sys.path.append("../")
from jmetal.operator import IntegerPolynomialMutation
from jmetal.operator.crossover import IntegerSBXCrossover
from jmetal.util.solution import get_non_dominated_solutions, print_function_values_to_file, print_variables_to_file
from jmetal.algorithm.multiobjective import NSGAII
from jmetal.util.termination_criterion import StoppingByEvaluations
from jmetal.util.observer import WriteFrontToFileObserver, BasicObserver
from code_ownership.DeveloperGraph import DeveloperGraph
from code_ownership.PullRequestService import PullRequestService
from jxplatform2.jClass import jClass
from search_technique.SearchROProblemRE import SearchROProbleRE
from call_graph.CallGraph import CallGraph
from utils import readJson

def load_args():
    'Read Jxplatform2 extraction result'
    repoName = sys.argv[1]
    max_evaluations = sys.argv[2]
    platform = sys.argv[3]
    return repoName, max_evaluations, platform


def select_platform(repoName, platform):
    """select to run on local: 1 or on server: 2"""
    if platform == "1":
        'Local'
        jsonFile = "/Users/leichen/Desktop/StaticalAnalysis/" + repoName + ".json"
        repoPath = "/Users/leichen/ResearchAssistant/InteractiveRebase/data/" + repoName
        outputPath = "/Users/leichen/Desktop/output/"
        # load developer relationship
        relationshipCsvPath = "/Users/leichen/ResearchAssistant/InteractiveRebase/data/"+repoName+"/MORCOoutput/csv/pullrequest.csv"
        res = PullRequestService().loadPullRequest(relationshipCsvPath)
        developerGraph = DeveloperGraph(res).generate_vertices().build()
        ownershipPath = "/Users/leichen/ResearchAssistant/InteractiveRebase/data/" + repoName + "/MORCOoutput/csv/ownership.csv"
        callGraph = CallGraph("/Users/leichen/ResearchAssistant/InteractiveRebase/data/" + repoName + "/MORCOoutput/csv/callgraph.json")

    elif platform == "2":
        'Server'
        jsonFile = "/home/chenlei/MORCO/extractResult/" + repoName + ".json"
        repoPath = "/home/chenlei/MORCO/data/" + repoName
        outputPath = "/home/chenlei/MORCO/output_temp/"
        # load developer relationship
        relationshipCsvPath = "/home/chenlei/MORCO/relationship/" + repoName + "/pullrequest.csv"
        res = PullRequestService().loadPullRequest(relationshipCsvPath)
        developerGraph = DeveloperGraph(res).generate_vertices().build()
        ownershipPath = "/home/chenlei/MORCO/relationship/" + repoName + "/ownership.csv"
        callGraph = CallGraph("/home/chenlei/MORCO/relationship/" + repoName + "/callgraph.json")


    return jsonFile, repoPath, outputPath, developerGraph, ownershipPath, callGraph


def exclude_test_class(exclude: bool, javaClasses):
    """exclude test_class"""
    res = []
    if exclude:
        for each in javaClasses:
            if not each.testClass:
                res.append(each)
    else:
        for each in javaClasses:
            res.append(each)
    return res

def exclude_anonymous_class(exclude: bool, javaClasses):
    """ exclude anonymous class"""
    res = []
    if exclude:
        for each in javaClasses:
            if not each.anonymous_class:
                res.append(each)
    else:
        for each in javaClasses:
                res.append(each)
    return res

def json_2_jClass(jsonList):
    res = []
    for each in jsonList:
        res.append(jClass(each))
    return res


def load_repository(jsonFile: str, exclude_test: bool, exclude_anonymous: bool=False):
    # load repository class info
    load = readJson(jsonFile)
    javaClasses = json_2_jClass(load)
    javaClasses = exclude_test_class(exclude=exclude_test, javaClasses=javaClasses)
    javaClasses = exclude_anonymous_class(exclude = exclude_anonymous, javaClasses = javaClasses)
    return javaClasses


if __name__ =="__main__":
    repoName, max_evaluations, platform = load_args()
    jsonFile, repoPath, outputPath, developerGraph, ownershipPath, callGraph = select_platform(repoName, platform)
    jClist = load_repository(jsonFile=jsonFile, exclude_test=True, exclude_anonymous=True)

    problem = SearchROProbleRE(jClist, repoPath, developerGraph, ownershipPath, callGraph)

    algorithm = NSGAII(
        problem=problem,
        population_size=100,
        offspring_population_size=100,
        mutation=IntegerPolynomialMutation(probability=0.5),
        crossover=IntegerSBXCrossover(probability=1),
        termination_criterion=StoppingByEvaluations(max_evaluations=int(max_evaluations))
    )

    algorithm.observable.register(observer=BasicObserver())
    algorithm.observable.register(observer=WriteFrontToFileObserver(
        output_directory=outputPath + repoName + "/front"))
    algorithm.run()
    front = get_non_dominated_solutions(algorithm.get_result())

    # save to files
    print_function_values_to_file(front, outputPath + repoName + '/FUN.NSGAII.SearchRO')
    print_variables_to_file(front, outputPath + repoName + '/VAR.NSGAII.SearchRO')

    print('Algorithm (continuous problem): ' + algorithm.get_name())
    print('Problem: ' + problem.get_name())
    print('Computing time: ' + str(algorithm.total_computing_time))
