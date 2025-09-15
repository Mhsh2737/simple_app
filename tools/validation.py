import re

def name_validator(name):
    if re.match(r"^[A-Za-z0-9\s]{3,30}$", name):
        return name
    else:
        raise ValueError("Invalid name!!!")


def model_validator(model):
    if re.match(r"^[A-Za-z0-9\s]{3,30}$", model):
        return model
    else:
        raise ValueError("Invalid model!!!")

def plate_validator(plate):
    if re.match(r"^\d{2}.\d{3}_.{4}\d{2}$",plate):
        return plate
    else:
        raise ValueError("Invalid plate!!!")


