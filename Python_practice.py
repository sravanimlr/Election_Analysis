my_dict={}
counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}  
my_dict{}
voting_dict=[{"county":"Arapahoe","registered_voters":422829},
                {"county": "Denver","registered_voters":463353},
                {"county": "Jefferson","registered_voters:"432438}]
for counties_dict in voting_dict:
    for value in counties_dict.values():
        print(value)