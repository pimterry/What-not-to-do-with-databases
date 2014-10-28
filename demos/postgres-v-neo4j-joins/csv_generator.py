from collections import namedtuple
import csv

User = namedtuple('User', ['id', 'name'])

def generate_user_table(num_users):
    return [User(i, "User %s" % i) for i in range(0, num_users)]

def generate_friendships(users, num_friends):
    for user_index, user in enumerate(users):
        for friend_index in range(1, num_friends + 1):
            friend_user_index = (user_index + friend_index) % len(users)
            friend = users[friend_user_index]
            yield (user.id, friend.id)

if __name__ == "__main__":
    users = generate_user_table(10000)
    friendships = generate_friendships(users, 10)

    with open('users.csv', 'w') as user_file:
        writer = csv.writer(user_file, lineterminator='\n')
        writer.writerows(users)

    with open('friendships.csv', 'w') as friendships_file:
        writer = csv.writer(friendships_file, lineterminator='\n')
        writer.writerows(friendships)