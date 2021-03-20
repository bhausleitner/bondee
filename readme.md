# bondee

bondee is an application that helps you build meaningful relationships at work.

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

bondee is a web-application that matches an employees profile to a suitable counterprofile. Thereby, bondee's functional principle can be split into 3 main areas: gathering, engine, recommendation. 

![image](https://user-images.githubusercontent.com/58265021/111886590-16483a80-89cf-11eb-8c23-8bf771720a8b.png)

### Gathering 
In a first step, bondee collects data through numerous domains. Next to obvious data from an employees' CV (location, previous companies, previous roles, language, etc.), social media accounts (contact lists, intersts, image recognition on Insta, event attendance, etc) and HR related information (department, calendar time utilization), bondee also gathers potential employee growth fields through a indiviudalized survey. State of the art data preprocessing methods subsequently prep the data.


### Engine
In a next step, bondees core engine creates three different employee profiles: 
- growth profile
- discipline profile
- interests profile

By applying principal components analysis (reduce dataset to relevant features) and subsequent agglomerative hierachical clustering, bondee determines the best fitting employee match in the database (Employee A should spend more time with Employee B).

Ontop of that, bondee considers employee calendar utilization in order to assess the status quo of an employees current time utilization (How is the meeting time of Employee A distributed? How much time is Employee A already with Employee B,C,D, etc.). 

### Recommendation

In a final step all this information is summarized in an actionable and joyful text recommendation: "Hey there, it looks like you should spend more time with Employee B, here is a calendar invite, just send it over! 😊" 

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
