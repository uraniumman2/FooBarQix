class FooBarQix:
    
    def __init__(self):
        self.result = ""
        self.range_result = []

    def convertor(self, number):
        self.result = ""
        divisiblity = self.divisibility_checker(number)
        content = self.content_checker(number)        
        if not (divisiblity or content):
            self.result = str(number)
        return self.result

    def range_convertor(self, start_point, end_point):
        self.range_result = []
        for number in range(start_point, end_point + 1):
            self.range_result.append(self.convertor(number))
        return self.range_result
    
    def divisibility_checker(self, number):
        flag = False
        if number % 3 == 0:
            flag = True
            self.result += "Foo"
        if number % 5 == 0:
            flag = True
            self.result += "Bar"
        if number % 7 == 0:
            flag = True
            self.result += "Qix"
        return flag
        
    def content_checker(self, number):
        flag = False
        digits = str(number)
        for digit in digits:
            if "3" == digit:
                flag = True
                self.result += "Foo"
            if "5" == digit:
                flag = True
                self.result += "Bar"
            if "7" == digit:
                flag = True
                self.result += "Qix"
        return flag

if __name__=='__main__':
    start_point = 1
    end_point = 100
    foo_bar_qix = FooBarQix()
    for number in range(start_point, end_point + 1):
        print(str(number) + " => " + foo_bar_qix.convertor(number))