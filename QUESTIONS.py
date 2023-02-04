from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import re

# Check whether email is valid or not
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

# Check whether phone number is valid or not
Pattern = re.compile("(0/91)?[6-9][0-9]{9}")


def check_form(data):
    # Validating name
    if data['name'].isdigit():
        return ('name', 'Invalid name!')

    # Validating age
    if data['age'] <= 0:
        return ('age', 'Invalid age!')

    # Checking mail
    if not (re.search(regex, data['email'])):
        return ('email', 'Invalid email!')

    # Checking Phone Number
    if not (Pattern.match(str(data['phone']))) or len(str(data['phone'])) != 10:
        return ('phone', 'Invalid phone!')

    # Validating passwords
    if data['pass'] != data['passes']:
        return ('passes', "Please make sure your passwords match")


# Taking input from the user
data = input_group("Fill out the form:", [
    input('Name', name='name', type=TEXT, required=True,
          PlaceHolder="name"),
    input('Password', name='pass', type=PASSWORD,
          required=True, PlaceHolder="Password"),

    input('Confirm Password', name='passes', type=PASSWORD,
          required=True, PlaceHolder="Confirm Password"),



    input('Phone', name='phone', type=NUMBER,
          required=True, PlaceHolder="12345"),

    input('Email', name='email', type=TEXT,
          required=True, PlaceHolder="user@gmail.com"),

    input('Age', name='age', type=NUMBER, required=True,
          PlaceHolder="age"),

], validate=check_form, cancelable=True)

# Create a radio button
gender = radio("Gender", options=['Male', 'Female'], required=True)

# Create a skills markdown
skills = select("Tech Stack", options=[
    'Machine learning', 'Python', 'tensorflow'],
                required=True)

# Display output using popup
popup("Your Details",
      f"Name: {data['name']}\
	\nPhone: {str(data['phone'])}\nEmail: {data['email']}\
	\nAge: {str(data['age'])}\n\
	\nGender: {gender}\nSkill: {skills}\n",
      closable=True)
score = 0
if skills == 'Python':

    q1 = radio("1. Who developed Python Programming Language?",
               ["Wick van Rossum", "Rasmus Lerdorf", "Guido van Rossum", "Niene stom"])
    if q1 == "Guido van Rossum":
        score += 1
    q2 = radio("2. Which type of Programming does Python support?",
               ["object-oriented programming", "strucured programming", "functional programming",
                "all of the mentioned"])
    if q2 == "all of the mentioned":
        score += 1
    q3 = radio("3. Is Python case sensitive when dealing with identifiers?",
               ["no", "yes", "machine dependent", "None of the mentioned"])
    if q3 == "yes":
        score += 1
    q4 = radio("4. Which of the following is the correct extension of the Python file?",
               [".python", ".pl", ".py", ".p"])
    if q4 == "Guido van Rossum":
        score += 1
    q5 = radio("5. What are the advantages of arrays?",
               ["Objects of mixed data types can be stored",
                " Elements in an array cannot be sorted",
                " Index of first element of an array is 1",
                " Easier to store elements of same data type"])
    if q5 == "Easier to store elements of same data type":
        score += 1
    q6 = radio("6. Is Python code compiled or interpreted?",
               ["Python code is both compiled and interpreted", "Python code is neither compiled nor interpreted",
                "Python code is only compiled", " Python code is only interpreted"])
    if q6 == "Python code is both compiled and interpreted":
        score += 1
if skills == 'tensorflow':

    q1 = radio("1.How many types of Tensors are there?",
               ["2", "3", "4", "5"])
    if q1 == "3":
        score += 1
    q2 = radio("2. Which of the following are main advantages of TensorFlow?",
               ["It is easily customizable and open-source", " It has platform flexibility",
                "It has auto differentiation capabilities",
                "all of the mentioned"])
    if q2 == "all of the mentioned":
        score += 1
    q3 = radio("3.TensorFlow architecture works in ________ parts?",
               ["2", "3", "4", "5"])
    if q3 == "3":
        score += 1
    q4 = radio(
        "4. __________ provides a high-level API which makes neural network building and training fast and easy?",
        ["TensorLayer", "Sonnet", "PrettyTensor", "TFLearn"])
    if q4 == "TFLearn":
        score += 1
    q5 = radio("5. Variables in TensorFlow are also known as?",
               ["tensor keywords",
                " tensor attributes",
                " tensor objects",
                " tensor variables"])
    if q5 == "tensor objects":
        score += 1
    q6 = radio("6.  Which of the following defines specific input data that does not change with time?",
               ["tf.variable", "tf.placeholder",
                "Both A and B", " None of the above"])
    if q6 == "tf.placeholder":
        score += 1
if skills == "Machine learning":
    q1 = radio("1.Which of the following are not types of Machine learning algorithms?",
               ["Supervised", "Unsupervised", "Reinforcement", "Human Learning"])
    if q1 == "Human Learning":
        score += 1
    q2 = radio("2. Which of the following are types of Supervised algorithms?",
               ["SVM", "Naive Bayes", "ID3",
                "all of the mentioned"])
    if q2 == "all of the mentioned":
        score += 1
    q3 = radio("3.Examples of unsupervised learning algorithms?",
               ["Recommender Systems", "anomaly detection", "latent variable methods", "all of the mentioned"])
    if q3 == "all of the mentioned":
        score += 1
    q4 = radio(
        "4. The term machine learning was coined in which year?",
        ["1958", "1959", "1960", "1961"])
    if q4 == "1959":
        score += 1
    q5 = radio("Machine learning approaches can be traditionally categorized into ______ categories",
               ["3",
                "4",
                "7",
                "9"])
    if q5 == "3":
        score += 1
    q6 = radio("6.-----is the machine learning algorithms that can be used with labeled data",
               ["Regression algorithms", "Clustering algorithms",
                "Association algorithms", " All of the above"])
    if q6 == "Regression algorithms":
        score += 1
if score >= 2:
    put_text("Passed")
else:
    put_text("Failed")
put_text(" your score is " + str(score))
style(put_text("Thankyou for participation"), 'color:red')
