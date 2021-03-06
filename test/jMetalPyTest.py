from IntegerEncoding import SubsetSum
from jmetal.algorithm.singleobjective.genetic_algorithm import GeneticAlgorithm
from jmetal.operator import IntegerPolynomialMutation
from jmetal.operator.selection import BinaryTournamentSelection
from jmetal.operator.crossover import IntegerSBXCrossover
from jmetal.util.termination_criterion import StoppingByEvaluations

if __name__ == '__main__':
    C = 9
    W = [3,34,4,12,5,2]

    problem = SubsetSum(C, W)

    algorithm = GeneticAlgorithm(
        problem=problem,
        population_size=4,
        offspring_population_size=4,
        mutation=IntegerPolynomialMutation(probability=0.5),
        crossover=IntegerSBXCrossover(probability=0.5),
        selection=BinaryTournamentSelection(),
        termination_criterion=StoppingByEvaluations(max_evaluations=5*100)
    )

    algorithm.run()
    subset = algorithm.get_result()

    print('Algorithm: {}'.format(algorithm.get_name()))
    print('Problem: {}'.format(problem.get_name()))
    print('Solution: {}'.format(subset.variables))
    print('Fitness: {}'.format(subset.objectives[0]))
    print('Computing time: {}'.format(algorithm.total_computing_time))