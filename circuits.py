
from string import ascii_lowercase


class Bool_Operators():
    '''Boolean Operators: AND, OR, XOR, NAND, NOR, XNOR, NOT'''

    def __init__(self, volts, and_bool=None, or_bool=None, xor_bool=None, nand_bool=None, nor_bool=None, xnor_bool=None, not_bool=None):
        '''Initialize boolean operators'''
        self.and_bool = and_bool
        self.or_bool = or_bool
        self.xor_bool = xor_bool
        self.nand_bool = nand_bool
        self.nor_bool = nor_bool
        self.xnor_bool = xnor_bool
        self.not_bool = not_bool
        self.volts = volts

        '''Input which operator to be tested'''

    def volt_loop(self):
        '''Loop through volts'''
        for volt in self.volts:
            print(volt)

    def and_operator(self):
        '''AND Operator'''
        print("AND Operator")
        for volt in self.volts:
            if volt == [1, 1]:
                print(str(volt) + ' out: ' + str(1))
            else:
                print(str(volt) + ' out: ' + str(0))

    def or_operator(self):
        '''OR Operator'''
        print("OR Operator")
        for volt in self.volts:
            if volt == [0, 0]:
                print(str(volt) + ' out: ' + str(0))
            else:
                print(str(volt) + ' out: ' + str(1))

    def xor_operator(self):
        '''XOR Operator (Exclusive OR)'''
        print("XOR Operator")
        for volt in self.volts:
            if volt == [0, 1] or volt == [1, 0]:
                print(str(volt) + ' out: ' + str(1))
            else:
                print(str(volt) + ' out: ' + str(0))

    def nand_operator(self):
        '''NAND Operator'''
        print("NAND Operator")
        for volt in self.volts:
            if volt == [1, 1]:
                print(str(volt) + ' out: ' + str(0))
            else:
                print(str(volt) + ' out: ' + str(1))
    
    def nor_operator(self):
        '''NOR Operator'''
        print("NOR Operator")
        for volt in self.volts:
            if volt == [0, 0]:
                print(str(volt) + ' out: ' + str(1))
            else:
                print(str(volt) + ' out: ' + str(0))

    def xnor_operator(self):
        '''XNOR Operator'''
        print("XNOR Operator")
        for volt in self.volts:
            if volt == [0, 0] or volt == [1, 1]:
                print(str(volt) + ' out: ' + str(1))
            else:
                print(str(volt) + ' out: ' + str(0))

var_list = [] # A variable list to be used for naming variables and creating unique variables

for var in ascii_lowercase: # for each variable in the set of lowercase of ascii letters--
    var_list.append(var) # --append that variable to the variable list

#
#
#

def request_user_bool_pairs():

    bool_pair_dict = {} # Dictionary to store boolean pairs

    bool_pair_amount = int(input("How many boolean pairs? ")) # Ask user how many boolean pairs would they like to request

    while bool_pair_amount: # Keep iterating through until bool_pair_amount is exhausted

        bool_pair_list = [] # Temporary list for storing a single pair of two boolean inputs
        bool_pair_temp = {} # Temporarily store the boolean pair in current loop

        # These lists above automatically clear through every iteration; no need to manually clear since they are set to
        # empty or null values

        bool_a = int(input("First boolean(0/1): ")) # Request user first boolean
        bool_pair_list.append(bool_a) # Add 1st boolean to temp pair list

        bool_b = int(input("Second boolean(0/1): ")) # Request user second boolean
        bool_pair_list.append(bool_b) # Add 2nd boolean to temp pair list

        bool_pair_temp["bool_pair_" + var_list.pop(0)] = bool_pair_list # Add boolean list into a "key, value" pair in temp dict

        bool_pair_dict.update(bool_pair_temp) # Add iterated temp dict to permanent dictionary

        bool_pair_amount -= 1 # Reduce bool_pair_amount by 1 after each iteration

    bool_pair_values = bool_pair_dict.values() 

    return(bool_pair_values) # Return the values of the boolean pairs

bool_pair_values = request_user_bool_pairs()

test = Bool_Operators(bool_pair_values)
test.volt_loop()
test.and_operator()
test.or_operator()
test.xor_operator()
test.nand_operator()
test.nor_operator()
test.xnor_operator()
