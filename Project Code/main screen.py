from tkinter import *
import tkinter as tk
import torch
import torch.nn as nn
import torch.nn.functional as f
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


window=Tk()
# add widgets here
window.iconbitmap(r'C:\Users\Costas\Desktop\Pytorch\logo-modified.ico')  
window.title('Pocket Gym')
#window.aspect(1,1,1,1)
window.geometry("350x600+10+20")
window.configure(bg='white')

#placeholder class to show that it is not done


def not_working():
   text.config(text= "Not Working yet")


#class gia to neurwniko pou 8a paragei to auto program
class Model(nn.Module):
    def __init__(self, in_features=4, h1=25, h2=50, out_features=1): #in features = weight,height,age,gender out=exercise
        super().__init__()
        self.fc1 = nn.Linear(in_features, h1)  # input layer
        self.fc2 = nn.Linear(h1, h2)  # hidden layer
        self.out = nn.Linear(h2, out_features)  # output layer

    def forward(self, x):
        x = f.relu(self.fc1(x))
        x = f.relu(self.fc2(x))
        x = self.out(x)
        return x


#class tou user

class User:
  def __init__(self, username, password, email , user_id, user_type):

    self.username = username
    self.password = password
    self.email = email
    self.user_id = user_id
    self.user_type = user_type
  def error_check(self):
      pass
  def connect(self):
      pass
  def create_account(self):
      pass   
  def forgot_password(self):
      pass 
  def log_in(self):
      pass
  def log_out(self):
      pass
  def change_email(self):
      pass
  def view_profile(self):
      pass   
  def delete_account(self):
      pass 
  def contact_support(self):
      pass

  


#class Profile
class Profile(User):
   def __init__(self,username,password,email,user_id,user_type,name,surname,avatar,weight,age,gender,height):
      User.__init__(self,username, password, email , user_id, user_type)
      self.name=name 
      self.surname = surname
      self.avatar = avatar
      self.weight = weight
      self.age = age
      self.gender = gender 
      self.height = height

   def biometric_check(self):
      pass

   def upload_image(self):
      pass

   def spell_check(self):
      pass

   def completion_check(self):
      pass

   def change_weight(self):
      pass

   def change_height(self):
      pass

   def change_goals(self):
      pass

   def calculate_bmi(weight,height):
      BMI = weight / (height/100)**2
      return bmi

   def report(self):
      pass

#Class gia tis drasthriothtes xrhsth
class UserActivity(Profile,User):
   def __init__(self,username,password,email,user_id,user_type,name,surname,avatar,weight,age,gender,height,activity_id,duration,calories,difficulty,details):
      Profile.__init__(self,name,surname,avatar,weight,age,gender,height)

      self.activity_id = activity_id 
      self.duration =  duration 
      self.calories = calories 
      self.difficulty = difficulty
      self.details=details
   def track(self):
      pass
   def stop_track(self):
      pass
   def get_id(self):
      pass
   def return_id(self):
      pass
   def add_to_history(self):
      pass


#class gia to istoriko
class History():
   def __init__(self,achievements,completed_program,completed_activity):
      self.achievements = achievements
      self.completed_program = completed_program
      self.completed_activity = completed_activity
   def update(self):
      pass
   def delete_workout(self):
      pass
   def view_graph(self):
      pass
   def download_history(self):
      pass
   def share_achievements(self):
      pass
#class gia to autoprogram
class AutoProgram(Profile):
   def __init__(self,name,surname,avatar,weight,age,gender,height,program_id,duration,equipment,session_duration,calories,details,preferences):
      Profile.__init__(self,name,surname,avatar,weight,age,gender,height)
      self.program_id = program_id
      self.duration = duration 
      self.equipment = equipment 
      self.session_duration = session_duration
      self.calories = calories
      self.details = details
      self.preferences = preferences

   def create_exercise(self):
      dfx_dict ={'weight': weight , 'height': height , 'age': age , 'gender' :gender} 
      dfx = pd.DataFrame(dfx_dict, index=[0])
      X = torch.FloatTensor(dfx)
      model2= Model()
      model2.load_state_dict(torch.load('exercise.pt'));
      model2.eval()
      with torch.no_grad():
         z = model2(X)
      return z 

   def accept_program(self):
      pass

   def decline_program(self):
      pass

   def track(self):
      pass

   def add_to_user(self):
      pass

   def add_to_history(self):
      pass



      

#base user
class BaseUser(Profile,User):
   def __init__(self,username,password,email,user_id,user_type,name,surname,avatar,weight,age,gender,height):
      User.__init__(self,username, password, email , user_id, user_type)
      Profile.__init__(self,name,surname,avatar,weight,age,gender,height)
#premium
class PremiumUser(Profile,User):
   def __init__(self,username,password,email,user_id,user_type,name,surname,avatar,weight,age,gender,height,subscription,sub_start,sub_end,diet,personal_program):
      User.__init__(self,username, password, email , user_id, user_type)
      Profile.__init__(self,name,surname,avatar,weight,age,gender,height)
      self.subscription =  subscription 
      self.sub_start = sub_start 
      self.sub_end = sub_end
      self.diet = diet
      self.personal_program = personal_program
   def cancel_membership(self):
      pass
   def renew_membership(self):
      pass
   def premium_tour(self):
      pass

#sundromh
class Subscription():
   def __init__(self,price,duration,sub_id):
      self.price = price
      self.duration = duration
      self.sub_id= sub_id
   def buy(self):
      pass 
   def gift(self):
      pass 
   def refund(self):
      pass

#profile proswpikou(employee)
class PersonnelProfile(User):
   def __init__(self,username, password, email , user_id, user_type,personnel_id,name,surname,afm,amka,phone,payment_details,hire_date,salary):
      User.__init__(self,username, password, email , user_id, user_type)
      self.personnel_id = personnel_id
      self.name = name 
      self.surname = surname
      self.email = email
      self.afm = afm
      self.amka = amka
      self.phone = phone
      self.payment_details = payment_details
      self.hire_date = hire_date
      self.salary = salary

   def availability_check(self):
      pass

   def assign(self):
      pass

   def view_as_user(self):
      pass

   def contact_admin(self):
      pass

   def get_id(self):
      pass


   def get_type(self):
      pass


class Address:
    def __init__(self, street, city, state, zipcode, street2=''):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.state} {self.zipcode}')
        return '\n'.join(lines)

class PersonnelHistory():
   def __init__(self,achievements,completed_program,completed_activity):
      self.achievements = achievements
      self.completed_program = completed_program
      self.completed_activity = completed_activity


class Dietician(PersonnelProfile,User):
  
   def __init__(self,username, password, email , user_id, user_type,personnel_id,name,surname,afm,amka,phone,payment_details,hire_date,salary,dietician_id):
      User.__init__(self,username, password, email , user_id, user_type)
      PersonnelProfile.__init__(self,personnel_id,name,surname,email,afm,amka,phone,payment_details,hire_date,salary)
      self.dietician_id = dietician_id

   def delete_request(self, request_id):
      pass

   def create_program(self):
      pass

   def send_program(self):
      pass

class PersonalTrainer(PersonnelProfile,User):
   def __init__(self,username, password, email , user_id, user_type,personnel_id,name,surname,afm,amka,phone,payment_details,hire_date,salary,personal_trainer_id):
      User.__init__(self,username, password, email , user_id, user_type)
      PersonnelProfile.__init__(self,personnel_id,name,surname,email,afm,amka,phone,payment_details,hire_date,salary)
      self.personal_trainer_id = personal_trainer_id

   def delete_request(self, request_id):
      pass

   def create_program(self):
      pass

   def send_program(self):
      pass

   def edit_program(self):
      pass

class Blogger(PersonnelProfile,User):
   def __init__(self,username, password, email , user_id, user_type,personnel_id,name,surname,afm,amka,phone,payment_details,hire_date,salary,arthro_id):
      User.__init__(self,username, password, email , user_id, user_type)
      PersonnelProfile.__init__(self,personnel_id,name,surname,email,afm,amka,phone,payment_details,hire_date,salary)
      self.arthro_id = arthro_id

   def create_article(self):
      pass

   def delete_article(self):
      pass

class Moderator(PersonnelProfile,User):
   def __init__(self,username, password, email , user_id, user_type,personnel_id,name,surname,afm,amka,phone,payment_details,hire_date,salary,moderator_id):
      User.__init__(self,username, password, email , user_id, user_type)
      PersonnelProfile.__init__(self,personnel_id,name,surname,email,afm,amka,phone,payment_details,hire_date,salary)
      self.moderator_id = moderator_id
   def view_report(self,report_id):
      pass

   def inspect_report(self,report_id):
      pass

   def remove_content(self,content_id):
      pass

   def allow_content(self,content_id):
      pass

   def ban_user(self,user_id):
         pass   

class Diet():
   def __init__(self,diet,duration,request_id,personnel_id,user_id):
      self.diet=diet
      self.duration=duration
      self.request_id=request_id
      self.personnel_id=personnel_id
      self.user_id=user_id

   def get_requests():
      pass
   def get_request_id():
      pass
   def get_user_id():
      pass
   def show_details():
      pass
   def create_diet():
      pass
   def delete_request():
      pass
   def send_to(user_id,request_id):
      pass
   def send_request_delete_msg():
      pass
   def request_input():
      pass

   def create_program():
      pass

class Trainer_Program():
   def __init__(self,duration,program,request_id,personnel_id,user_id):
      self.duration=duration
      self.program=program
      self.request_id=request_id
      self.personnel_id=personnel_id
      self.user_id=user_id


class Blog:
    def __init__(self,title,publish_date,likes,comments,content,category,description,blog_id):
        self.title = title
        self.publish_date = publish_date
        self.likes = likes
        self.comments = comments
        self.category = category
        self.description = description
        self.blog_id = blog_id

  




#Import the image using PhotoImage function
aithmata= PhotoImage(file='buttons/aitimata.png')
drastiriothta=PhotoImage(file='buttons/drastiriotita.png')
news=PhotoImage(file='buttons/news.png')
profil=PhotoImage(file='buttons/profil.png')
istoriko=PhotoImage(file='buttons/istoriko.png')
logo= PhotoImage(file='logo-modified.png')
#Let us create a label for button event

frameA = tk.Frame(background="#ffffff")
frameB = tk.Frame(width=400, height = 600, background="#ffffff")
# Nested Frame. framebb is created within frameB without width or height
framebb = tk.Frame(frameB, background="#ffffff")


frameA.pack(side='top', fill=None)
frameB.pack(side='top')
# expand is the key parameter to center the framebb within frameB
framebb.pack(expand=True)


#frameA.pack_propagate(False)
frameB.pack_propagate(False)


#%% Buttons and Labels
tk.Label(frameA, image=logo).pack()
Button(window, image=aithmata,command= not_working,
borderwidth=0)

a = tk.Button(framebb, image=aithmata,command= not_working,
borderwidth=0).pack()
b = tk.Button(framebb, image=drastiriothta,command= not_working,
borderwidth=0).pack()
c = tk.Button(framebb, image=istoriko,command= not_working,
borderwidth=0).pack()
d=tk.Button(framebb, image=profil,command= not_working,
borderwidth=0).pack()
e=tk.Button(framebb, image=news,command= not_working,
borderwidth=0).pack()
f=tk.Button(framebb, image=aithmata,command= not_working,
borderwidth=0).pack()
text= Label(window, text= "")
text.pack()

tk.mainloop()
