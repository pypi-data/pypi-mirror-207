import unittest
from unittest.mock import patch
from src.FlaskGuard.FlaskGuard import RequestChecker
from src.FlaskGuard.RequestParameter import RequestParameter



class TestRequestChecker(unittest.TestCase):
    

    def setUp(self):
        self.flaskGuard =  RequestChecker("myapp")
        self.requestParameter = RequestParameter("name",min_value=0,max_value=10)
        self.requestParameter_int_value = RequestParameter("age",value_type=int,min_value=0,max_value=99)


    def test_generate_missing_key_error_message(self):
         """
         Test the `_generate_missing_key_error_message()` method of FlaskGuard class.

         This method tests the `_generate_missing_key_error_message()` method of the 
         FlaskGuard class by passing various input values to ensure that it
         correctly generates error messages for missing keys in the request body.

         Test cases:
            - Test with a valid RequestParameter instance: should return the correct error message.
            - Test with None as input: should raise AttributeError.
            - Test with an empty dictionary as input: should raise AttributeError.
         """
         test_method =  self.flaskGuard._generate_missing_key_error_message
         message = test_method(self.requestParameter)
         self.assertEqual(message,"Missing name field in request body.")
         with self.assertRaises(AttributeError):
            message = test_method(None)
         with self.assertRaises(AttributeError):
             message = test_method({})

        
    def test_generate_length_error_message(self):
         """
         Test the `_generate_length_error_message()` method of FlaskGuard class.

         This method tests the `_generate_length_error_message()` method of the 
         FlaskGuard class by passing various input values to ensure that it
         correctly generates error messages for fields that have lengths outside of
         the specified range.

         Test cases:
            - Test with valid input: should return the correct error message.
            - Test with None as key input: should raise AttributeError.
            - Test with None as request input: should raise TypeError.
            - Test with an invalid key input: should raise AttributeError.
         """
         test_method = self.flaskGuard._generate_length_error_message

         key = self.requestParameter
         request = {"name":"e"*20,"age":10}
         message = test_method(key,request)
         expected_length = key.get_max_value()
         actual_length = len(request[key.get_name()])
         expected_message = (
        f"The '{key.get_name()}' field must be {10} size or less, "
        f"and at least {0} size or more,"
        f"but is actually {actual_length} characters long."
         )

         self.assertEqual(message,expected_message)

         with self.assertRaises(AttributeError):
            message = test_method(None,request)

         with self.assertRaises(TypeError):
              message = test_method(key,None)

         with self.assertRaises(AttributeError):
            message = test_method(request,key)


    def test_generate_wrong_variable_type_error_message(self):
        """
        Test the `_generate_wrong_variable_type_error_message()` method of FlaskGuard class.

        This method tests the `_generate_wrong_variable_type_error_message()` method 
        of the FlaskGuard class by passing various input values to ensure that it
        correctly generates error messages for fields that have values of the wrong type.

        Test cases:
            - Test with a valid RequestParameter instance and a value of the correct type: 
               should not generate an error message.
            - Test with a valid RequestParameter instance and a value of the wrong type: 
               should return the correct error message.
            - Test with None as key input: should raise AttributeError.
            - Test with None as value input: should raise TypeError.
         """
        test_metod = self.flaskGuard._generate_wrong_variable_type_error_message
        key = self.requestParameter
        wrong_type = 39
        expected_type = key.get_value_type().__name__
        actual_type = type(wrong_type).__name__
        message = test_metod(key,wrong_type)
        expected_message = (
        f"The value for {key.get_name()} must be of type {expected_type}, "
        f"but is of type {actual_type} with the value {wrong_type}."
         )
        self.assertEqual(message,expected_message)




    def test_is_key_not_in_request(self):
         """
            Test the `_is_key_not_in_request()` method of FlaskGuard class.

            This method tests the `_is_key_not_in_request()` method of the FlaskGuard class by
            passing various input values to ensure that it correctly identifies whether a
            given key is present in a given request.

            Test cases:
               - Test with a request that contains the key: should return False.
               - Test with a request that does not contain the key: should return True.
               - Test with a request where the key has whitespace: should return True.
               - Test with an empty request: should return True.
               - Test with a very long request that does not contain the key: should return True.
               - Test with a very long request that contains the key: should return False.
               - Test with an integer as request input: should raise TypeError.
               - Test with None as request input: should raise TypeError.
               - Test with None as key input: should raise AttributeError.
               - Test with a string as key input: should raise AttributeError.
         """
         test_method = self.flaskGuard._is_key_not_in_request
         request = {"name":"erik","age":10}
         key_name = RequestParameter("name",min_value=0,max_value=10)
         key_lastname = RequestParameter("last_name",min_value=0,max_value=10)
         self.assertFalse(test_method(request,key_name))
         self.assertTrue(test_method(request,key_lastname))

         request_name_white_space = {"name ":"erik","age":10}
         self.assertTrue(test_method(request_name_white_space,key_name))

         empty_request = {}
         self.assertTrue(test_method(empty_request,key_name))


         long_request_not_conatining_key = {f"name{x}": x for x in range(1, 10000)}
         self.assertTrue(test_method(long_request_not_conatining_key,key_name))
         long_request_not_conatining_key["name"] = "eirk"
         self.assertFalse(test_method(long_request_not_conatining_key,key_name))
         

         
         with self.assertRaises(TypeError):
            test_method(12,key_name)

         with self.assertRaises(TypeError):
            test_method(None,key_name)
          
         with self.assertRaises(AttributeError):
            test_method(request,None)

         with self.assertRaises(AttributeError):
            test_method(request,str(key_lastname))


    def test_is_not_key_attributes_instance(self):
      test_method = self.flaskGuard._is_not_key_attributes_instance
      key_none = None
      key_bool_false = False
      key_bool_true = True
      key_empyt_string = ""
      key_vaild = self.requestParameter
      self.assertTrue(test_method(key_none))
      self.assertTrue(test_method(key_bool_false))
      self.assertTrue(test_method(key_bool_true))
      self.assertTrue(test_method(key_empyt_string))
      self.assertFalse(test_method(key_vaild))


    def test_is_string_value_within_length_limit(self):
        """
        Test the `_is_not_key_attributes_instance()` method of the FlaskGuard class.
         This method tests the `_is_not_key_attributes_instance()` method of the FlaskGuard
         class by passing various input values to ensure that it correctly identifies
         invalid instances of RequestParameter attributes. Invalid instances should
         return True, while valid instances should return False.

         Test cases:
            - Test with a None value: should return True.
            - Test with a False value: should return True.
            - Test with a True value: should return True.
            - Test with an empty string: should return True.
            - Test with a valid instance of RequestParameter attributes: should return False.
        """
        test_method = self.flaskGuard._is_value_within_max_length_limit
        key_vaild = self.requestParameter
      
        request_stander = {"name":"erik"}
        self.assertFalse(test_method(request_stander,key_vaild))
        request_pass_edage_case = {"name":"e" *10}
        self.assertFalse(test_method(request_pass_edage_case,key_vaild))
        request_fail_edage_case = {"name":"e" *11}
        self.assertTrue(test_method(request_fail_edage_case,key_vaild))
        key_int_value = RequestParameter("age",int,min_value=0,max_value=0)
        request_age = {"age":10}
        self.assertTrue(test_method(request_age,key_int_value))

        with self.assertRaises(KeyError):
            test_method({},key_vaild )
        with self.assertRaises(TypeError):
            test_method(None,key_vaild )

        with self.assertRaises(TypeError):
            test_method(str(request_stander),key_vaild )

        with self.assertRaises(AttributeError):
             test_method(request_stander,None)

        with self.assertRaises(AttributeError):
             test_method(key_vaild,request_stander)


    def test_is_string_value_within_min_length_limit(self):
        """
         Test the _is_value_within_min_length_limit method of the FlaskGuard class for a string key. 
         It should return True if the length of the value of the specified key in the given request is less than the minimum length limit of the key, False otherwise. 

         It also tests the method for an integer key. In this case, it should return True if the value of the specified key in the given request is less than the minimum value limit of the key, False otherwise.

         The test cases cover the following scenarios:
         - Request contains the key with value greater than or equal to the minimum length/ value limit.
         - Request contains the key with value less than the minimum length/ value limit.
         - Request does not contain the key.
         """
        test_metod = self.flaskGuard._is_value_within_min_length_limit

        string_key = self.requestParameter
        int_key = self.requestParameter_int_value 
        request = {"name":"erik"}
        self.assertFalse(test_metod(request,string_key))
        self.assertFalse(test_metod({"name":""},string_key))
        string_key_1_min_len = RequestParameter("name",min_value=1,max_value=10)
        self.assertTrue(test_metod({"name":""},string_key_1_min_len))
        self.assertFalse(test_metod({"name":"e"},string_key_1_min_len))
        self.assertFalse(test_metod({"name":"ee"},string_key_1_min_len))
        self.assertFalse(test_metod({"name":"e"*100000000},string_key_1_min_len))

        
        self.assertTrue(test_metod({"age":-1} ,int_key))
        self.assertTrue(test_metod({"age":-10} ,int_key))
        self.assertFalse(test_metod({"age":0} ,int_key))
        self.assertFalse(test_metod({"age":1} ,int_key))
        self.assertFalse(test_metod({"age":10} ,int_key))
        self.assertFalse(test_metod({"age":100000000000000000000000} ,int_key))
        self.assertTrue(test_metod({"age":-100000000000000000000000} ,int_key))


    def test_is_string_value_within_max_length_limit(self):
        """
        Test the `_is_value_within_min_length_limit` method of the `FlaskGuard`
          class for a string key. It should return True if the length of the 
          value of the specified key in the given request is less than the minimum
            length limit of the key, False otherwise. 

         It also tests the method for an integer key. In this case, it should return True if the value of the specified key in the given request is less than the minimum value limit of the key, False otherwise.

         The test cases cover the following scenarios:
         - Request contains the string key with value greater than or equal to the minimum length limit.
         - Request contains the string key with value less than the minimum length limit.
         - Request does not contain the string key.
         - Request contains the integer key with value greater than or equal to the minimum value limit.
         - Request contains the integer key with value less than the minimum value limit.
         - Request does not contain the integer key.
        """
        test_metod = self.flaskGuard._is_value_within_max_length_limit

        string_key = self.requestParameter
        int_key = self.requestParameter_int_value 
        request = {"name":"erik"}
        self.assertFalse(test_metod(request,string_key))
        self.assertFalse(test_metod({"name":"e"*10},string_key))
        self.assertTrue(test_metod({"name":"e"*11},string_key))
      
        self.assertFalse(test_metod({"name":"e"},string_key))
        self.assertFalse(test_metod({"name":"ee"},string_key))
        self.assertTrue(test_metod({"name":"e"*100000000},string_key))

        
        self.assertFalse(test_metod({"age":-1} ,int_key))
        self.assertFalse(test_metod({"age":-100} ,int_key))
        self.assertFalse(test_metod({"age":0} ,int_key))
        self.assertFalse(test_metod({"age":1} ,int_key))
        self.assertFalse(test_metod({"age":99} ,int_key))
        self.assertTrue(test_metod({"age":100} ,int_key))
        self.assertTrue(test_metod({"age":100000000000000000000000} ,int_key))
        self.assertFalse(test_metod({"age":-100000000000000000000000} ,int_key))
        
        


    def test_validate_key_int_value(self):
        """
        Test the _validate_key method of the FlaskGuard class for an integer key. It should validate whether the value of the specified key in the given request is an integer and within the specified range.

         The test cases cover the following scenarios:
         - Request contains the key with an integer value within the specified range.
         - Request contains the key with a non-integer value.
         - Request contains the key with a float value.
         - Request contains the key with a value outside the specified range.
         - Request does not contain the key.
        """
        test_method = self.flaskGuard._validate_key
        index = 0

        key = self.requestParameter_int_value
        request = {"age":"1" }
        result = test_method(key,request,index)

        self.assertListEqual(result,['The value for age must be of type int, but is of type str with the value 1.'])


        request = {"age":False }
        result = test_method(key,request,index)

        self.assertListEqual(result,['The value for age must be of type int, but is of type bool with the value False.'])


        request = {"age":True}
        result = test_method(key,request,index)
        self.assertListEqual(result,['The value for age must be of type int, but is of type bool with the value True.'])

        request = {"age":None}
        result = test_method(key,request,index)
        self.assertListEqual(result,['The value for age must be of type int, but is of type NoneType with the value None.'])

        request = {"age":2.0}
        result = test_method(key,request,index)
        self.assertListEqual(result,['The value for age must be of type int, but is of type float with the value 2.0.'])

        request = {"age":0.0}
        result = test_method(key,request,index)
        self.assertListEqual(result,['The value for age must be of type int, but is of type float with the value 0.0.'])

        request = {"age":100}
        result = test_method(key,request,index)
        self.assertListEqual(result,["The 'age' field must be 99 size or less, and at least 0 size or more,but is actually 100 characters long."])

        request = {"age":99}
        result = test_method(key,request,index)
        self.assertListEqual(result,[])


        request = {"age":[]}
        result = test_method(key,request,index)
        self.assertListEqual(result,['The value for age must be of type int, but is of type list with the value [].'])
        
         
    def test_validate_key(self):
        """
         Tests the `_validate_key` method of the FlaskGuard class.

         The test cases cover the following scenarios:
         - Request contains the key with the correct type and length.
         - Request does not contain the key.
         - Request contains the key with a length greater than the maximum allowed length.
         - Request contains the key with a value that is not of type str.
         - Request contains the key with a value of type NoneType.
         - Request contains the key with a value of type bool.
        """
        test_method = self.flaskGuard._validate_key
        key = 2
        request = {"name":"erik"}
        index = 0
        with self.assertRaises(ValueError) as  excaption_message:
             result = test_method(key,request,index)

        error_message = (
        f"The item at index {index} has type {type(key).__name__}, "
        f"which is not the required type {RequestParameter.__name__}. "
        f"Please ensure that you are passing the correct type of object "
        f"as the key attribute. You can create the required key attributes "
        f"using the RequestParameter class."
         )
        self.assertEqual(str(excaption_message.exception),error_message)



        key = self.requestParameter
        string_lenght = key.get_max_value() + 1
        request = {"name":"e" * string_lenght}
        result = test_method(key,request,index)

        self.assertListEqual(result,["The 'name' field must be 10 size or less, and at least 0 size or more,but is actually 11 characters long."])


        
        request = {"name ":"e" }
        result = test_method(key,request,index)

        self.assertListEqual(result,['Missing name field in request body.'])


        string_lenght = key.get_max_value() 
        request = {"name":"e" * string_lenght}
        result = test_method(key,request,index)

        self.assertListEqual(result,[])

        request = {}
        result = test_method(key,request,index)

        self.assertListEqual(result,['Missing name field in request body.'])


        string_lenght = key.get_max_value() 
        request = {"name":40 * string_lenght}
        result = test_method(key,request,index)

        self.assertListEqual(result,['The value for name must be of type str, but is of type int with the value 400.'])


        request = {"name":None}
        result = test_method(key,request,index)

        self.assertListEqual(result,['The value for name must be of type str, but is of type NoneType with the value None.'])

   
        request = {"name":True}
        result = test_method(key,request,index)

        self.assertListEqual(result,['The value for name must be of type str, but is of type bool with the value True.'])


        request = {"name":False}
        result = test_method(key,request,index)

        self.assertListEqual(result,['The value for name must be of type str, but is of type bool with the value False.'])









    def test_creat_validate_funcktion_erros_warings(self):
        test_method =  self.flaskGuard.create_validate_function

        with self.assertRaisesRegex(ValueError,r"('The required_keys is not a type of list', 'instead its RequestParameter')"):
             test_method(self.requestParameter)

        with self.assertRaisesRegex(ValueError,r"('The required_keys is not a type of list', 'instead its NoneType')"):
             test_method(None)

        with self.assertRaisesRegex(ValueError,r"('The required_keys is not a type of list', 'instead its tuple')"):
             test_method(())

        with patch('builtins.print') as mock_print:
            test_method([])
            mock_print.assert_called_once_with("Warning:The list of that contains the required_keys has length 0")


    def test_create_validate_function(self):
        test_method = self.flaskGuard.create_validate_function
        required_keys = [self.requestParameter,self.requestParameter_int_value]

        self.assertTrue(callable(test_method(required_keys)))

        valdiate_funcktion = test_method(required_keys)

        request_no_erros = {"name":"erik","age":29}
        is_vaild,message = valdiate_funcktion(request_no_erros)
        self.assertTrue(is_vaild)
        self.assertDictEqual(message,{'error messages': []})


        request_name_to_long = {"name":"e"*11,"age":29}
        is_vaild,message = valdiate_funcktion(request_name_to_long)
        self.assertFalse(is_vaild)
        self.assertDictEqual(message,{'error messages': ["The 'name' field must be 10 size or less, and at least 0 size or more,but is actually 11 characters long."]})

        request_missing_name = {"age":29}
        is_vaild,message = valdiate_funcktion(request_missing_name)
        self.assertFalse(is_vaild)
        self.assertDictEqual(message,{'error messages': ["Missing name field in request body."]})

        request_missing_name = {"age":29}
        is_vaild,message = valdiate_funcktion(request_missing_name)
        self.assertFalse(is_vaild)
        self.assertDictEqual(message,{'error messages': ["Missing name field in request body."]})

        request_missing_age = {"name":"erik"}
        is_vaild,message = valdiate_funcktion(request_missing_age)
        self.assertFalse(is_vaild)
        self.assertDictEqual(message,{'error messages': ["Missing age field in request body."]})

        request_age_to_big = {"name":"erik","age":100}
        is_vaild,message = valdiate_funcktion(request_age_to_big)
        self.assertFalse(is_vaild)
        self.assertDictEqual(message,{'error messages': ["The 'age' field must be 99 size or less, and at least 0 size or more,but is actually 100 characters long."]})

        request_missing_age_name = {}
        is_vaild,message = valdiate_funcktion(request_missing_age_name)
        self.assertFalse(is_vaild)
        self.assertDictEqual(message,{'error messages': ['Missing name field in request body.','Missing age field in request body.']})


        request_containg_other_key_vaild = {"name":"erik","age":29,"last-name":"svenson"}
        is_vaild,message = valdiate_funcktion(request_containg_other_key_vaild)
        self.assertTrue(is_vaild)
        self.assertDictEqual(message,{'error messages': []})
        
        request_containg_other_key_not_vaild = {"name":"erik",
                                                "last-name":"svenson"}
        is_vaild,message = valdiate_funcktion(request_containg_other_key_not_vaild)
        self.assertFalse(is_vaild)
        self.assertDictEqual(message,{'error messages': ['Missing age field in request body.']})


    def test_validate_funcktion_erros(self):
        test_method = self.flaskGuard.create_validate_function
        required_keys = [self.requestParameter,self.requestParameter_int_value]

        self.assertTrue(callable(test_method(required_keys)))

        valdiate_funcktion = test_method(required_keys)

        with self.assertRaisesRegex(ValueError,r"The provided request is not a type of dict,instead its NoneType"):
             valdiate_funcktion(None)

        with self.assertRaisesRegex(ValueError,r"The provided request is not a type of dict,instead its bool"):
             valdiate_funcktion(True)

        with self.assertRaisesRegex(ValueError,r"The provided request is not a type of dict,instead its bool"):
             valdiate_funcktion(False)

        with self.assertRaisesRegex(ValueError,r"The provided request is not a type of dict,instead its list"):
             valdiate_funcktion([])

        with self.assertRaisesRegex(ValueError,r"The provided request is not a type of dict,instead its str"):
             valdiate_funcktion('{"name":"erik"}')


if __name__ == '__main__':
    unittest.main()