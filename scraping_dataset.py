## Importing Libraries
import requests
import pandas as pd
import time
import random
import re
import numpy as np
import pickle as pickle
from tqdm import tqdm_notebook as tqdm
from bs4 import BeautifulSoup as bs

# Randomizing the refresh rate
seq = [i/10 for i in range(8,18)]

# Creating a list of bios
biolist = []

# Gathering bios by looping and refreshing the web page
for _ in tqdm(range(10)):
    
    # Refreshing the page
    page = requests.get("https://www.character-generator.org.uk/bio/")
    soup = bs(page.content)
    
    try:
        # Getting the bios
        bios = soup.find('div', class_='row no-margin for-sign').find_all('p')

        # Adding to a list of the bios
        biolist.extend([re.findall('"([^"]*)"', i.text) for i in bios])
    except:
        pass
    
    # Sleeping 
    time.sleep(random.choice(seq))
    
# Creating a DF from the bio list
bio_df = pd.DataFrame(biolist, columns=['Bios'])

# List of potential Dating questions/categories
qs = ['Movies',
      'TV',
      'Religion',
      'Music',
      'Sports',
      'Books',
      'Politics']

# Creating a DF of the questions/categories
topic_df = pd.DataFrame(columns=qs)

# Filling in Data
for i in topic_df.columns:
    
    # Range of numbers to represent different labels in each category
    topic_df[i] = np.random.randint(0,10, bio_df.shape[0])
    
final_df = bio_df.join(topic_df)
final_df

# Exporting the complete DF
with open("profiles.pkl", "wb") as fp:
    pickle.dump(final_df, fp)