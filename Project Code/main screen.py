import torch
import torch.nn as nn
import torch.nn.functional as f
import numpy as np
import pandas as pd
import time



def not_working():
   text.config(text= "Not Working yet")

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

class User:
  def __init__(self, username, password, email , user_id, user_type):

    self.username = username
    self.password = password
    self.email = email
    self.user_id = user_id
    self.user_type = user_type
  def error_check():
      pass
  def connect():
      pass
  def create_account():
      pass   
  def forgot_password():
      pass 
  def log_in():
      pass
  def log_out():
      pass
  def change_email():
      pass
  def view_profile():
      pass   
  def delete_account():
      pass 
  def contact_support():
      pass

  def discount_wait():
      pass



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

   def biometric_check():
      pass

   def upload_image():
      pass

   def spell_check():
      pass

   def completion_check():
      pass

   def change_weight():
      pass

   def change_height():
      pass

   def change_goals():
      pass

   def calculate_bmi(weight,height):
      BMI = weight / (height/100)**2
      return bmi

   def report():
      pass


class UserActivity():
   def __init__(self,id,duration,calories,type1,difficulty):
      self.id = id 
      self.duration =  duration 
      self.calories = calories 
      self.type1 = type1
      self.difficulty = difficulty
   def track():
      pass
   def stop_track():
      pass
   def get_id():
      pass
   def return_id():
      pass
   def add_to_history():
      pass

class History():
   def __init__(self,achievements,completedprogram,completedactivity):
      self.achievements = achievements
      self.completedprogram = completedprogram
      self.completedactivity = completedactivity
   def update():
      pass
   def delete_workout():
      pass
   def view_graph():
      pass
   def download_history():
      pass
   def share_achievements():
      pass

class AutoProgram(Profile):
   def __init__(self,name,surname,avatar,weight,age,gender,height,autoprogramid,trainduration,equipment,activityduration,calories):
      Profile.__init__(self,name,surname,avatar,weight,age,gender,height)
      self.autoprogramid = autoprogramid
      self.trainduration = trainduration 
      self.equipment = equipment 
      self.activityduration = activityduration
      self.calories = calories

   def create_exercise():
      dfx_dict ={'weight': weight , 'height': height , 'age': age , 'gender' :gender} 
      dfx = pd.DataFrame(dfx_dict, index=[0])
      X = torch.FloatTensor(dfx)
      model2= Model()
      model2.load_state_dict(torch.load('exercise.pt'));
      model2.eval()
      with torch.no_grad():
         z = model2(X)
      return z 

   def add_to_user():
      pass

   def add_to_history():
      pass



      


class BaseUser(Profile,User):
   def __init__(self,username,password,email,user_id,user_type,name,surname,avatar,weight,age,gender,height):
      User.__init__(self,username, password, email , user_id, user_type)
      Profile.__init__(self,name,surname,avatar,weight,age,gender,height)

class PremiumUser(Profile,User):
   def __init__(self,username,password,email,user_id,user_type,name,surname,avatar,weight,age,gender,height,subscription,buydate,enddate,diet,trainningprogram):
      User.__init__(self,username, password, email , user_id, user_type)
      Profile.__init__(self,name,surname,avatar,weight,age,gender,height)
      self.subscription =  subscription 
      self.buydate = buydate 
      self.enddate = enddate
      self.diet = diet
      self.trainningprogram = trainningprogram
   def cancel_membership():
      pass
   def renew_membership():
      pass
   def premium_tour():
      pass


class Subscription():
   def __init__(self,price,duration):
      self.price = price
      self.duration = duration
   def buy():
      pass 
   def gift():
      pass 
   def refund():
      pass


class PersonnelProfile(User):
   def __init__(self,username, password, email , user_id, user_type,personnel_id,profiletype,name,surname,afm,amka,phone,address,payment_details,hire_date,salary):
      User.__init__(self,username, password, email , user_id, user_type)
      self.personnel_id = personnel_id
      self.profiletype = profiletype
      self.name = name 
      self.surname = surname
      self.email = email
      self.afm = afm
      self.amka = amka
      self.phone = phone
      self.address = address
      self.payment_details = payment_details
      self.hire_date = hire_date
      self.salary = salary

   def availability_check():
      pass

   def assign():
      pass

   def view_as_user():
      pass

   def contact_admin():
      pass

   def get_id():
      pass


   def get_type():
      pass



class PersonnelHistory():
   def __init__(self,achievements,completedprogram,completedactivity):
      self.achievements = achievements
      self.completedprogram = completedprogram
      self.completedactivity = completedactivity


class Dietician(PersonnelProfile):
   def __init__(self, username, password, email , user_id, user_type,personnel_id,profiletype,name,surname,afm,amka,phone,address,payment_details,hire_date,salary, dietician_id):
      User.__init__(self,username, password, email , user_id, user_type)
      PersonnelProfile.__init__(self,personnel_id,profiletype,name,surname,afm,amka,phone,address,payment_details,hire_date,salary)
      self.dietician_id=dietician_id


   def delete_request(request_id):
      pass

   def create_program():
      pass

   def send_program():
      pass


class DietPlan():
    def __init__(self,diet_plan,duration,request_id,personnel_id,user_id):
        self.diet_plan = diet_plan
        self.duration = duration
        self.request_id = request_id 
        self.user_id = user_id
        self.personnel_id =  personnel_id
    
    def show_details(request_id):
        pass
    
    def create_diet():
        pass
    
    def send_to(user_id):
        pass
    
    def send_request_delete_msg(user_id):
        pass
    
    def request_input():
        pass
    
    def edit_program():
        pass
    
    
class Trainer(PersonnelProfile):
   def __init__(self,personnel_id,profiletype,name,surname,afm,amka,phone,address,payment_details,hire_date,salary,personal_trainer_id):
      User.__init__(self,username, password, email , user_id, user_type)
      PersonnelProfile.__init__(self,personnel_id,profiletype,name,surname,afm,amka,phone,address,payment_details,hire_date,salary)
      self.personal_trainer_id = personal_trainer_id
   def delete_request(request_id):
      pass
   def create_program():
      pass
   def send_program(user_id):
      pass
   def edit_program():
      pass

class PersonalProgram():
   def __init___(self,duration,personal_program,request_id,personnel_id,user_id):
      self.duration = duration 
      self.personal_program = personal_program
      self.request_id = request_id
      self.personnel_id = personnel_id
      self.user_id = user_id

   def get_user_id():
      pass
   
   def show_details(request_id):
      pass 
   def create_activity():
      pass      
   def delete_request(request_id):
      pass
   def send_to(user_id):
      pass
   def send_request_delete_msg(user_id):
      pass
   def request_input():
      pass 
   def create_program():
      pass 

class Request():
   def __init__(self,request_id,request_type,content):
      self.request_id = request_id 
      self.request_type = request_type 
      self.content = content

   def get_sub_status():
      pass

   def submit():
      pass
   def send_accept_msg_to():
      pass

   def send_decline_msg_to():
      pass

   def data_check():
      pass

class DieticianRequest(Request):
   def __init__(self,request_id,request_type,content,user_id,request_date,biometrics,preferences):
      Request.__init__(self,request_id,request_type,content)
      self.user_id = user_id
      self.request_date = request_date
      self.biometrics = biometrics
      self.preferences = preferences

   def get_biometrics():
      pass
   def show_summary():
      pass
   def create_request():
      pass
   def add_to_requests():
      pass
   def get_biometric_stats():
      pass
   def info_check():
      pass
   def create_biometrics():
      pass
   def request_input():
      pass

class PersTrainRequest(Request):
   def __init__(self,request_id,request_type,content,user_id,request_date,biometrics,preferences):
      Request.__init__(self,request_id,request_type,content)
      self.user_id = user_id
      self.request_date = request_date
      self.biometrics = biometrics
      self.preferences = preferences

   def get_biometrics():
      pass
   def show_summary():
      pass
   def create_request():
      pass
   def add_to_requests():
      pass
   def get_biometric_stats():
      pass
   def info_check():
      pass
   def create_biometrics():
      pass
   def request_input():
      pass

class LiveCallRequest(Request):
   def __init__(self,request_id,request_type,content,user_id,availability,personnel_id):
      Request.__init__(self,request_id,request_type,content)
      self.user_id = user_id
      self.availability = availability
      self.personnel_id = personnel_id

   def show_summary(request_id):
      pass

   def create_request():
      pass

   def add_to_requests():
      pass

   def request_input():
      pass

   def get_availability():
      pass
   def assign_to(personnel_id):
      pass





class Blogger(PersonnelProfile):
   def __init__(self,personnel_id,profiletype,name,surname,afm,amka,phone,address,payment_details,hire_date,salary,blogger_id):
      User.__init__(self,username, password, email , user_id, user_type)
      PersonnelProfile.__init__(self,personnel_id,profiletype,name,surname,afm,amka,phone,address,payment_details,hire_date,salary)
      self.blogger_id = blogger_id
   def create_article():
      pass
   def delete_article(article_id):
      pass
   def edit_article(article_id):
      pass

class Article():
   def __init__(self, title, publish_date, likes, comments, content, category, description, article_id):
      self.title = title 
      self.publish_date = publish_date
      self.likes = likes
      self.comments = comments
      self.content = content
      self.category = category
      self.description = description
      self.article_id = article_id

   def create_article():
      pass
   def error_check():
      pass
   def publish():
      pass
   def error_highlight():
      pass
   def edit_article():
      pass
      
class Moderator():
   def __init__(self,personnel_id,profiletype,name,surname,afm,amka,phone,address,payment_details,hire_date,salary,moderator_id):
      User.__init__(self,username, password, email , user_id, user_type)
      PersonnelProfile.__init__(self,personnel_id,profiletype,name,surname,afm,amka,phone,address,payment_details,hire_date,salary)
      self.moderator_id = moderator_id
   def view_report(report_id):
      pass
   def inspect_report(report_id):
      pass
   def remove():
      pass
   def allow():
      pass
   def ban(user_id):
      pass

class Reports():
   def __init__(self,report_id,post_id,date,message_id,content,comments,api_type,api_results):
      self.report_id = report_id
      self.post_id = post_id
      self.date = date
      self.message_id = message_id
      self.content = content
      self.comments = comments
      self.api_type = api_type
      self.api_results = call_api()

   def api_call():
      pass
   def content_check():
      pass
   def judge(api_results):
      pass
   def delete_content(post_id,message_id):
      pass
   def move_for_approval(report_id):
      pass
   def show_details(report_id):
      pass
   def get_report_content():
      pass
   def get_content():
      pass
   def send_to():
      pass
   def delete_report(report_id):
      pass
   def input_duration():
      pass
   def ban(user_id):
      pass



class Message():
   def __init__(self,conv_id,content,sender_id,recipient_id,message_date,friendlist):
      self.conv_id = conv_id
      self.content = content
      self.sender_id = sender_id
      self.recipient_id = recipient_id
      self.message_date = message_date
      self.friendlist = friendlist
   def message_send(recipient_id):
      pass
   def send_to(recipient_id):
      pass
   def create_message():
      pass
   def edit_message():
      pass
   def delete_message():
      pass
   def report():
      pass
   def forward_message():
      pass
   def create_conversation(recipient_id):
      pass
   def open_conversation(conversation_id):
      pass

   def show_friendlist():
      pass

   def close_friendlist():
      pass

class Post():
   def __init__(self,content,comments,likes,post_id,post_title,date,user_id):
      self.content = content
      self.comments = comments
      self.likes = likes
      self.post_id = post_id 
      self.post_title = post_title
      self.date = date 
      self.user_id = user_id 

   def invitation():
      pass
   def edit_post(post_id):
      pass
   def like(post_id):
      pass
   def comment(post_id):
      pass
   def delete(post_id):
      pass
   def pin(post_id):
      pass
   def report(post_id):
      pass
   def publish():
      pass

class Share():
   def __init__(self,share_id,share_name,share_description,share_type,share_post_id):
      self.share_id = share_id
      self.share_name = share_name
      self.share_description = share_description
      self.share_type = share_type
      self.share_post_id = share_post_id

   def add_share():
      pass
   def edit_share():
      pass
   def delete_share():
      pass



class UserFeed():
   def __init__(self,user_id,post_id):
      self.user_id = user_id 
      self.post_id = post_id 
   def refresh():
      pass
   def view():
      pass


class Communities():
   def __init__(self,community_id,group_list):
      self.community_id = community_id
      self.group_list = group_list


class Friends():
   def __init__(self,friend_id,friend_name,friend_username):
      self.friend_id = friend_id
      self.friend_name = friend_name 
      self.friend_username = friend_username

   def add_friend(user_id):
      pass

   def edit_friends():
      pass

   def delete_friends():
      pass

   def search_friends():
      pass

class NewsBlog():
   def __init__(self):
      pass 
   def like():
      pass
   def comment():
      pass
   def delete():
      pass
   def pin():
      pass
   def report():
      pass


