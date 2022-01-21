class test_fun:
    def __init__(self, fname, *args, expected_output):
        self.fname = fname
        self.args = args
        self.expected_output = expected_output

    def run_code(self):
        output = eval(f'{self.fname}(*{self.args})')

        result = False
        if str(output) == str(self.expected_output):
            result = True

        return result, self.expected_output, output
    


    

class test_code:
    def __init__(self, list_of_test_fun) -> None:
        self.list_of_test_fun = list_of_test_fun
    
    def run_codes(self):
        result_list = []
        for fun in self.list_of_test_fun:

            result_list.append(test_fun(fun[0],*fun[1:-1],expected_output=fun[-1]).run_code())
        
        return result_list
    
    def __str__(self) -> str:
        st = ''
        counter = 1
        for result in self.run_codes():
            txt = 'SUCCESSEDED'
            if result[0] == False:
                txt = 'FAILED'
            st += f'########## Test case {counter}  {txt} ###########\n'
            counter += 1
            st += f'Expected Output \n\n {result[1]}\n\n'
            st += f'Compiled Output \n\n {result[2]}\n\n\n\n'
        return st


        


# fun1 = test_fun('sum',(1,2,2,2,1),expected_output = 6)
# print(fun1.run_code())
# fname = 'fun1'
# args = (1,2,3)
# fun2 = test_code([['sum', *args,5],['sum', *args,6]])
# print(fun2.run_codes())
# print(fun2)

def count(ls1 , ls2):
    c = 0
    for i in ls1:
        if i in ls2:
            c += 1
    return c

test = test_code([['count',[1,2,3,4],[5,3,1,2], 3],
['count',[1,2],[5,2], 1],
['count',[1,2],[5,3], 0],
['sum',(1,2,3),5
]]
)


print(test)