"""Provide an Input class to handle CLI inputs."""

from typing import List, Dict, Tuple
from termcolor import cprint
import colorama

colorama.init()

MODULE_COLOUR = 'blue'
ERROR_COLOUR = 'red'
RETURN = '<RTN>'
INTEGER_SELECTION = '<INTEGERS>'

__all__ = ['Input']

class Input():
    """
    The class takes a prompt string and a list of processes that
    define allowed inputs and the relevant process to be called.

    Attributes
    ----------

    prompt: str
        The prompt is the string that appears in the input statement. E.g.

            prompt = f"'S' to synchronise {len(files_to_copy)} files, 'Q' to quit: "

    process: dict[str, Tuple[object, list]] or dict[str, Tuple[object, list, tuple]]
        The process object is the function to be called when the input is the key
        the list contains the parameters to be passed to the function.
        The second definition includes a two-ple for min_integer and max_integer

        An example process:

            processes = {
                '<INTEGERS>': (function_one, [], (min_integer, max_integer)),
                '<RTN>': (function_two, []),
                'S': (function_three, [files_to_copy]),
                'Q': (quit, []),
            }
        If the process key is <RTN> (RETURN) then a null input (RETURN) will invoke the associated process.

        If the process key is <INTEGERS> (INTEGER_SELECTION) then a valid input is created for
        integers in the range (min_integer to the max_integer) and
        the call is to function_one with the  parameter input integer.)


    validation: dict[str, x]
        experimental

    Methods
    -------

    process_response:
        Returns the method associated with a valid input.

    Example Usage
    -----


    response = Input(prompt, processes).process_response()
    """
    def __init__(self, prompt: str,
                    processes: dict[str, Tuple[object, List[object]]],
                    validation: dict[str, object]={}):

        self.valid = False
        self.prompt = prompt
        self.processes = processes
        self.validation = validation
        self.valid = False
        (self.valid_inputs, self.valid_list) = self._get_valid_input_list()
        self.error_colour = ERROR_COLOUR
        self .response = None
        # Are valid inputs to be included in the error message?
        self.include_valid_in_error = True
        self._error_message = self._get_error_message('Invalid input.')

    def process_response(self) -> object:
        # Return the result of a valid input
        while True:
            response = self._get_input()
            if not self.valid:
                continue

            self.response = response
            if response not in self.processes:
                return response
            if not self.processes[response]:
                return True
            if response not in self.processes:
                return response
            process = self.processes[response]

            if not process[0]:
                return response
            result = process[0](*process[1])
            if len(process) <= 2:
                return result

    def _get_input(self) -> str:
        # Return a valid input string
        valid_inputs = self._get_valid_inputs()

        while True:
            self.valid = False
            response = input(self.prompt)

            # Handle null input
            if not response:
                if RETURN in self.processes:
                    self.valid = True
                    return RETURN
                continue

            if response in valid_inputs:
                self.valid = True
                if response in self.valid_inputs:
                    return response
                if response.upper() in self.valid_inputs:
                    return response.upper()
                if response.lower() in self.valid_inputs:
                    return response.lower()
            elif self.validation:
                return self.validate_input(response)
            cprint(f"{self._error_message}", self.error_colour)

    def validate_input(self, response):
        # Return a valid input string having validated input.
        if 'integer' in self.validation:
            return self.validate_integer(response)
        return False

    def validate_integer(self, response):
        # Validate an integer  response.
        if not response.isnumeric():
            return False
        integer = int(response)
        min_, max_ = self.validation['integer']['min'], self.validation['integer']['max']
        if integer < min_ or integer > max_:
            cprint(f"Integer outside valid range: {min_} to {max_}", ERROR_COLOUR)
            return False
        self.valid = True
        return response

    def _get_valid_input_list(self) -> List[str]:
        # Return a list of valid inputs and valid_list (used in error message)
        valid_inputs = []
        valid_list = []
        for key in self.processes:
            processes = {}
            if key == INTEGER_SELECTION:
                (min_, max_) = self.processes[key][2]
                integer_range = range(min_, max_+1)
                for index in integer_range:
                    valid_inputs.append(str(index))
                    processes[str(index)] = (self.processes[key][0], [index])
                self.processes = {**self.processes, **processes}
                valid_list.append(f'an integer({min_}-{max_})')
            else:
                valid_inputs.append(key)
                valid_list.append(key)
        return (valid_inputs, valid_list)

    def _get_valid_inputs(self):
        # Return a list of valid uppercase and lowercase inputs
        valid_inputs = []
        uppercase_valid_inputs = [item.upper() for item in self.valid_inputs]
        for item in uppercase_valid_inputs:
            valid_inputs.append(item)
            valid_inputs.append(item.lower())
        return valid_inputs

    def _get_error_message(self, error_text: str) -> str:
        # Return the error message for the input
        if self.include_valid_in_error:
            valid_responses_list = self.valid_list
            valid_responses = ', '.join(valid_responses_list)
            if len(valid_responses_list) >= 1:
                return f'{error_text} Use one of {valid_responses}'
        return error_text

    def __str__(self) -> str:
        return f'Input: {self.prompt} {self.valid_inputs}, {self.processes}'
