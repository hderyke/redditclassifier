import requests
import json
import sys
# Replace 'YOUR_API_KEY' with your Mandrill API key
API_KEY = 'md-j5JDFuYJ5BjJbzGdpOBFBQ'


def send_email(subject, message, recipient_email, sender_email):
    url = 'https://mandrillapp.com/api/1.0/messages/send.json'
    headers = {'Content-Type': 'application/json'}

    data = {
        'key': API_KEY,
        'message': {
            'from_email': sender_email,
            'to': [{'email': recipient_email}],
            'subject': subject,
            'text': message
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(message)
    if response.status_code == 200:
        print('Email sent successfully!')
    else:
        print('Failed to send email. Status Code:', response.status_code)
        print('Response:', response.text)

def read_message():
    with open(sys.argv[1],'r') as file:
        return file.read()


# Example usage:
if __name__ == '__main__':
    subject = 'Reddit posts of interest'
    message = read_message();
    recipient_email = sys.argv[2]
    sender_email = 'redditbot@leaguejoe.com'

    send_email(subject, message, recipient_email, sender_email)
