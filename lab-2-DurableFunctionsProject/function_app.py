#Function_app.py

import azure.functions as func
import azure.durable_functions as df


import datetime
import json
import logging

app = func.FunctionApp()


def orchestrator_function(context: df.DurableOrchestrationContext):
    # Input image
    input_image = context.get_input()

    # Step 1: ResizeImage
    resized_image = yield context.call_activity('ResizeImage', input_image)

    # Step 2: GrayscaleImage
    grayscale_image = yield context.call_activity('GrayscaleImage', resized_image)

    # Step 3: WatermarkImage
    watermarked_image = yield context.call_activity('WatermarkImage', grayscale_image)

    return watermarked_image

main = df.Orchestrator.create(orchestrator_function)
