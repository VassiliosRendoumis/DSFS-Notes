# -*- coding: utf-8 -*-
"""
Created on Mon May 02 22:13:49 2016

"""
from __future__ import division
from collections import Counter, defaultdict
from matplotlib import pyplot as plt

##########################
#                        #
# FINDING KEY CONNECTORS #
#                        #
##########################

users = [
            {"id":0, "name":"Hero"},
            {"id":1, "name":"Dunn"}, 
            {"id":2, "name":"Sue"},
            {"id":3, "name":"Chi"},
            {"id":4, "name":"Thor"},
            {"id":5, "name":"Clive"},
            {"id":6, "name":"Hicks"},
            {"id":7, "name":"Devin"},
            {"id":8, "name":"Kate"},
            {"id":9, "name":"Klein"}
        ]

def print_users():
    """Prints all users with their ID and name"""
    for user in users:
        print ''.join(["ID = ", str(user["id"]), ", Name = ", str(user["name"])])

        
# Friendship data
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
               
               
def print_friendships():
    """Prints the friendship relation between user a and b for all users"""
    
    for fs in friendships:
        print fs

# Let's add another field to every user dictionaryin the users list.
# This new field is the user's friends list and it is ... a list.
# First we add an empty list of friends to each user.
    
for user in users:
    user["friends"] = []
 

for i, j in friendships:
    users[i]["friends"].append(users[j]) # because j is a friend of i
    users[j]["friends"].append(users[i]) # because, since j is a friend of i,
                                         # i is a friend of j

   
    
def print_friends_number():
    """Prints out the number of friends for each user"""
    
    for user in users:
        print ''.join([str(user["name"]), " has ", str(len(user["friends"])), " friends"])


def my_number_of_friends(user_name):
        
    """Returns the number of friends a user has.
       This function can be used when you know the
       user name.
    """
    if user_name not in [user["name"] for user in users]:
        return ''.join([user_name, " not in users dump"])   
    else:
        for user in users:
            if user["name"] == user_name:
                return len(user["friends"])


def number_of_friends(user):
    """How many friends does user have?"""
    
    return len(user["friends"])


def my_total_connections():
    return sum(len(user["friends"]) for user in users)
 
total_connections = sum(number_of_friends(user) for user in users)


average_number_of_connections = total_connections / len(users)


# Hence, the average number of connections is:
#print average_number_of_connections


################################
#                              #
# DATA SCIENTISTS YOU MAY KNOW #
#                              #
################################


# Let's find the most connected people and add them in a list

num_friends_by_id = [(user["id"], len(user["friends"])) for user in users]


# Let's sort the list from most connected to less connected users
       
#print sorted(num_friends_by_id, key = lambda(user_id, num_friends): num_friends,
#       reverse = True)

 
def friends_of_friend_ids_bad(user):
    # "foaf" is short for "friend of a friend"
    return [foaf["id"]
            for friend in user["friends"]  # for each of user's friends
            for foaf in friend["friends"]] # get each of _their_ friends
    

# Here we see that people are friends-of-friends in multiple ways:      
#print [friend["id"] for friend in users[0]["friends"]]
#print [friend["id"] for friend in users[1]["friends"]]
#print [friend["id"] for friend in users[2]["friends"]]

def not_the_same(user, other_user):
    """Two users are not the same if the have different ids"""
    return user["id"] != other_user["id"]
    

def not_friends(user, other_user):
    """other_user is not a friend of user if he is not in user["friend"]"""
    
    return all(not_the_same(friend, other_user) for friend in user["friends"])
    

def friends_of_friend_ids(user):
    return Counter(foaf["id"]
            for friend in user["friends"] # for each of my friends 
            for foaf in friend["friends"] # count *their* friends
            if not_the_same(user, foaf)   # who aren't me
            and not_friends(user, foaf))  # and aren't my friends
            

# Let's check out with whom Chi (id 3) has common friends and how many           
# print friends_of_friend_ids(users[3])

# The result should be Counter({0: 2, 5: 1})
# That is, user Chi has two common friends with user Hero (id 0)
# and one common friend with user Clive (id 5)


interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):
    """Returns users with certain interest"""
    return [user_id 
            for user_id, user_interest in interests 
            if user_interest == target_interest]
                
# Let's build an index from interests to users:                
# keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

#print user_ids_by_interest

# Although, defaultdicts belong to the high performance containers family in Python,
# you can use also a common dictionary, like so:
my_user_ids_by_interest = {j:[] for i, j in interests}

for k, v in my_user_ids_by_interest.iteritems():
    for user_id, interest in interests:
        if interest == k:
            my_user_ids_by_interest[k].append(user_id)
            
# print my_user_ids_by_interest
            
# Let's build also an index from users to interests:
# Keys are user_ids, values are lists of interests for that user_id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

#print interests_by_user_id

def most_common_interests_with(user_id):
    return Counter(interested_user_id
                    for interest in  interests_by_user_id[user_id]
                    for interested_user_id in user_ids_by_interest[interest]
                    if interested_user_id != user_id)

# Let's see who has common interests with user Hero (id 0) and what's their 
# number

#print most_common_interests_with(0)

# If we want to see how many interests in common user(s) have with a given user
# we can check the maximum number of common interests among users with 
# common interests
# print max([v for k, v in most_common_interests_with(0).items() ])


def max_common_interests(user_id):
    """Returns the maximum number of common interst given user
       has with other user(s).
    """
    
    return max([common_interests 
                for user, common_interests 
                in most_common_interests_with(user_id).iteritems()])
                

def users_with_max_common_interests(user_id):
    """Returns a list with users which have the same maximum
        number of common intersts with given user (via user_id)
    """
    
    num_of_max_common_intersts = max_common_interests(user_id)
    
    return [user 
            for user, interest_num 
            in most_common_interests_with(user_id).iteritems() 
            if interest_num == num_of_max_common_intersts]

              
def pretty_printing_users_with_common_interests(user_id):
    """Prints out a report providing which user(s) have the maximum number of
       common interests, with the given user (user is given via user_id)
    """
    
    print "User", users[user_id]["name"], "has", max_common_interests(user_id), \
          "interest(s) in common with user(s)", \
          ''.join([''.join([users[_]["name"], ", "]) 
                  for _ in users_with_max_common_interests(user_id)])     
    
# Let's check how many users have a maximum number of interests with user Sue
# and list them
# pretty_printing_users_with_common_interests(2)
    
    
    
###########################
#                         #
# SALARIES AND EXPERIENCE #
#                         #
###########################
    
    
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# Let's plot the salaries_and_tenures data in a scatter plot.

def scatter_plot_pair_list(some_pair_list, 
                   x_label = "xlabel", y_label = "ylabel", 
                   title = "Title"):
    """A helper function which plots a given list of pairs values with 
       some labels and title.
    """
    
    plt.scatter([_[1] for _ in some_pair_list], [_[0] for _ in some_pair_list])
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

# scatter_plot_pair_list(salaries_and_tenures, "Years of Experience", "Salary", "Salary by years of Experience")

# It seems a generic pattern exists: Salary(Tenure) ~ Tenure

# Let's create naive indexing of the salaries for each tenure
salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)
    
# keys are years, each value is average salary for that tenure
# We use here iteritems, since it is more efficient in python 2
average_salary_by_tenure = {tenure:sum(salaries)/len(salaries)
                            for tenure, salaries in salary_by_tenure.iteritems()}

#print average_salary_by_tenure
# This is not very usefull since none of the users have the same tenure

# Let's create a bucket of tenures, that is some range of tenure values and
# vs the salaries in this range
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"
        
# Let's group together the salarie corresponding to each bucket:
# Keys are tenure buckets, values are lists of salaries for that bucket
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)
    
# Finally, let's compute the average salary for each group:
average_salary_by_bucket = {tenure_bucket:sum(salaries)/len(salaries) 
                            for tenure_bucket, salaries 
                            in salary_by_tenure_bucket.iteritems()}
                            
#print average_salary_by_bucket

#################
#               #
# PAID_ACCOUNTS #
#               #
#################

account_payment_vs_tenure = [
                             (0.7, "paid"),
                             (1.9, "unpaid"),
                             (2.5, "paid"),
                             (4.2, "unpaid"),
                             (6, "unpaid"),
                             (6.5, "unpaid"),
                             (7.5, "unpaid"),
                             (8.1, "unpaid"),
                             (8.7, "paid"),
                             (10, "paid")
                             ]
                             
                                
# General naive pattern: Users with very little or with many years of 
# experience, pay their account, while users with average amount of experience
# don't. 
                                
def predict_apid_or_unpaid(years_of_experience):
    if years_of_experience < 3.0:
        return "paid"
    elif years_of_experience < 8.5:
        return "unpaid"
    else:
        return "paid"

######################
#                    #
# TOPICS OF INTEREST #
#                    #
######################

# We can look for the most popular interests, simply by counting the words in
# our interests list. However, the names of this list could be altered a little
# bit in order to avoid missbehavior with interests which are made up of two
# separate words, like decision trees. We could change that by replacing the
# space between the words with a minus (-) sign. We know though, that all
# interests have only one space at most and no one at minimum.

# Due to the fact that our list of interests is a list of tuples, we can't
# alter the string entry in this tupple. Instead we will crate a new list
# of interests with the interest syntax we want.

def cleans_interests_v1(list_of_interest):
    """Input is a list of pair tuples with first part the user id (int) 
       and second part a string (interest). It returns a similar data structure
       with only difference the substituion of spaces in the string part with
       the minus sign (-).
    """
    interests_v1 = []

    for _ in interests:
        if " " in _[1]: # if the interest includes a space
            space_index = _[1].index(" ") # get the index of this space
            interests_v1.append((_[0], 
                               ''.join([_[1][:space_index], "-", _[1][space_index + 1:]
                                    ])
                                    )) # add a tuple to the new list by substituting
                                       # the string part with correct syntax (no spaces)
                             
        else: # if no space is found, just add the tupple as it is
            interests_v1.append(_)
    return interests_v1

# Another way is to create a mechanism which removes the interests in question
# and adds the correct format, like so:

def cleans_interests_v2(list_of_interest):
    """Input is a list of pair tuples with first part the user id (int) 
       and second part a string (interest). It returns the initial list of 
       interests similar with only difference the substituion of spaces
       in the string part with the minus sign (-).
    """
    for _ in list_of_interest:  
        temp_list = []       # a temporary list of tupples we change
        indexes_to_dump = [] # a list of list indexes of the tuples we want to change
        
        if " " in _[1]:      # if the interest includes a space
        
            indexes_to_dump.append(list_of_interest.index(_))
            
            space_index = _[1].index(" ") # get the index of this space
            
            new_tupple = (_[0], ''.join([_[1][:space_index], "-", _[1][space_index + 1:]])) 
            
            temp_list.append(new_tupple) # add a tupple to the interests list by substituting
                                         # the string part with correct syntax (no spaces)
        else:
            pass                         # if there is nothing to change, just pass
            
        for _ in indexes_to_dump:        # for every index in our index list
        
            del list_of_interest[_]      # delete this tupple from the interests list
            
        list_of_interest = list_of_interest + temp_list # concatenate the reduced interests list
                                                        # and the list of altered tuples
    return list_of_interest  
      
# Now we can count the words. We will use a slightly different approach 
# then the original code of the book uses, since we don't have any spaces now.
# We will use our new list created by our helper function cleans_interests_v1.

words_and_counts_v1 = Counter(interest.lower() for user, interest in cleans_interests_v1(interests))                           

words_and_counts_v2 = Counter(interest.lower() for user, interest in cleans_interests_v2(interests))
                        
# We can see that both implementations of our helper function yield the same
# words and counts dictionaries    
                        
# This make it easy to list out words that accur more than once.
# Let's use just the words_and_counts_v1:
for word, count in words_and_counts_v1.most_common():
    if count > 1:
        print word, count
        
