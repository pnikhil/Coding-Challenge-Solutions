def mutate_string(string, position, character):
    string = string[:int(position)] + character + string[int(position) + 1:]
    return (string)