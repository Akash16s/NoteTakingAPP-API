# NoteTakingAPP-API
Agenda is to create API's for a note-taking web application.

# API
#### 1> SignUp : http://127.0.0.1:8000/note/signup/  
POST:
{
	"username":"Akash",
	"email":"akash@gmail.com",
	"password":"******"
}

#### 2> Login : http://127.0.0.1:8000/note/login/
POST:
{
   "username":"Akash,
   "password":"*****"
}

#### 3> View Note : http://127.0.0.1:8000/note/?query  
GET
#### 4> Write Note: http://127.0.0.1:8000/note/write/

POST and PUT
{
  "id":1,
  "note":"note is here"
}
