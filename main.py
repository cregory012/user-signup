from flask import Flask, request, redirect, render_template


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/home")
def signup():
     return render_template("index.html")

def no_space(name):
     if name.count(" ") == 0:
          return True
     else:
          return False     

def right_length(name):
     if len(name) > 2 and len(name) < 21: 
          return True
     else:
          return False     

def valid_email(email):
     if right_length(email) and no_space(email) and email.count("@") == 1 and email.count(".")==1:
          return True
     else: 
          return False          


@app.route("/home", methods=['POST'])
def signup_validate():
     
     username = request.form['username']
     if not right_length(username) or not no_space(username):
          user_error = "That's not a valid username"
          username = ""
     else: user_error = ''     
     password = request.form['password']
     if not right_length(password) or not no_space(password):
          pass_error = "That's not a valid password"
     else: pass_error = ''     
     verify = request.form['verify']
     if password != verify:
          verify_error = "Passwords don't match"
     else: verify_error = ''     
     email = request.form['email']
     if not valid_email(email) and len(email) != 0:
          email_error = "That's not a valid email"
          email = ""
     else:
          email_error = ''     

     if user_error or pass_error or verify_error or email_error:
          password = ""
          verify = ""
          return render_template("index.html", username= username,
           password = password, verify = verify, email = email,
           user_error = user_error, pass_error = pass_error,
           verify_error = verify_error, email_error = email_error)
     else:
          return redirect("/welcome?username={0}".format(username))
            

@app.route("/welcome")
def welcome():
     username = request.args.get("username")
     return render_template("welcome.html", username = username)


app.run()
