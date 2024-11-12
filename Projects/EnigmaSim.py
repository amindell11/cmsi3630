def generate_code_dict(offset=0):
    offset %=26
    ASCII_OFFSET = 97  # Constant for the ASCII value of 'a'
    code_offset = ASCII_OFFSET-offset
    return {chr(i): chr(i + offset) for i in range(ASCII_OFFSET, ASCII_OFFSET+26)}

@DeprecationWarning
def shift_dict_values(original_dict, offset):
    # Create a new dictionary with the same keys and shifted values
    return {key: value + offset for key, value in original_dict.items()}

@DeprecationWarning
def shift_array_values(array, offset):
    # Apply the offset to each element in the array
    return [element + offset for element in array]

# encodes a string into ints
@DeprecationWarning
def alpha_to_numeric(string, dict):
    return [dict[chr] for chr in string]

# decodes a list of ints into a string
@DeprecationWarning
def numeric_to_alpha(nums, dict):
    reverse_dict = {value: key for key, value in dict.items()}
    print(reverse_dict)
    return ''.join(reverse_dict[i] for i in nums)

def apply_code(msg, dict):
    return ''.join(dict[chr] for chr in msg)

def alphabetical_offset(msg, offset):
    dict = generate_code_dict(offset)
    return apply_code(msg, dict)

class Rotor:
    def __init__(self, offset=0):
        self.offset = offset
        self.dict = generate_code_dict(offset)
        
    def encode(self, msg):
        return apply_code(msg, self.dict)

class EnigmaMachine:
    def __init__(self, rotors):
        self.rotors = rotors
    def encode(self, msg):
        for rotor in self.rotors :
            msg = rotor.encode(msg)
            print(msg)
        return msg
def main():
    print(alphabetical_offset("hello",29))
    rotor_1 = Rotor(29)
    rotor_2 = Rotor(6)
    machine = EnigmaMachine([rotor_1,rotor_2])
    coded_msg = machine.encode("hello")
    print(coded_msg)
    print(machine.encode(coded_msg))


main()