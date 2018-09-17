from string import ascii_lowercase


class UserInput():
    '''Request user input that will be used in logic operators.'''

    def __init__(self):
        '''Initialize user input class.'''
        self.var_list = var_list # list of variables
        self.in_amt = in_amt # input amount
        self.op_amt = op_amt # operator amount
        self.out_amt = out_amt # output amount

    def create_variables(self):
        '''Create variables to be used in each method.'''
        self.var_list = [] # List of all variables a-z; will scale for more
        for var in ascii_lowercase:
            self.var_list.append(var) # add a-z to var_list

    def object_amount(self):
        '''Request user how many objects in circuit.
        Inputs, Operators, Outputs.'''
        self.in_amt = int(input("How many inputs: "))
        self.op_amt = int(input("How many operators: "))
        self.out_amt = int(input("How many outputs: "))

    def object_variables(self):
        '''Assign variables to each object.
        Inputs, Operators, Outputs.'''
        #add dictionary w/ empty values but keys for
        #each input, operator, & output

    # use letters for output variables; out_x, out_y
    # use numbers for operators; op_1, op_2
    # use letters for inputs; in_a, in_b

    # define amt of inputs, operators, outputs
    # assign variables to each object ^
    # what will inputs connect to:
    #(in_b -> op_d(NOT)), (in_a -> op_1(XOR)), (in_c -> op_b(NOT))
    #print each operator var with corresponding op(and,or,etc) before user has to input
    # what will operators connect to:
    #print each operator var with corresponding op(and,or,etc) before user has to input
    #plus current connections
    #(op_a(XOR) -> out_x, op_b(NOR)), (op_d(NOT) -> op_a(XOR), op_e(NOT)),
    #(op_b(NOR) -> out_y, op_c(AND)), (op_e(NOT) -> op_c(AND)), (op_c -> out_z)
    # refer to pics for logic gate referred to these connections
    # compute outputs

    # possibly use 4 objects: input, operator, output, & layers(max connections btwn operators & outputs)
    #i.e. use 2 layers for only i/o, use 3 for i -> op -> o, use 4 for i -> op -> op -> o.

# make general class that declares all the variables for each object;
# use inheritance for each object and their functions
# input for holding 0/1 (inherit from user input above)
# operators & their functions(LogicalOperators())
# output (create extra output vars if requested for each operator output)
# layers (logic for connecting and max connections btwn in/op/out)

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
        #take list from dictionary and store into
        #temporary list to be manipulated for
        #each operator
        

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
        if self.len_logic_list > 0:
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


#class ConnectOperators(LogicalOperators):


#class OutputTable(ConnectOperators):
    




















