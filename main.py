from string import ascii_lowercase


class UserInput():
    '''Request user input that will be used in logic operators.'''

    def __init__(self):
        '''Initialize user input class.'''
        self.var_list = var_list

    def create_variables(self):
        '''Create variables to be used in each method.'''
        self.var_list = [] # List of all variables a-z; will scale for more
        for var in ascii_lowercase:
            self.var_list.append(var) # add a-z to var_list

    def req_pair_amt(self):
        '''Request the amount of boolean pairs to test for.'''
        #request how many pairs
        #assign each pair to a variable i.e. pair_a, pair_b w/ for loop

    def req_input_amt(self):
        '''Request the amount of inputs in each pair.'''
        #pair_a will have arbitrary number of inputs
        #pair_b will have different number of inputs

    def input_vals(self):
        '''Input the boolean values in each pair.'''
        #Pair A (Input 5 boolean vals): 01100
        #Check to make sure values are the amount requested for the pair
        #Check to make sure values are 0 or 1
        #return pairs in dict w/ vals attached

#    def req_operators(self):
#        '''Request which operators to be tested on for each pair.'''
#        #Which operators for each pair?


class LogicOperators():
    '''Logic Operators and output for each scalable w/
    multiple inputs: AND, OR, XOR, NAND, NOR, XNOR, NOT'''

    def __init__(self, logic_dict)
        self.logic_dict = logic_dict
        self.logic_pair = logic_pair

    def and_operator(self):
        #take pair from dict and test
        while self.logic_pair:
            val = self.logic_pair.pop(0)
            if val == 1:
                continue
            elif val == 0:
                return(0)
                print("out: " + str(0))
            if self.logic_pair = []:
                return(1)
                print("out: " + str(1))


class ConnectOperators(LogicOperators):


class OutputTable(ConnectOperators):





















