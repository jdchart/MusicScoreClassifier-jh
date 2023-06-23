from .runModel import *

def process(model, toProcess):
    if isinstance(toProcess, str):
        return classify_image(model, toProcess)
    else:
        return classify_images(model, toProcess)