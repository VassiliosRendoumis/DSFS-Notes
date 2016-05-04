# -*- coding: utf-8 -*-
"""
Created on Mon May 02 22:13:49 2016

"""
from __future__ import division
from collections import Counter

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

        

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
               
               
def print_friendships():
    """Prints the friendship relation between user a and b for all users"""
    
    for fs in friendships:
        print fs

# Let's add another field to every user dictionaryin the users list.
# This new field is the user's friends list and it will be a list.
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
            
            
print "Test"