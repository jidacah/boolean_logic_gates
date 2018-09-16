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

#split up sum and length of lists later
class LogicalOperators():
    '''Logical Operators and output for each scalable w/
    multiple inputs: AND, OR, XOR, NAND, NOR, XNOR, NOT'''

    def __init__(self, logic_dict):
        self.logic_dict = logic_dict
        self.logic_list = logic_list

    def logic_list_basics(self):
        '''Perform basic operations used in later
        methods for logic lists. Run before using
        other operators and methods.'''
        #take list from dictionary
        

        self.sum_logic_list = sum(self.logic_list)
        self.len_logic_list = len(self.logic_list)

    def return_true_value(self):
        '''Return & print true/high value.'''
        return(1)
        print("Out: " + str(1))

    def return_false_value(self):
        '''Return & print false/low value.'''
        return(0)
        print("Out: " + str(0))

    def and_operator(self):
        '''Perform the OR operator on the boolean list.
        True if all inputs are true.'''
        if self.len_logic_list == self.sum_logic_list:
            self.return_true_value()
        elif self.len_logic_list != self.sum_logic_list:
            self.return_false_value()
    
    def or_operator(self):
        '''Perform the OR operator on the boolean list.
        True if any input is true.'''
        if self.len_logic_list == self.sum_logic_list or self.len_logic_list != self.sum_logic_list:
            self.return_true_value()
        elif self.len_logic_list == 0:
            self.return_false_value()

    def xor_operator(self):
        '''Perform the XOR operator on the boolean list.
        True if odd number of inputs are true.'''
        if self.sum_logic_list % 2 == 1:
            self.return_true_value()
        elif self.sum_logic_list % 2 == 0:
            self.return_false_value()

    def nand_operator(self):
        '''Perform the NAND operator on the boolean list.
        False if all inputs are true.'''
        if self.len_logic_list != self.sum_logic_list:
            self.return_true_value()
        elif self.len_logic_list == self.sum_logic_list:
            self.return_false_value()

    def nor_operator(self):
        '''Perform the NOR operator on the boolean list.
        True if all inputs are false.'''
        if self.sum_logic_list == 0:
            self.return_true_value()
        elif self.sum_logic_list > 0:
            self.return_false_value()

    def xnor_operator(self):
        '''Perform the XNOR operator on the boolean list.
        True if even number of inputs are true.'''
        if self.sum_logic_list % 2 == 0:
            self.return_true_value()
        elif self.sum_logic_list % 2 == 1:
            self.return_false_value()

    def not_operator(self):
        '''Perform the NOT operator on a boolean.
        Only operates on unary values.
        Inverses the value given.'''
        if self.sum_logic_list > 1:
            print("Error: NOT Gate can only take one value.")
        elif self.sum_logic_list == 1:
            self.return_true_value()
        elif self.sum_logic_list == 0:
            self.return_false_value()


class ConnectOperators(LogicalOperators):


class OutputTable(ConnectOperators):
    




















