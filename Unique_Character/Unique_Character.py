def unique_character(str):
    
    str_list = []
    for character in str:
        str_list.append(character)


    output = []
    letter_block = []
    for letter in str_list:
        if letter in output:
            output.remove(letter)
            letter_block.append(letter)
        
        elif letter in letter_block:
            continue

        else:
            output.append(letter)
    
    return output




