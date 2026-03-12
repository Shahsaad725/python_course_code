test_settings = {
    "name" : "Saad",
    "grade": 12
}

def add_setting(dict_set, key_value):
    key = key_value[0].lower()
    value = str(key_value[1]).lower()
    if key not in dict_set:
        dict_set[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
    else:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

def update_setting(dict_set, key_value):
    key = key_value[0].lower()
    value = str(key_value[1]).lower()
    if key in dict_set:
        dict_set[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dict_set,key):
    key = key.lower()
    if key in dict_set:
        del dict_set[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(dict_set):
    if not dict_set:
        return "No settings available."
    else:
        output = "Current User Settings:\n"
        for key, value in dict_set.items():
            output += f"{key.capitalize()}: {value}\n"
    return output
