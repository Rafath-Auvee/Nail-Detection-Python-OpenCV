import requests
import os
import csv
from urllib.parse import urlparse
import urllib
import pandas as pd

file_url = "https://madarskom2.adortatechnologies.com/wp-content/themes/twentytwentytwo-child/student_image_data.php"


file_data = requests.get(file_url).content
with open("historical.csv", "wb") as file:
    file.write(file_data)

# with open('historical.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     next(csv_reader)
#     for row in csv_reader:
#         basename = os.path.basename(urlparse(row[2]).path)
#         # filename = '{}/{}/{}'.format(row[2], row[1], basename)
#         urllib.request.urlretrieve(basename)

donwloads_images = [ ]
df = pd.read_csv('historical.csv')
# print(df)
donwloads_images.append(df['image'])
print(df['image'][0])
print(donwloads_images)

for image in donwloads_images:
    testfile = urllib.URLopener()
    testfile.retrieve(f'{image}', f"{image}.jpg")