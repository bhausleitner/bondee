# Bondee

Bondee is an application that helps you build meaningful relationships at work.

## Installation

Create a python3 virtual env and use the package manager [pip](https://pip.pypa.io/en/stable/) to install following packages:

```bash
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
pip install pickle
pip install sklearn
pip install tqdm
pip install random
```

## How it works

Bondee is a web-application that matches an employees profile to a suitable counterprofile. Thereby, Bondee's functional principle can be split into 3 main areas: gathering, engine, recommendation. 

![image](https://user-images.githubusercontent.com/58265021/111886590-16483a80-89cf-11eb-8c23-8bf771720a8b.png)

### Gathering 
In a first step, Bondee collects data through numerous domains. Next to obvious data from an employees' CV (location, previous companies, previous roles, language, etc.), social media accounts (contact lists, intersts, image recognition on Insta, event attendance, etc) and HR related information (department, calendar time utilization), Bondee also gathers potential employee growth fields through a indiviudalized survey. State of the art data preprocessing methods subsequently prep the data.


### Engine
In a next step, Bondees' core engine creates three different employee profiles: 
- growth profile
- discipline profile
- interests profile

By applying principal components analysis (reduce dataset to relevant features) and subsequent agglomerative hierachical clustering, Bondee determines the best fitting employee match in the database (Employee A should spend more time with Employee B).

Ontop of that, Bondee considers employee calendar utilization in order to assess the status quo of an employees current time utilization (How is the meeting time of Employee A distributed? How much time is Employee A already with Employee B,C,D, etc.). 

### Recommendation

In a final step all this information is summarized in an actionable and joyful text recommendation: "Hey there, it looks like you should spend more time with Employee B, here is a calendar invite, just send it over! 😊" 

## Additional Notes

For the context of this hackathon we've been scraping example data and created our own dataset (see `data_exploration/scraping_dataset.py`).

Getting Bondee out there generating valuable customer feedback will be of utmost importance to Bondees' success! This is why we've been focusing on leaving out unnecessary complexity in the first version of Bondee. We've been intentionally utilizing basic statistical methods (PCA and agglomerative clustering). Through that, we'll enable light weight deployment as well as deterministic behavior, which will help us tremendously to bring Bondee into companies' hands asap! 
 
In the weeks to come we will, of course, be working hard to further improve Bondee with state of the art machine learning and NLP methods to continously build meaningful relationships at work!
 
## License
[MIT](https://choosealicense.com/licenses/mit/)
