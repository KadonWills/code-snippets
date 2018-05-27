class opcode_map_functions:
        
    def divide(self):
        temp = self.stack_pop()
        self.stack_push(self.stack_pop() / temp)

    def multiply(self):
        temp = self.stack_pop()
        self.stack_push(self.stack_pop() * temp)

    def plus(self):
        temp = self.stack_pop()
        self.stack_push(self.stack_pop() + temp)

    def minus(self):
        temp = self.stack_pop()
        self.stack_push(self.stack_pop() - temp)

    def notEqual(self):
        temp = self.stack_pop()
        self.stack_push(self.stack_pop() != temp)

    def isEqual(self):
        temp = self.stack_pop()
        self.stack_push(self.stack_pop() == temp)

    def greaterThanOrEqual(self):
        temp = self.stack_pop()
        self.stack_push(self.stack_pop() >= temp)

    def lessThanOrEqual(self):
        temp = self.stack_pop()
        self.stack_push(self.stack_pop() <= temp)

    def greaterThan(self):
        temp = self.stack_pop()
        self.stack_push(self.stack_pop() > temp)
        
    def lessThan(self):
        temp = self.stack_pop()
        self.stack_push(self.stack_pop() < temp)



    def array_pop(self):
        #pops value of array
        array = self.stack_pop()
        self.stack_push(array.pop())
        self.stack_push(array)

    def array_push(self):
        #appends to an array
        data_to_add = self.stack_pop()
        array = self.stack_pop()
        array.append(data_to_add)
        self.stack_push(array)



    def object_add(self):
        #adds data to the object
        obj_name_A_data = self.stack_pop()
        obj = self.stack_pop()

        obj[obj_name_A_data[0]] = obj_name_A_data[1]
        self.stack_push(obj)

    def object_read(self):
        #reads a directory from object
        obj_dir = self.stack_pop()
        obj = self.stack_pop()
        for x in obj.keys():

            if obj_dir == x:
                self.stack_push(obj[obj_dir])

    def object_remove(self):
        pass



    def newValue(self):
        #creates new value on memory
        self.memory_add(self.stack_pop(), self.stack_pop())

    def readValue(self):
        #reads value on the memory
        self.stack_push(self.memory[self.stack_pop()])

    def dropValue(self):
        #removes value from the memory
        self.memory_drop(self.stack_pop())



    def stack_insert(self):
        #inserts valuse at stack index
        temp = self.stack_pop()
        self.stack.insert(temp, self.stack_pop())
        
    def stack_read(self):
        #reads item on index of the stack
        self.stack_push(self.stack[self.stack_pop()])

    def stack_swap(self):
        #swaps item on the stack for something else
        temp = self.stack_pop()
        self.stack[temp] = self.stack_pop()
        
    def stack_drop(self):
        #drops item on the stack
        self.stack.pop(self.stack_pop())

    def stack_length(self):
        #gets the length of the stack
        self.stack_push(len(self.stack))
        
    def stack_run(self):
        #runs code dumped on the stack
        sub_pointer = 0
        stack = self.stack_pop()
        while sub_pointer < len(stack):
            opcode = stack[sub_pointer]
            #error finding log code:
            #print('{}.{} => {}\n'.format(self.instruction_pointer, sub_pointer, self.stack))
            sub_pointer += 1
            self.dispatch(opcode)



    def builtin_tostring(self):
        #changes anything into string
        self.stack_push(str(self.stack_pop()))

    def builtin_tointeger(self):
        #changes string into integer/number if it can
        self.stack_push(int(self.stack_pop()))

    def builtin_type(self):
        #returns true if the type matches the one given
        datatype = self.stack_pop()
        data = self.stack_pop()

        if datatype == 'int':
            self.stack_push(isinstance(data, int))
        elif datatype == 'str':
            self.stack_push(isinstance(data, str))
        elif datatype == 'list':
            self.stack_push(isinstance(data, list))

    def builtin_input(self):
        #takes input from console
        self.stack_push(input(self.stack_pop()))
        
    def builtin_print(self):
        #prints out to console
        print(self.stack_pop())



    def ref_slice(self):
        index2 = self.stack_pop()
        index1 = self.stack_pop()
        self.stack_push(self.stack_pop()[index1:index2])
        #print('s_{} => {}\n'.format(self.instruction_pointer, self.stack))


 
    def statment_else(self):
        #else is a standard if statment
        if self.stack_pop():
            self.stack_run()
        else:
            #this cleans of the cash if we can't execute self.runValue
            self.stack_pop()

    def statment_ifelse(self):
        #ifelse is a standard if statment. But it leaves a True or False
        #trail behind so that we can execute the else.
        if self.stack_pop():
            self.stack_run()
            self.stack_push(False)
        else:
            self.stack_pop()
            self.stack_push(True)

    def statment_loop(self):
        while True:
            #performs loop condition
            self.stack_push(self.stack_top())
            self.stack_run()

            #test to see if loop condition is filled
            #if so re execute
            if self.stack_pop():
                self.stack_push(self.stack[-2])
                self.stack_run()
            else:
                #closes loop if condition fails
                self.stack_pop()
                self.stack_pop()
                break

    def statment_match(self):
        #matches value with a case
        arg = self.stack_pop()
        cases = self.stack_pop()

        #our no arguments called catch
        num = 0
        case_len = len(cases)

        for case in cases:
            if case[0] == arg:
                self.stack_push(case[1])
                self.stack_run()
            else:
                num += 1

        #now if all failed we will return True, if at least 1 worked we return False
        if num == case_len:
            self.stack_push(True)
        else:
            self.stack_push(False)



class vm(opcode_map_functions):

    def __init__(self, ast):
        self.memory = {}
        self.stack = []
        self.ast = ast
        self.instruction_pointer = 0
        self.opcode_map = {
            '_/':        self.divide,
            '_*':        self.multiply,
            '_+':        self.plus,
            '_-':        self.minus,
            '_!=':       self.notEqual,
            '_==':       self.isEqual,
            '_>=':       self.greaterThanOrEqual,
            '_<=':       self.lessThanOrEqual,
            '_>':        self.greaterThan,
            '_<':        self.lessThan,

            '_arr_push': self.array_push,
            '_arr_pop':  self.array_pop,

            '_obj_add':  self.object_add,
            '_obj_read': self.object_read,

            '_mem_new':  self.newValue,
            '_mem_read': self.readValue,
            '_mem_drop': self.dropValue,

            '_sta_ins':  self.stack_insert,
            '_sta_read': self.stack_read,
            '_sta_swap': self.stack_swap,
            '_sta_drop': self.stack_drop,
            '_sta_len':  self.stack_length,
            '_sta_run':  self.stack_run,

            '_str':      self.builtin_tostring,
            '_int':      self.builtin_tointeger,
            '_type':     self.builtin_type,
            '_input':    self.builtin_input,
            '_print':    self.builtin_print,

            '_slice':    self.ref_slice,

            '_ifelse':   self.statment_ifelse,
            '_else':     self.statment_else,
            '_loop':     self.statment_loop,
            '_match':    self.statment_match
            }


    def memory_add(self, variableName, data):
        self.memory[variableName] = data

    def memory_drop(self, variableName):
        del self.memory[variableName]



    def stack_pop(self):
        return self.stack.pop()

    def stack_push(self, data):
        self.stack.append(data)

    def stack_top(self):
        return self.stack[-1]


    def run(self):
        while self.instruction_pointer < len(self.ast):
            opcode = self.ast[self.instruction_pointer]
            #error finding log code:
            #print('{} => {}\n'.format(self.instruction_pointer, self.stack))
            self.instruction_pointer += 1
            self.dispatch(opcode)

        print("\n\n Memory => {} \n\n Stack => {}".format(self.memory, self.stack))


    def dispatch(self, operation):
        if isinstance(operation, str) and operation in self.opcode_map:
            self.opcode_map[operation]()
        else:
            self.stack_push(operation)
            



vm([
    {
        'Rian/age': 16,
        'Rian/gender': 'Male',
        'Sweet/age': 12,
        'Sweet/gender': 'Female'
        },
    0,
    '_sta_read',
    [
        'Rian/job',
        'programming'
        ],
    '_obj_add',
    0,
    '_sta_swap',
    '_print'
    ]).run()

"""
vm(
    [
        [
            [
                False,
                ['It was False!','_print']
                ],
            [
                'str',
                ['It was a string!','_print']
                ],
            [
                True,
                ['It was a true boolean!','_print']
                ],
            [
                5,
                ['It was the number 5!','_print']
                ]
            ],
        70,
        '_match',
        [
            'Nothing Worked!',
            '_print'
            ],
        -2,
        '_sta_read',
        '_else'
        ]
    ).run()
"""
#vm([[1,2,3,4,5], '_arr_pop', '_print']).run()
#vm([['hello', 'world'],0,1,'_slice','_print']).run()
"""
vm([
    [
        True,
        True,
        False
        ],
    'lt',
    '_mem_new',

    0,
    'num',
    '_mem_new',

    [
        'num',
        '_mem_read',
        1,
        '_+',
        'num',
        '_mem_new',

        #'num',
        'hello',
        '_print'
        ],
    [
        'lt',
        '_mem_read',
        'num',
        '_mem_read',
        'num',
        '_mem_read',
        1,
        '_+',
        '_slice'
        ],
    '_loop'
    ]).run()
"""
"""
vm([
    #'give an input> ',
    #'_input',
    1,
    'x',
    '_mem_new',

    [
        'It is an int!',
        '_print'
        ],
    'x',
    '_mem_read',
    'int',
    '_type',
    '_else',

    [
        'It is a string!',
        '_print'
        ],
    'x',
    '_mem_read',
    'str',
    '_type',
    '_else',

    [
        'It is a list!',
        '_print'
        ],
    'x',
    '_mem_read',
    'list',
    '_type',
    '_else'
    ]).run()
"""
"""
vm([
    0,
    'x',
    '_mem_new',
    
    [
        #'x',
        #'_mem_read',
        #'_print',
        
        'x',
        '_mem_read',
        1,
        '_+',
        'x',
        '_mem_new'
        ],
    [
        'x',
        '_mem_read',
        999999,#10000000000000000000000000000000000000000000000000000000000,
        '_<'
        ],
    '_loop',
    'x',
    '_mem_read',
    '_print'
    ]).run()
"""
#vm(["Hello", "World", 0,'_sta_swap','Hello ', 0, '_sta_ins', '_+', '_print']).run()
"""
vm([
    'input> ',

    0,
    '_sta_read',
    '_input',

    1,
    0,
    '_sta_ins',
    '_sta_swap',

    [#else block
        'paper',
        '_print'
        ],
    [#if block
        'rock',
        '_print'
        ],
    'rock',
    0,
    '_sta_read',
    '_==',
    '_ifelse',
    '_else'
    ]).run()
"""
#vm(['Hello ', 'my ', 'name ', 'is ', 'Sweet', '_+', '_+', '_+', '_+', '_print']).run()
#vm(['Hello', 'world', ' ', 0, '_sta_read', 2, '_sta_read', '_+', 1, '_sta_read', '_+', '_print']).run()
#vm([1,2,3,4,5,6,7,8,9,10,'_print','_sta_len',5,'_-','_sta_drop']).run()
"""
vm([#example while loop counter

    #number variable
    0,
    'x',
    '_mem_new',

    #block of code
    [
        #prints our current number count
        'x',
        '_mem_read',
        '_print',

        #increments x by 1
        'x',
        '_mem_read',
        1,
        '_+',
        'x',
        '_mem_new',

        #loads in block for use if needed
        'counter',
        '_mem_read',
        #performes an operation
        'x',
        '_mem_read',
        10000000000000000000000000000000000000000000000000000000000,#10,
        '_<',
        #if true then it will run loaded block, if false it will just delete
        '_else'
        ],
    #creates new function with block of code
    'counter',
    '_mem_new',

    #calles function to start loop
    'counter',
    '_mem_read',
    '_sta_run',

    #drops unneeded variable/function/data
    'counter',
    '_mem_drop',

    #lets us know we made it!
    'We have reached ',
    'x',
    '_mem_read',
    '_str',
    '_+',
    '!',
    '_+',
    '_print'

    ]).run()
"""
"""
vm([
    1,
    'x',
    '_mem_new',
    
    [
        'x',
        '_mem_read',
        '_print',

        'x',
        '_mem_read',
        'x',
        '_mem_read',
        '_+',
        'x',
        '_mem_new',

        [
            'fib',
            '_mem_read',
            '_sta_run'
            ],

        'x',
        '_mem_read',
        10000000000000000000000000000000000000000000000000000000000,#max integer python can handle
        '_<',
        '_else'
        ],

    'fib',
    '_mem_new',

    'fib',
    '_mem_read',
    '_sta_run',

    'x',
    '_mem_read',
    '_print',
    
    'fib',
    '_mem_drop',
    'x',
    '_mem_drop'
    ]).run()
"""
