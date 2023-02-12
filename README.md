
# Creating an Interactive Quiz with PyWebIO

This Project is a form validation and quiz application that utilizes the PyWebIO library. The user is asked to fill out a form that includes fields for name, password, phone, email, age, and gender. The form data is then validated using a regular expression and phone number pattern to ensure that the input is valid. After filling out the form, the user is asked to select a skill (Machine learning, Python, or TensorFlow) and then complete a corresponding quiz. The quiz results are displayed in a popup along with the user's form information, including the selected gender and skill.

## Table of Contents
* [Introduction](#introduction)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Documentation](#documentation)

# Introduction
Building a quiz web app with PyWebIO becomes a breeze as it requires significantly less code compared to traditional HTML, CSS, and JavaScript, making it a more efficient and streamlined way to accomplish the task.Additionally, PyWebIO is highly customizable, allowing developers to modify the look and feel of their applications to match their needs.

## Technologies Used

Python and PyWebIO are the main technologies used in building this project.

**Python** Python is the main programming language used in this project. The use of the regex module from Python helps in building a form with validation, making the process of user registration smoother and more secure.

**PyWebIO** is used for user input and output handling, which makes the process of creating engaging quizzes easier and more efficient.


## Features

- Easy to Use
- Interactive and real-time experience
- Form registration and input validation
- Support for multiple choice questions
- Quiz Results
- Dynamic Question Generation


## Setup

Install my-project with cmd

Stable version:

```bash
pip3 install -U pywebio
```

Development version:

```bash
pip3 install -U https://github.com/pywebio/PyWebIO/archive/dev-release.zip
```
## Usage
The basic usage of this project is divided into three steps.

#### Create a Skills Markdown
To create a skills markdown, you can use the select function from the PyWebIO library. The code would look like this:
```
skills = select("Select Your Skills", options=[
    'Machine Learning', 'Python', 'TensorFlow'],
                required=True)

```
#### Create Multiple Choice Questions Based on Skills
Based on the selected skill, you can create multiple choice questions using the **radio** function from PyWebIO. For example, if the selected skill is **TensorFlow**, the code would look like this:

```
score = 0
if skills == 'TensorFlow':
    q1 = radio("1. How many types of Tensors are there?",
               ["2", "3", "4", "5"])
    if q1 == "3":
        score += 1

```
#### Creating Multiple Choices with Different Markdowns
You can create multiple choice questions for different skills by adding similar code blocks for each skill. You can also add different markdowns and formatting to make the quiz engaging and interactive.

## Documentation

[Documentation](https://pywebio.readthedocs.io/en/latest/)

