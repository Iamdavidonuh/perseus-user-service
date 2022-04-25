# Perseus User Service Challenge

[![Perseus Tests](https://github.com/Iamdavidonuh/perseus-user-service/actions/workflows/test.yml/badge.svg)](https://github.com/Iamdavidonuh/perseus-user-service/actions/workflows/test.yml)

# Table of Contents
1. [Summary](#Summary)
2. [Installation](#Installation)
3. [Alternatively, Run with Docker](#Using%20Docker)
4. [Navigation](#Navigation)
5. [Endpoints](#Endpoints)

### Summary
The objective of this exercise is to implement a rest-service which is able to:

- Create new user with contact data
- Return user by id
- Return user by name
- Add additional mail/phone data
- Update existing mail/phone data
- Delete user

The data objects are defined as followed:
```
User:
    id: <int>
    lastName: <string>
    firstName: <string>
    emails: List<Email>
    phoneNumbers: List<PhoneNumber>

Email:
    id: <int>
    mail: <string>
    
PhoneNumber:
    id: <int>
    number: <string>
```

### Constraints
- You provide straightforward documentation how to build and run the service
- Submitted data is stored in database (free choice which one)
- You can only use the following programming languages: Scala, Java, Python


### Bonus
- You let your service run within a container based environment (Docker, Kubernetes)
- You provide documentation of your services API endpoints
- Your service is covered with tests


## Installation


- Install Postgres

        sudo apt-get install postgresql postgresql-contrib postgis

- Create Postgres User

        sudo su postgres -c "psql -c \"CREATE USER perseus_user WITH PASSWORD 'perseus_pass';\""
    
- Create Postgres Databse

        sudo su postgres -c "psql -c \"CREATE DATABASE perseus_db OWNER perseus_user;\""

- Install virtualenv for creating virtual environments

        pip3 install virtualenv

- Set up virtual environment

        virtualenv -p python3.8 .virtualenv 

- Activate virutalenv

        source .virtualenv/bin/activate

- Install requirements

        pip3 install -r requirements.txt

- Copy the settings file

        cp perseus-user-service/perseus/settings/default.py perseus-user-service/perseus/settings/local_settings.py

- Run migrations before starting the server.

        python manage.py migrate

- Start the server

        python manage.py runserver

- Run Tests

        python manage.py test

### Using Docker
- run using docker compose

        docker-compose up


## Navigation:

You can navigate the application using:

- ### Django Rest API root

    on your browser, go to ``127.0.0.1:8000``

- ### Using Swagger UI

    go to ``127.0.0.1:8000/swagger/``    


## Endpoints


- ### Users

     - Create a user

        ``` POST "http://localhost:8000/users" ```
        
        ```
        {
                "user_emails": [
                        {
                        "mail": "testuser@gmail.com",
                        },
                ],
                "user_phone_numbers": [
                        {
                        "number": "911"
                        },
                ],
                "lastName": "testing",
                "firstName": "user"
        }
        
        ```
        ```
        response:
        
            {
                "id": 1,
                "lastName": "testing",
                "firstName": "user",
                "emails": [
                "testuser@gmail.com"
                ],
                "phoneNumbers": [
                "911"
                ]
           }
        ```

    - Get all users

        ``` GET "http://localhost:8000/users" ```
        ```
        response:
        
        [

                {
                        "id": 1,
                        "lastName": "testing",
                        "firstName": "user",
                        "emails": [
                            "testuser@gmail.com"
                        ],
                        "phoneNumbers": [
                            "911"
                        ]
                }
        ]
        ```
    - Get a User by ID

        ``` GET "http://localhost:8000/users/<user_id>/" ```
        ```
        Response

            {
                "id": 1,
                "lastName": "testing",
                "firstName": "user",
                "emails": [
                "testuser@gmail.com"
                ],
                "phoneNumbers": [
                "911"
                ]
           }
        ``` 
    - Update a User

        ``` PUT "http://localhost:8000/users/<user_id>/" ```
        ```
        example payload:

            {
                    "lastName": "Updated",
            }

        ```
        ```
        Response

          {
                "id": 1,
                "lastName": "Updated",
                "firstName": "user",
                "emails": [
                "testuser@gmail.com"
                ],
                "phoneNumbers": [
                "911"
                ]
           }
        ``` 


    - DELETE a user 

        ``` DELETE "http://localhost:8000/users/<user_id>/"```
        ```
        Response
        

            {}
        ```

- ### User Email

     - CREATE and Add an email to a user

        ``` POST "http://localhost:8000/user-email/" ```
        
        ```
        {
                "mail": "testuser2@gmail.com",
                "user": 1
        }
        
        ```
        ```
        response:
        
            {
                "id": 1,
                "mail": "testuser2@gmail.com",
                "user": 1
            }
        ```

    - GET a user's email address by email id

        ``` GET "http://localhost:8000/user-email/<email_id>" ```

        ```
        response
        {
                "id": 1,
                "mail": "testuser2@gmail.com",
                "user": 1
        }
        ```


    - UPDATE a User's email address

        ``` PUT "http://localhost:8000/user-email/<email_id>" ```
        ```
        {
                "mail": "updated123@gmail.com"
        }
        
        ```
        ```
        response:
        
        {
                "id": 3,
                "mail": "updated123@gmail.com",
                "user": 1
        }
        ```

   - DELETE a user 

        ``` DELETE "http://localhost:8000/user-email/<email_id>/"```
        ```
        Response
        

            {}
        ```

- ### User's Emails

    - Get a user's emails

        ``` GET "http://localhost:8000/user-emails/<user_id>/" ```
        ```
        response:
        
        [
                {
                "id": 1,
                "mail": "user@example.com",
                "user": 1
                }
        ]
        ```

- ### User Phone Number

     - CREATE and Add an phone number to a user

        ``` POST "http://localhost:8000/user-phone-number/" ```
        
        ```
        {
                "number": "2129001",
                "user": 1
        }
        
        ```
        ```
        response:
        
            {
                "id": 2,
                "number": "2129001",
                "user": 1
            }
        ```

    - GET a user's phone number by phone_number_id

        ``` GET "http://localhost:8000/user-phone-number/<phone_number_id>" ```

        ```
        response
        {
                "id": 1,
                "number": "911",
                "user": 1
        }
        ```


    - UPDATE a User's phone number

        ``` PUT "http://localhost:8000/user-phone-number/<phone_number_id>" ```
        ```
        {
                "number": "00001"
        }
        
        ```
        ```
        response:
        
        {
                "id": 1,
                "number": "00001",
                "user": 1
        }
        ```

   - DELETE a user 

        ``` DELETE "http://localhost:8000/user-phone-number/<phone_number_id>/"```
        ```
        Response
        

            {}
        ```

- ### User's Phone Numbers

    - Get a user's phone numbers

        ``` GET "http://localhost:8000/user-phone-number/<user_id>/" ```
        ```
        response:
        
        [
                {
                "id": 1,
                "number": "00001",
                "user": 1
                },
                {
                "id": 2,
                "number": "2129001",
                "user": 1
                }
        ]
        ```

