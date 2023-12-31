import os
import pandas as pd
from deepface import DeepFace

# Specify the folder containing the images
image_folder = 'faceimages'

# Create a list to store data for CSV
csv_data = []

# Process each image in the folder
for filename in os.listdir(image_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(image_folder, filename)

        try:
            # Use deepface to get gender, race, and age
            result = DeepFace.analyze(image_path)

            # Extract gender, race, and age from the result
            gender = result['gender']
            race = result['dominant_race']
            age = result['age']

            # Append data to the CSV list
            csv_data.append([filename, gender, race, age])

        except Exception as e:
            print(f"Error processing image {filename}: {str(e)}")

# Create a DataFrame from the CSV data
#columns = ['Filename', 'Gender', 'Race/Ethnicity', 'Age']
#df = pd.DataFrame(csv_data, columns=columns)

# Write data to CSV file
#csv_file_path = 'output.csv'
#df.to_csv(csv_file_path, index=False)

#print(f"CSV file '{csv_file_path}' created successfully.")
