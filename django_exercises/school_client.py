import requests
import json
import argparse

HOST = 'localhost:8000'

def enroll_student(first_name, last_name):
    resp =requests.post(
        'http://{}/request'.format(HOST),
        json.dumps({'first_name':first_name,'last_name':last_name}))
    if resp.status_code == 200:
        print 'OK'
    else:
        print 'Errore'

def search_student(student):
    resp = requests.get('http://{}/enroll'.format(HOST))
    content = json.loads(resp.content)
    for stud in content:
        if(stud['first_name'] == student or stud['last_name']== student):
            print stud['first_name'] + " " + stud['last_name']

parser = argparse.ArgumentParser('student client')
parser.add_argument('command')
parser.add_argument('--fist_name')
parser.add_argument('--last_name')
parser.add_argument('--student')
args = parser.parse_args()

if args.command == 'enroll':
    enroll_student(args.first_name, args.last_name)
elif args.command == 'search':
    search_student(args.student)
else:
    print 'Errore'