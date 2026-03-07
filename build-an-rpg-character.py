full_dot = '●'
empty_dot = '○'

def dot(label, value):
    line = label + " "
    
    for i in range(1, 11):
        if i <= value:
            line += full_dot
        else:
            line += empty_dot
    
    return line

def create_character(name,strength,intelligence,charisma):
    if  type(name) != str:
        return'The character name should be a string'
    elif name == "":
        return 'The character should have a name'
    elif len(name) > 10:
        return 'The character name is too long'
    elif " " in name:
            return 'The character name should not contain spaces'
    
    if type(strength) != int or type(intelligence) != int or type(charisma) != int:
        return 'All stats should be integers'
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    else:
        if strength + intelligence + charisma != 7:
            return 'The character should start with 7 points'

    output = name + "\n"
    output += dot("STR", strength) + "\n"
    output += dot("INT", intelligence) + "\n"
    output += dot("CHA", charisma)
    return output
