# Step 1: Import necessary modules
import os
import json
from openai import OpenAI
from data import training_data, validation_data

# Step 2: Initialize the OpenAI client with the API key from environment variables
client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
)

# Step 3: Define the names of the training and validation data files
training_file_name = "training_data.jsonl"
validation_file_name = "validation_data.jsonl"


# Step 4: Function to prepare data and write it to a JSONL file
def prepare_data(dictonary_data: list[dict], final_file_name):
    with open(final_file_name, 'w') as outfile:
        for entry in dictonary_data:
            json.dump(entry, outfile)
            outfile.write('\n')


# Step 5: Call the prepare_data function for both training and validation data
prepare_data(training_data, training_file_name)
prepare_data(validation_data, validation_file_name)

# Step 6: Upload the training data file to OpenAI and get the file ID
training_file_id = client.files.create(
    file=open(training_file_name, "rb"),
    purpose="fine-tune",
)

# Step 7: Upload the validation data file to OpenAI and get the file ID
validation_file_id = client.files.create(
    file=open(validation_file_name, "rb"),
    purpose="fine-tune",
)

# Step 8: Print the file IDs for reference
print(f"Training file ID: {training_file_id}")
print(f"Validation file ID: {validation_file_id}")

import pdb; pdb.set_trace()

# Step 9: Create a fine-tuning job with the uploaded files and specific hyperparameters


# Step 10: Retrieve the job ID and status from the response


# Step 11: Print the job ID and initial status


# Step 12: Import signal and datetime modules for handling interruptions and timestamps
import signal
import datetime

# Step 13: Define a signal handler to manage interruptions


# Step 14: Print the start of event streaming


# Step 15: Set up the signal handler for keyboard interruptions


# Step 16: List events for the fine-tuning job and print them with timestamps


# Step 17: Import time module for sleep function
import time

# Step 18: Check the status of the fine-tuning job and wait if it is not in a terminal state


# Step 19: Print the status of other fine-tuning jobs in the subscription


# Step 20: Retrieve and print the ID of the fine-tuned model
