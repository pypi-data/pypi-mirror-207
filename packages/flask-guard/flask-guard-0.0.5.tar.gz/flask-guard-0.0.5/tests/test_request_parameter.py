import unittest
from src.FlaskGuard.RequestParameter import RequestParameter



class TestRequestParameter(unittest.TestCase):



    def test_is_not_vaild_value_size(self):
         """
         Test the `_is_not_vaild_value_size()` method of the RequestParameter
         class.

         This method tests the `_is_not_vaild_value_size()` method of the 
         RequestParameter class by passing various input values
         to ensure that it correctly identifies invalid size values. Valid
         size values should return False, while invalid size
        values should return True.

        Test cases:
            - Test with a valid integer: should return False.
            - Test with edge cases: 0, -10: should return True.
            - Test with invalid input types: None, list, string, list containing 
            None, empty list, empty dict:
            should return True.
            - Test with invalid float values: 0.0, -0.1, 0.1: should return True.
        """

         test_method = RequestParameter._is_not_vaild_value_size

         self.assertFalse(test_method(10))
         self.assertFalse(test_method(0))
         self.assertFalse(test_method(-10))

         self.assertFalse(test_method(None))
         self.assertTrue(test_method([1,2,3]))
         self.assertTrue(test_method("5"))
         self.assertTrue(test_method([None]))
         self.assertTrue(test_method([]))
         self.assertTrue(test_method({}))
         self.assertTrue(test_method(False))
         self.assertTrue(test_method(True))

         self.assertTrue(test_method(0.0))
         self.assertTrue(test_method(-0.1))
         self.assertTrue(test_method(0.1))


    def test_is_not_string_or_integer(self):
        """
        Test the _is_not_string_or_integer static method of RequestParameter.

        This method checks if the given variable type is not a string or an 
        integer.The test asserts that the method returns False when the type
        is int or str,and True when it's any other type.
        """
        test_method = RequestParameter._is_not_string_or_integer

        self.assertFalse(test_method(int))
        self.assertFalse(test_method(str))

        self.assertTrue(test_method(float))
        self.assertTrue(test_method(list))
        self.assertTrue(test_method("int"))
        self.assertTrue(test_method(0))
        self.assertTrue(test_method(["str"]))
        self.assertTrue(test_method(0.0))
        self.assertTrue(test_method(None))
        self.assertTrue(test_method(True))
        self.assertTrue(test_method(False))
         
       
    def test_object_creation(self):
        """
        Tests the creation of a RequestParameter object with valid arguments.
        Creates two RequestParameter objects, one with name "name", type str 
        and min value 0 and max value 10,and another with name "range", type 
        int and min value -10 and max value 10.Asserts that the objects are 
        instances of RequestParameter and that their respective getter methods 
        returnthe expected values for name, value_type, min_value and max_value.
        """
        requestParameter = RequestParameter("name",str,0,10)
        self.assertIsInstance(requestParameter,RequestParameter)

        requestParameterNegativNumber = RequestParameter("range",int,-10,10)
        self.assertEqual(requestParameterNegativNumber.get_name(), "range")
        self.assertEqual(requestParameterNegativNumber.get_value_type(), int)
        self.assertEqual(requestParameterNegativNumber.get_min_value(), -10)
        self.assertEqual(requestParameterNegativNumber.get_max_value(), 10)


    def test_object_creation_default_args(self):
        """
        Tests that a `RequestParameter` object can be created with only the 
        required 'name' argument,and that the default values are correctly
        assigned to the optional arguments.
        """
        requestParameter = RequestParameter("name")
        self.assertIsInstance(requestParameter,RequestParameter)
        self.assertEqual(requestParameter.get_name(), "name")
        self.assertEqual(requestParameter.get_value_type(), str)
        self.assertEqual(requestParameter.get_min_value(), None)
        self.assertEqual(requestParameter.get_max_value(), None)
         

    def test_getters(self):
        """
        Tests the getter methods of the RequestParameter class.
        It creates a RequestParameter object and then tests each of its getter 
        methods to ensure they are returning the correct value.

        The expected results are as follows:
        - requestParameter.get_name() should return "name".
        - requestParameter.get_value_type() should return str.
        - requestParameter.get_min_value() should return 0.
        - requestParameter.get_max_value() should return 10.
        """
        requestParameter = RequestParameter("name",str,0,10)
        self.assertEqual(requestParameter.get_name(), "name")
        self.assertEqual(requestParameter.get_value_type(), str)
        self.assertEqual(requestParameter.get_min_value(), 0)
        self.assertEqual(requestParameter.get_max_value(), 10)


    def test_object_creation_wrong(self):
        """
        Test that the constructor of the RequestParameter class raises a ValueError
        with the correct error message when it is given invalid arguments.

        Specifically, we test that the constructor raises a ValueError when:
        - the key name is not a string
        - the value type is not a string or an integer
        - the minimum or maximum value is not an integer or None

        For each invalid argument, we check that the correct error message is raised.
        """
        with self.assertRaisesRegex(ValueError, r'The key name must be a string, not int.'):
            RequestParameter(2, str, 0, 10)

        with self.assertRaisesRegex(ValueError,r'The key name must be a string, not None.'):
             RequestParameter(None,str,0,10)

        with self.assertRaisesRegex(ValueError,r'The second argument must be either str or int, not str.'):
             RequestParameter("name","string",0,10)

        with self.assertRaisesRegex(ValueError,r'The second argument must be either str or int, not None.'):
             RequestParameter("name",None,0,10)

        with self.assertRaisesRegex(ValueError,r'The second argument must be either str or int, not type.'):
             RequestParameter("name",float,0,10)

        with self.assertRaisesRegex(ValueError,r'The min_value must be int or None, not str.'):
             RequestParameter("name",str,"5",10)

        with self.assertRaisesRegex(ValueError,r'The min_value must be int or None, not float.'):
             RequestParameter("name",str,0.0,10)

        with self.assertRaisesRegex(ValueError,r'The max_value must be int or None, not float.'):
             RequestParameter("name",str,0,10.0)

        with self.assertRaisesRegex(ValueError,r'The max_value must be int or None, not str.'):
             RequestParameter("name",str,0,"10")

        

    


if __name__ == '__main__':
    unittest.main()