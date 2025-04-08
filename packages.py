# installing the necessary libraries and packages
# for the project
# using pip to install the packages

# requests
# for making HTTP requests

import requests

response = requests.get('https://api.github.com')

print(response.status_code)  # 200
print(response.json())  # {'current_user_url': 'https://api.github.com/user', ...}

# request.get()
# for making GET requests
# request.post()
# for making POST requests
# request.put()
# for making PUT requests
# request.delete()
# request.patch()   
# for making PATCH requests
# request.head()
# for making HEAD requests


# PIP COMMANDS SUMMARY
# pip install requests
# pip install pandas
# pip install numpy
# pip install matplotlib
# pip install seaborn



# flask
# for creating web applications
# pip install flask
# pip install flask-restful
# pip install flask-cors
# pip install flask-socketio
# pip install flask-login
# pip install flask-mail
# pip install flask-migrate
# pip install flask-script
# pip install flask-wtf     
# pip install flask-admin
# pip install flask-sqlalchemy
# pip install flask-redis
# pip install flask-cache   





