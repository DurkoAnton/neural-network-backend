from flask import Flask,jsonify

app = Flask(__name__)

Student = [
{
'id': 1,
'firstName': 'Aditya',
'lastName': 'Malviya',
'age': '24'
},
{
'id': 2,
'firstName': 'Aman',
'lastName': 'Mehta',
'age': '25'
},
{
'id': 3,
'firstName': 'Nuclear',
'lastName': 'Geeks',
'age': '26'
}
]

def get_Student():
   return "hello"


if __name__ == '__main__': 
  get_Student()