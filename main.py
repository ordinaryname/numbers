import numpy as np

class Number:
    '''A class which represents an array of numbers defined by a group of conditions
    '''
    def __init__ (self, initial=1, growth_rate=0, number_of_steps=2, operation='add'):
        # When setting these values, also set: self._reevaluate = True
        # self._initial is the first number in the array
        self._initial = initial
        # self._growth_rate defines the difference between 2 adjacent numbers in the array
        self._growth_rate = growth_rate
        # self._number_of_steps defines the amount of numbers in the array
        self._number_of_steps = int(number_of_steps)
        # self._operation defines the algebraic operation needed to define self._value
        self._operation = operation

        # When getting these values, check if these values need to be re-evaluated (self._reevaluate = True)
        # These values are supposed to be dependent on the values defined above
        # They are updated by the 'evaluate' function
        self._value = None
        self._array = None

        # Helps keep the values defined above updated before each use
        self._reevaluate = True

    def evaluate(self):
        if(self._reevaluate):
            if(self.get_growthRate() == 0):
                self._array = np.full(self.get_numberOfSteps(), self.get_initial())
            else:
                last_array_element = self.get_growthRate() * (self.get_numberOfSteps() - 1) + self.get_initial()
                # absolute_distance: i.e. absDis(-1, -5) = 4, absDis(2, -5) = 3, absDis(6, 1) = 5
                absolute_distance = np.abs(self.get_growthRate() / 2)
                # direction = -1 or 1
                direction = self.get_growthRate() / np.abs(self.get_growthRate())
                # Create array: np.arange()
                # [start = self._initial
                # stop) = num WHERE num BETWEEN last_array_element AND (last_array_element + self._growth_rate)
                # step = self._growth_rate
                self._array = np.arange(self.get_initial(), last_array_element + (absolute_distance * direction), self.get_growthRate())
            self._value = np.sum(self._array)
            self._reevaluate = False

    # Overide methods
    def __repr__(self):
        return f"Number({self.get_initial()}, {self.get_growthRate()}, {self.get_numberOfSteps()}, {self.get_operation()})"

    def __eq__(self, other):
        if(isinstance(other, Number)):
            return (self.get_initial(), self.get_growthRate(), self.get_numberOfSteps(), self.get_operation()) == (other.get_initial(), other.get_growthRate(), other.get_numberOfSteps(), other.get_operation())
        return NotImplemented

    # Getters and Setters
    def get_initial(self):
        return self._initial

    def set_initial(self, initial):
        self._initial = initial
        self._reevaluate = True

    def get_growthRate(self):
        return self._growth_rate

    def set_growthRate(self, growth_rate):
        self._growth_rate = growth_rate
        self._reevaluate = True

    def get_numberOfSteps(self):
        return self._number_of_steps

    def set_numberOfSteps(self, number_of_steps):
        self._number_of_steps = number_of_steps
        self._reevaluate = True

    def get_operation(self):
        return self._operation

    def set_operation(self, operation):
        self._operation = operation
        self._reevaluate = True

    def get_value(self):
        if(self._reevaluate):
            self.evaluate()
        return self._value

    def get_array(self):
        if(self._reevaluate):
            self.evaluate()
        return self._array
