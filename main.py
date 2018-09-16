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


class LogicalOperators():
    '''Logical Operators and output for each scalable w/
    multiple inputs: AND, OR, XOR, NAND, NOR, XNOR, NOT'''

    def __init__(self, logic_dict)
        self.logic_dict = logic_dict
        self.logic_list = logic_list

    def and_operator(self):
        #take list from dict and test
        #if 10 nums in list take length of list then add nums in list to see if it equals length of list
        sum_logic_list = sum(self.logic_list)
        len_logic_list = len(self.logic_list)
        if len_logic_list == sum_logic_list:
            return(1)
            print("Out: " + str(1))
        elif len_logic_list != sum_logic_list:
            return(0)
            print("Out: " + str(0))
    
    def or_operator(self)
        


class ConnectOperators(LogicalOperators):


class OutputTable(ConnectOperators):





















