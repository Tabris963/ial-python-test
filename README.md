# Language exercises

Put each solution in a separate python module named `excerciseN.py` where `N` is the number of the excercise.

    mkdir language_excercises
    cd language_excercises
    touch excercise1.py
    touch excercise2.py
    # ... and so on ...

1. Write a function `dict_values_ascending` that accecpts a dictionary as an argument and returns a list of dictionary *values* in ascending order
 
2. Write a function named `add_dict(dict_1, dict_2)` that joins the two dictionaries provided as arguments and returns a single dictionary with all the items of `dict_1` and `dict_2`

3. Write a function that counts the lines of a file. The file name is provided as a function argument. It returns the number of lines in the file.

4. write a module `esercizio4.py` that reads a list of words from the command line and prints them out on standard output each one inside a `<p>` HTML tag:

    $ python esercizio5.py ciao hey
    <p>ciao</p>
    <p>hey</p>


5. write a python module `esercizio5.py` that reads the remote HTTP endpoint http://ialpython.apiary.io/laboratories and prints to standard output all the laboratories with network status `down`


# Django Excercises

## Instructions

this goes in a `django_excercises` folder under `/vagrant/python-test`

    mkdir /vagrant/python-test/django_excercises
    cd /vagrant/python-test/django_excercises
    touch school_client.py
    # ... and so on ....


## Features

Implement a django server and a python command line client to manage a school's enrolment system.

Components:

 - django project named `school_pro`
 - django app named `enrolment`
 - python command line client named `school_client.py`

The enrolment app exposes a web service for the command line client to enroll students saving their details in a db.


### Store student

The school staff uses the command line client to add a student to the database.

    $ python school_client.py enroll John Doe
    OK

The command line client prints `OK` if the operation went correctly.

The clerk can add more students:

    $ python school_client.py enroll Jane Austen
    OK
    $ python school_client.py enroll Jane Austen
    OK
    $ python school_client.py enroll Jane Austen
    OK


### Search students

The school staff uses the command line client to list all the enrolled students

    $ python school_client.py search Jane
    OK listing results:
    Jane Austen
    Jane Austen
    Jane Austen


The client first displays an informative line and then prints out all the matching students one per line.

Bonus: search on both first name and last name.


### Persist enrollment date and time  (optional)

The system saves date and time of enrolment when the staff enrols a student.

The enrolment date and time is displayed in the search results.


    $ python school_client.py search Jane
    OK listing results:
    Jane Austen enrolled on 2014-01-01T12:00:00
    Jane Austen enrolled on 2014-01-01T12:00:00
    Jane Austen enrolled on 2014-01-01T12:00:00


*HINT 1* use DateTimeField for models

*HINT 2* datetime is not natively json-encodable, turn it into a string before
encoding it


# Submission

Push all the excercises to your github repo and make `mpaolini` a contributor:

 - login into github and create a new repo named `ial-python-test`
 - go to repo settings (bottom right), then collaborators (left column), write `mpaolini` and click "Add collaborator"
 - `git init`
 - `git add .`
 - `git commit -m test finished`
 - `git remote add origin https://github.com/<username>/ial-python-test.git` 
 - `git push -u origin master`
