""""""
import pymysql

queries = {
    "tweet": "insert into tweet (user, message) values ('{}', '{}')",
    "show": "select * from tweet order by tstamp",
    "user": "select * from tweet where user = '{}'",
    "like": "update tweet SET likes = likes + 1 where id = {}"
}


def display_tweet(tweet_dict):
    print("[" + str(tweet_dict['id']) + "]", end=" ")
    print(tweet_dict['user'] + ", {} likes".format(
        tweet_dict['likes']), end=': ')
    print(tweet_dict['message'])


def show_options():
    for item in queries.keys():
        print("  > " + item)
    print("  > quit/exit")

connection = pymysql.connect(host='10.224.45.113', user='cs101', db='twitter',
                             autocommit=True)


cursor = connection.cursor(pymysql.cursors.DictCursor)

username = input("What is your username?\n> ")

print("Welcome to Twitter v2")
while True:
    show_options()
    query = input("Please enter your query: ")
    if query in queries.keys():
        current_query = queries[query]

        if query == 'tweet':
            message = input("Type your message here: ")
            current_query = current_query.format(
                username, message[0:140])
            cursor.execute(current_query)
            print("Successfully inserted!")

        elif query == 'show':
            cursor.execute(current_query)
            for item in cursor:
                display_tweet(item)

        elif query == 'user':
            user_id = input("Whose tweets would you like to see? ")
            current_query = current_query.format(user_id)
            cursor.execute(current_query)
            for item in cursor:
                display_tweet(item)

        elif query == 'like':
            tweet_id = int(input("Which tweet did you like? "))
            try:
                current_query = current_query.format(tweet_id)
                cursor.execute(current_query)
                print("Liked.")
            except ValueError:
                print("Please try again.")

    elif query == 'quit' or query == 'exit':
        break

    else:
        print("Instructions unclear. Please try again.")

connection.close()
