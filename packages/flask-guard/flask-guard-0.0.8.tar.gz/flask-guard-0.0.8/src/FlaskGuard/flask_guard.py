from typing import Type,Dict, List,Tuple,Any,Callable
from .request_parameter import RequestParameter


class FlaskGuard:
  """
  The RequestChecker class is a utility class for validating and checking the 
  format of request data. It contains functions for generating error messages,
  as well as a series of validation functions for checking that requests 
  contain the expected data and are properly formatted. The class can create 
  a validation function that validates a dictionary against a set of required 
  keys
  """
  

  def __init__(self,app_name:str = "MyApp"):
     self.app_name = app_name

  # This section contains functions for generating error messages 

  def _generate_missing_key_error_message(
     self,
     key: RequestParameter
     ) -> str:
    """
    Generates an error message for a missing key in the request body.
    """
    return f"Missing {key.get_name()} field in request body."
  

  def _generate_wrong_variable_type_error_message(
     self,
     key: RequestParameter,
     value: Any
    ) -> str:
    """
    Generates a string message to indicate that a variable value is of the 
    wrong type.
    """
    expected_type = key.get_value_type().__name__
    actual_type = type(value).__name__
    return (
        f"The value for {key.get_name()} must be of type {expected_type}, "
        f"but is of type {actual_type} with the value {value}."
    )
  
  def _generate_length_error_message(
     self,
     key: RequestParameter, 
     request: dict
     ) -> str:
    """
    Generates an error message for a field with an invalid length.
    """
    max_value = key.get_max_value()
    min_value = key.get_min_value()
    if isinstance(request[key.get_name()],int):
       actual_length = request[key.get_name()]
    else:
       actual_length = len(request[key.get_name()])
    return (
        f"The '{key.get_name()}' field must be {max_value} size or less, "
        f"and at least {min_value} size or more,"
        f"but is actually {actual_length} characters long."
    )
     

  # Request Validation Section
  # This section contains functions for checking that requests contain the 
  # expected data and are properly formatted

  def _is_not_instance_of_type(
     self,
     type:Type,
     value:Any
    ) -> bool:
    """
    Check if a given value is not an instance of a specified type.
    """
    if type == int and isinstance(value,bool):
       return True
    return not isinstance(value,type)


  def _is_key_not_in_request(
     self,
     request:dict,
     key:RequestParameter
     ) -> bool:
     """
     Checks if a key is not present in a request dictionary.
     """
     return key.get_name() not in request
  

  def _is_not_key_attributes_instance(
     self,
     key: Any
     ) -> bool:
     """
     Checks if a value is not an instance of the _KeyAttributes class.
     """
     return not isinstance(key,RequestParameter)
     

  def _is_value_within_max_length_limit(
     self,
     request:dict,
     key:RequestParameter
     ) -> bool:
     """
     Checks if the value of the given key in the request dictionary is
     within the max length limit.
     """
     if isinstance(request[key.get_name()],int):
        return key.get_max_value() != None  and \
         request[key.get_name()] > key.get_max_value()
     return key.get_max_value() != None  and \
      len(request[key.get_name()]) > key.get_max_value()
  

  def _is_value_within_min_length_limit(
     self,
     request: dict,
     key: RequestParameter
     ) -> bool:
     """
     Checks if the value of the given key in the request dictionary is
     within the min length limit.
     """
     if isinstance(request[key.get_name()],int):
        return key.get_min_value() != None and \
           request[key.get_name()] < key.get_min_value()
     return key.get_min_value() != None  and \
      len(request[key.get_name()]) < key.get_min_value()


  def _validate_key(
     self,
     key: RequestParameter,
     request: dict,
     index: int
     ) -> list:
     """
     Checks a given key against a request dictionary to ensure that it meets
     certain criteria, returning a list of error messages if there are any 
     issues.
     """
     errors = []
     if self._is_not_key_attributes_instance(key):
        error_message = (
        f"The item at index {index} has type {type(key).__name__}, "
        f"which is not the required type {RequestParameter.__name__}. "
        f"Please ensure that you are passing the correct type of object "
        f"as the key attribute. You can create the required key attributes "
        f"using the RequestParameter class."
         )
        raise ValueError(error_message)
     if self._is_key_not_in_request(request,key):
        errors.append(
           self._generate_missing_key_error_message(key)
            )
     elif self._is_not_instance_of_type(key.get_value_type(),
                                       request[key.get_name()]):
        errors.append(
           self._generate_wrong_variable_type_error_message(
           key,request[key.get_name()])
           )
     elif self._is_value_within_max_length_limit(request,key):
        errors.append(
           self._generate_length_error_message(key,request))
     elif self._is_value_within_min_length_limit(request,key):
        errors.append(
           self._generate_length_error_message(key,request))
     return errors
        

  def create_validate_function(
    self,
    required_keys:list
    ) -> Callable:
     """
     Creates a function that validates a dictionary against a set of required
     keys.
     """
     if not isinstance(required_keys,list):
       error_message = ( f"The required_keys is not a type of list",
                        f"instead its {type(required_keys).__name__}")
       raise ValueError(error_message)
     elif len(required_keys) == 0:
        print("Warning:The list of that contains the required_keys has length 0")
     
     def validate_request_data(
        request:dict
        ) -> Tuple[bool,Dict[str, List[str]]]:
        """
        Validates that the given request contains all of the required keys with
        the correct data types and lengths.
        """
        if not isinstance(request,dict):
          type_name = type(request).__name__
          raise ValueError(
             f"The provided request is not a type of dict,instead its {type_name}"
             )
        errors = []
        for index,key in enumerate(required_keys):
            errors.extend(self._validate_key(key,request,index))
        return len(errors) == 0,{"error messages":errors}
     
     return validate_request_data
         
        
     
     

        
        





