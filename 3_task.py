"""
sample_object = [
{'Name':'Farhad', 'Surname:'Malik', 'Blogs':{'BlogName:'Python1','Date1':'20180901'}},
{'Name':'Farhad2', 'Surname:'Malik2', 'Blogs':{'BlogName:'Python3','Date1':'20180101'}}
]

Результат:
dictionary_1 = [
{'Name':'Farhad', 'Surname:'Malik'},
{'Name':'Farhad2', 'Surname:'Malik2'}
]
dictionary_2 = [
{'ParentId':'Farhad', 'BlogName:'Python1','Date1':'20180901'},{'ParentId':'Farhad2','BlogName:'Python3','Date1':'20180101'}
]
"""

sample_object = [
    {'Name': 'Farhad', 'Surname': 'Malik', 'Blogs': {'BlogName': 'Python1', 'Date1': '20180901'}},
    {'Name': 'Farhad2', 'Surname': 'Malik2', 'Blogs': {'BlogName': 'Python3', 'Date1': '20180101'}}
]
dict1 = []
persons = {}

blog_person_info = {}
dict2 = []

for person in sample_object:
    for key, value in person.items():
        if key == 'Name':
            blog_person_info[key] = value
        elif key == 'Blogs':
            for blog_key, blog_date in value.items():
                blog_person_info[blog_key] = blog_date
            dict2.append(blog_person_info.copy())
            continue
        persons[key] = value
    dict1.append(persons.copy())

print(dict1)
print(dict2)