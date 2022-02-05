#!/usr/bin/env python3
users = [
        { "id": 0, "name": "Hero" },
        { "id": 1, "name": "Dunn" },
        { "id": 2, "name": "Sue" },
        { "id": 3, "name": "Chi" },
        { "id": 4, "name": "Thor" },
        { "id": 5, "name": "Clive" },
        { "id": 6, "name": "Hicks" },
        { "id": 7, "name": "Devin" },
        { "id": 8, "name": "Kate" },
        { "id": 9, "name": "Klein" }
        ]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
        (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for friends in friendship_pairs :
    print("{} is a friend to {}".format(friends[0],friends[1]))

friendships = {user['id']:[] for user in users}

for i,j in friendship_pairs :
	friendships[i].append(j)
	friendships[j].append(i)
	print(i,j)
print(friendships)