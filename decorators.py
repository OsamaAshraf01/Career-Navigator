def clean_string(string):
    unwanted_characters = ["\t", "\n", ".", ",", "\'", "\"", ")", "(", "!", "?"]

    string = [c for c in string if c not in unwanted_characters]

    return ''.join(string)



def clean(function):
    def wrapper(*args, **kwargs):
        Return = function(*args, **kwargs)
        if type(Return) is str:
            Return = Return.split(', ')

        if type(Return) is list:
            for i in range(len(Return)):
                Return[i] = clean_string(Return[i])
        
        return Return
    
    return wrapper