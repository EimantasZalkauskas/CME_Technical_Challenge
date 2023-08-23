from cachetools import cached, TTLCache
import time

class Palindrome():

    def __init__(self):
        self.validation_responses = []

    #Time To Live cache added
    @cached(cache= TTLCache(maxsize=1000, ttl=36000))
    def run(self, value):
        # run validations
        # only proceeds if validations all passed  
        if self.validate(value):
            print("validations passed")
            #run check
            if self.palindrome_check(value):
                return True
        #return value
        return False
    #Method for all validations 
    def validate(self, value):
        #Add validation response to array 
        self.validation_responses.append(self.input_validation(value))

        #TODO
        #more validations can be added below 

        #check if validation_reponses contain a failure 
        if "Failed" in self.validation_responses:
            return False
        else:
        #if true being returned all validations passed
            return True

    def input_validation(self, value):
        #Check if value contains space or a digit
        if " " in value or any(map(str.isdigit, value)):
            return "Failed"
        return "Passed"

    def palindrome_check(self, value):
        #check if palindrome
        for i in range(0, int(len(value)/2)):
            if value[i] != value[len(value)-i-1]:
                return False
        return True
 
