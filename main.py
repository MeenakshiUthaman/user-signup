from flask import Flask, request
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader (template_dir), autoescape=True)
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('signup.html')
    return template.render()
@app.route("/",methods=['POST'])
def welcome():
    User_name = request.form['user']
    length = len(User_name)
    if (length < 3 or length > 20):
        template = jinja_env.get_template('signup.html')
        return template.render(name_error="That's not a vaild username",input_name=User_name)
    for i in User_name:
        if (i == " "):
           template = jinja_env.get_template('signup.html')
           return template.render(name_error="That's not a vaild username",input_name=User_name)

    Password = request.form['password']
    verify_password = request.form['verify']
    length1 = len(Password)
    if (length1 < 3 or length1 > 20):
        template = jinja_env.get_template('signup.html')
        return template.render(pwd_error="That's not a vaild password",input_name=User_name)
    for j in Password:
        if (j ==" "):
            template = jinja_env.get_template('signup.html')
            return template.render(pwd_error="That's not a vaild password",input_name=User_name)
    if (Password != verify_password) or (not verify_password):
        template = jinja_env.get_template('signup.html')
        return template.render(verify_error="That's not a vaild verify password",input_name=User_name)

    Email = request.form['email']
    length2 = len(Email)
    if length2 == 0:
        template = jinja_env.get_template('welcome.html')
        return template.render(name =User_name)
    if (length2 < 3 or length2 > 20):
        template = jinja_env.get_template('signup.html')
        return template.render(email_error="That's not a vaild email",input_name=User_name, input_email=Email)
    for xa in Email:
        if(xa ==" "):
           template = jinja_env.get_template('signup.html')
           return template.render(email_error="That's not a vaild email",input_name=User_name, input_email=Email) 
    atPresentInEmail = False
    dotPresentInEmail = False
    for z in Email:
        if z =="@":
            atPresentInEmail = True
    for z in Email:
        if z == ".":
            dotPresentInEmail = True
    if (atPresentInEmail == False or dotPresentInEmail == False):
        template = jinja_env.get_template('signup.html')
        return template.render(email_error="That's not a vaild email",input_name=User_name, input_email=Email)
            
    template = jinja_env.get_template('welcome.html')
    return template.render(name =User_name)
    

app.run()



nup