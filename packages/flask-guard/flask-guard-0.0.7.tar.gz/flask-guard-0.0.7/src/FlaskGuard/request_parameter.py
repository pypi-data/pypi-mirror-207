from typing import Type,Any

class RequestParameter:
    """
    A class representing a request parameter with a name, type, and optional
    minimum and maximum values.

    Attributes:
      - get_name: returns the name of the request parameter.
      - get_value_type: returns the type of the request parameter value.
      - get_min_value: returns the minimum value of the request parameter.
      - get_max_value: returns the maximum value of the request parameter.
    """
    def __init__(
            self, 
            name:str, 
            value_type:Type = str, 
            min_value:int=None, 
            max_value:int=None
            ) -> None:
        """
        Constructs a new RequestParameter object with the given name, value
        type, minimum value, and maximum value.
        """
        
        if not isinstance(name, str):
            type_name = type(name).__name__
            raise ValueError(
            f"The key name must be a string, not {type_name}.")
        elif RequestParameter._is_not_string_or_integer(value_type):
            type_name = type(value_type).__name__
            raise ValueError(
            f"The second argument must be either str or int, not {type_name}.")
        elif RequestParameter._is_not_vaild_value_size(min_value):
            type_name = type(min_value).__name__
            raise ValueError(
                f"The min_value must be int or None, not {type_name}."
            )
        elif RequestParameter._is_not_vaild_value_size(max_value):
            type_name = type(max_value).__name__
            raise ValueError(
                f"The max_value must be int or None, not {type_name}."
            )

        self._name = name
        self._value_type = value_type
        self._min_value = min_value
        self._max_value = max_value

    def get_name(self) -> str:
        """
        Get the name of the request parameter.
        """
        return self._name
    
    def get_value_type(self) -> Type:
        """
        Get the type of the request parameter value.
        """
        return self._value_type
    
    def get_min_value(self) -> int:
        """
        Get the minimum value of the request parameter.
        """
        return self._min_value
    
    def get_max_value(self) -> int:
        return self._max_value
    
    @staticmethod
    def _is_not_vaild_value_size(
         size_value:int
        ) -> bool:
        """
        Check if a given size value is not valid. To be used with the 
        constructor to check if the give size type is vaild.
        """
        if isinstance(size_value, type(None)):
            return False
        return not isinstance(size_value,int) or isinstance(size_value,bool)

    @staticmethod
    def _is_not_string_or_integer(
        variable_type:Type
        ) -> bool:
        """
        Checks if the given variable type is not a string or an integer. 
        The current implates onlt can handle strings or ints
        """
        return variable_type != str and variable_type != int
  

    


