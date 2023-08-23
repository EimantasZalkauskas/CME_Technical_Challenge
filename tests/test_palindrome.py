from palindrome_processing import Palindrome


class TestPalindrome:
    #Palindrome Pass
    def test_palindrome_method_pass(self):
        inst = Palindrome()
        res = inst.palindrome_check("kayak")
        assert res == True
    
    #Palindrome Fail
    def test_palindrome_method_fail(self):
        inst = Palindrome()
        res = inst.palindrome_check("kaya0")
        assert res == False
    
    #Input Validation Pass
    def test_input_validation_method_pass(self):
        inst = Palindrome()
        res = inst.input_validation("kayak")
        assert res == "Passed"
    
    #Input Validation Fail
    def test_input_validation_method_space_fail(self):
        inst = Palindrome()
        res = inst.input_validation("kaya ")
        assert res == "Failed"
    
    #Input Validation Fail
    def test_input_validation_method_number_fail(self):
        inst = Palindrome()
        res = inst.input_validation("kaya0")
        assert res == "Failed"
    
    #Validate Pass
    def test_validate_method_pass(self):
        inst = Palindrome()
        res = inst.validate("kayak")
        assert res == True
    
    #Validate Fail
    def test_validate_method_fail(self):
        inst = Palindrome()
        res = inst.validate("kaya0")
        assert res == False
    
    #Run Pass
    def test_run_method_pass(self):
        inst = Palindrome()
        res = inst.validate("kayak")
        assert res == True
    
    #Run Fail
    def test_run_method_fail(self):
        inst = Palindrome()
        res = inst.validate("kaya0")
        assert res == False