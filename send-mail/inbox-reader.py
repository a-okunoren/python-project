# references: https://www.techgeekbuzz.com/how-to-read-emails-in-python/, https://www.youtube.com/watch?v=6DD4IOHhNYo&list=PLEsfXFp6DpzQjDBvhNy5YbaBx9j-ZsUe6&index=9

import imaplib  # Import library for reading inbox
import email

host = 'imap.gmail.com'

username = 'atoprintsuk@gmail.com'
password = input("Type your email password")
# specify what you want read from the inbox
read_criteria = '(FROM "emails@mail.etsy.com")'


def read_inbox(username, password, read_criteria):
    # initialise an imap object we can use in this application
    imap = imaplib.IMAP4_SSL(host)
    imap.login(username, password)
    # you are choosing your default mailbox by specifying 'inbox'
    imap.select("inbox")

    email_list = []  # this will be a list of emails. the email itself is a list of components
    email_data = {}  # dictionary for storing email data
    # divide the results of the search function (a tuple of two values) into _ and search data. we only want search data but _ stores the unecessary value still
    _, search_data = imap.search(None, read_criteria)

    # convert the results of search data into a list we can iterate through
    data_list = search_data[0].split()
    #cropped_list = [data_list[0], data_list[1], data_list[2], data_list[3]]
    print("Total messages from Dee: ", len(data_list))

    for item in data_list:
        # RFC822 returns the entire message body
        _, data = imap.fetch(item, '(RFC822)')  # item is the email id
        # the data object has a lot in it but it is element 0 that has the tuple that contains the email msg
        _, msg = data[0]
        # email library is converting the bytes msg
        email_msg = email.message_from_bytes(msg)
        for header in ['subject', 'to', 'from', 'date']:
           # print("{}:{}".format(header, email_msg[header]))
            # key is header, value is email content specific to the header
            email_data[header] = email_msg[header]
        for part in email_msg.walk():  # for every part of each email we loop through, do this: (walk() goes through the different parts that make up the email)
            if part.get_content_type() == "text/plain":  # works well with type. messy with text/html
                body = part.get_payload(decode=True).decode()
             #   print("Body: ", body)
                email_data["body"] = body
        # for now this adds the list of email components as one list entry
        email_list.append(email_data)  # added dictionary to list

    return email_list  # we have an array of emails!


print(read_inbox(username, password, read_criteria))

# to do: finish that guy's video o
