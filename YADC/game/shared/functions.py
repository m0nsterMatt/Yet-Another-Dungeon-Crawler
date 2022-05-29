from pyray import measure_text


class Functions:
    """
    A group of functions to aid in calculations within the game.
    
    The responsibility of Functions is to provide specific, but necessary,
    calculations to be used within the game.
    """
    def __init__(self):
        """
        Constructs a new Functions
        """
        pass

    def make_flat_list(given):
        """
        Converts a list of lists into a flat list
        
        Args:
            given (list): the given list to convert
            final (list): the final, converted list; or, a list to add onto
        """
        final = []

        return Functions._make_flat_list_recur(given, final)

    def _make_flat_list_recur(given, final):
        """
        Converts a list of lists into a flat list (does the actual
        converting)
        """

        for elem in given:
            if isinstance(elem, list):
                Functions._make_flat_list_recur(elem, final)
            else:
                final.append(elem)
        return final

    def split_string(string, font_size, max_length):
        """
        Splits a string into a list of strings, each element of which is
        as close to the given maximum length as possible without going
        over or splitting in the middle of a word.

        Args:
            string (string): the string to be split
            font_size (integer): the string's font size
            max_length (integer): the maximum length of each string
        """
        final_list = []
        txt_list = string.split()
        final = txt_list[0]

        for elem in txt_list[1:]:
            possible = f'{final} {elem}'
            length = Functions.measure_text(possible, font_size)
            if length < max_length:
                final = possible
            else:
                final_list.append(final)
                final = elem

        final_list.append(final)
        return final_list

    def measure_text(string, size):
        """
        Measures the given text at the given size.
        
        Args:
            string (string): the text to be measured
            size (integer): the font size
        """
        return measure_text(string, size)
