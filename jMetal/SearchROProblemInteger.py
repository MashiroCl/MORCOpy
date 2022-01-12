from jmetal.core.problem import IntegerProblem
from jmetal.core.solution import IntegerSolution
import random
from CodeOwnership.CodeOwnership import  CodeOwnership
from Encoding.IntegerEncoding import IntegerEncoding
from RefactoringOperation.RefactoringOperationDispatcher import dispatch
from QMOOD.Qmood import Qmood
import copy

class SearchROProblemInteger(IntegerProblem):
    def __init__(self,projectInfo,repoPath):
        '''
        set basic parameters and encode current project
        :param projectInfo: project being processed, should be a list of jClass
        :param repository: repository of project being processed, used to do code ownership related manipulation,
        should be a entity of class Repository
        '''
        super(SearchROProblemInteger,self).__init__()
        "8 objectives: QMOOD 6 metrics + highest ownership+# of commiters"
        # self.number_of_objectives = 8
        self.number_of_objectives = 6
        "Length represents chromosome length"
        self.number_of_variables = 4
        # todo: Research on what are contraints for
        "No contraints"
        self.number_of_constraints = 0
        "number of chromosome"
        self.number_of_choromosome = 100

        'Qmood: maximize    code ownership: maximize'
        self.obj_directions=[self.MAXIMIZE,
                             self.MAXIMIZE,
                             self.MAXIMIZE,
                             self.MAXIMIZE,
                             self.MAXIMIZE,
                             self.MAXIMIZE,
                             self.MAXIMIZE,
                             self.MAXIMIZE]
        # self.obj_directions=[self.MINIMIZE,
        #                      self.MINIMIZE,
        #                      self.MINIMIZE,
        #                      self.MINIMIZE,
        #                      self.MINIMIZE,
        #                      self.MINIMIZE,
        #                      self.MINIMIZE,
        #                      self.MINIMIZE]
        self.obj_labels=['Effectiveness',
                         'Extendibility',
                         'Flexibility',
                         'Functionality',
                         'Resusability',
                         'Understandability',
                         'HighestOwnership',
                         'NumOfCommiters']
        self.projectInfo = projectInfo
        self.codeOwnership = CodeOwnership(repoPath)
        self.integerEncoding = IntegerEncoding()
        self.integerEncoding.encoding(self.projectInfo)
        self.lower_bound=[1, 1, 1, 1] *self.number_of_choromosome
        self.upper_bound=[self.integerEncoding.ROTypeNum,
                          self.integerEncoding.classNum,
                          self.integerEncoding.classNum,
                          self.integerEncoding.N]*self.number_of_choromosome
        # self.initial_front= []
        # print(self.upper_bound)
        self.initial_objectives = Qmood().calculateQmood(self.projectInfo)

    def evaluate(self, solution: IntegerSolution) -> IntegerSolution:
        # print(solution.variables)
        'Decode and execute'
        decodedIntegerSequences = self.integerEncoding.decoding(solution.variables)
        "Execute corressponding refactoring operations"

        projectInfo = copy.deepcopy(self.projectInfo)
        for each in decodedIntegerSequences:
            # print("Refactoring Operation: ", each)
            dispatch(each["ROType"].value)(each, projectInfo)

        'calculate QMOOD  after executed refactoring operations'
        qmood = Qmood()
        qmood.calculateQmood(projectInfo)
        effectiveness = qmood.getEffectiveness()
        extendibility = qmood.getExtendibility()
        flexibility = qmood.getFlexibility()
        functionality = qmood.getFunctionality()
        resusability = qmood.getResusability()
        understandability = qmood.getUnderstandability()

        minus = -1.0

        solution.objectives[0] = minus * (effectiveness - self.initial_objectives["Effectiveness"])
        solution.objectives[1] = minus * (extendibility - self.initial_objectives["Extendibility"])
        solution.objectives[2] = minus * (flexibility - self.initial_objectives["Flexibility"])
        solution.objectives[3] = minus * (functionality - self.initial_objectives["Functionality"])
        solution.objectives[4] = minus * (resusability - self.initial_objectives["Resusability"])
        solution.objectives[5] = minus * (understandability - self.initial_objectives["Understandability"])

        # solution.objectives[0] = minus * effectiveness if effectiveness<0 else effectiveness
        # solution.objectives[1] = minus * extendibility if extendibility<0 else extendibility
        # solution.objectives[2] = minus * flexibility if flexibility<0 else flexibility
        # solution.objectives[3] = minus * functionality if functionality<0 else functionality
        # solution.objectives[4] = minus * resusability if resusability<0 else resusability
        # solution.objectives[5] = minus * understandability if understandability<0 else understandability
        # print(solution)

        # 'calculate ownership on refactoring operations applied files'
        # highestOwnership, numOfCommiters = self.codeOwnership.calculateOwnership(decodedIntegerSequences)
        # # print("highestOwnership: ",highestOwnership)
        # # print("numOfCommiters: ",numOfCommiters)
        # solution.objectives[6] = minus * highestOwnership/self.initial_objectives[0]
        # solution.objectives[7] = minus * numOfCommiters/self.initial_objectives[0]

        # self.initial_solution.append(solution.objectives)
        return solution

    def create_solution(self) -> IntegerSolution:
        newSolution = IntegerSolution(lower_bound=self.lower_bound,
                                      upper_bound=self.upper_bound,
                                      number_of_objectives=self.number_of_objectives,
                                      number_of_constraints=self.number_of_constraints)

        newSolution.variables = \
            [int(random.uniform(self.lower_bound[i] * 1.0, self.upper_bound[i] * 1.0))
             for i in range(self.number_of_variables*self.number_of_choromosome)]
        # self.initial_front.append(self.evaluate(newSolution))
        return newSolution

    def get_name(self) -> str:
        return "Search Refactoring Operation Problem"