import numpy as np

def invariant_representation(color, illumination):
    """
    Illumination-invariant representation
    (removes lighting effect)
    """
    return color - illumination


def raw_representation(color):
    """
    Non-invariant representation
    """
    return color
