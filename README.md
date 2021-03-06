# One Left Foot API

## Description & Background

Ballroom dance is difficult to master. Practice partners make the process more enjoyable! One Left Foot helps you find a practice partner for dances that interest you. You can also search for dancers that share your skill level, whether you are a beginner, an intermediate, or advanced and looking to push your skills to higher heights.

## Technologies Used

##### Built with

- Python
- Django
- React [client](https://github.com/morriscodez/one-left-foot-client)

## Set Up

1.  Clone Repo:
   ```git clone git@github.com:morriscodez/one-left-foot-server.git```

2.  Virtual Environment with ```pipenv```
 
   ```
   pip3 install --user pipx
   pipx install pipenv
   ```
3. Run this command to install packages in the Pipfile
   ``` 
   pipenv install 
   ```
  

4.  Make an account with Cloudinary
 
5.  Input your Cloudinary name, api, and api secret in the ```.env.example``` file, then remove ```.example``` from the file and add ```.env``` to the ```gitignore```

6. Generate Django Secret Key
   - Run this command in terminal:
   
     ```
     python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

     ```
   - Copy the secret key output from terminal and pase it into your ```.env``` file as a value: ```SECRET_KEY=<paste random key output here>```
   

7.  ```python3 manage.py runserver``` for local server


