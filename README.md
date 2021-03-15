# Hospital's Local Patients Calculation

# Description

This is a program that can record patient's location. One can understand on a given day or for a range of days, how many OP's are within a particular city and how many are from outside.
Based on this one can make a decision if it is feasible to open new branches outside of that particular place or open new Centers within that particular city itself.
This program is based on OOPs concept that can record the percentage of local patients and for testing purpose there is a file named test_LocalPatientsCalculation.py is created where pytest
framework is used. Hospital details are taken in a object form where two arguments are required that is Hospital's name and its place. After that desirable number of Patient objects can be created
by passing three arguments that is Patient's name, Patient's place and Registration date. These Patient objects should be passed as agruments in addPatients method of Hospital class. 
Thereafter a method named getLocalPatientPercentageforDates of Hospital Class should be called by passing start date and end date as its arguments and this method would give the accurate
percentage of local patients.


# Requirements

Python 3.7
pytest framework


# Installation

Download and Install Python version 3.7
https://www.python.org/downloads/release/python-378/

Install pytest using pip install pytest


# Step to run the testcases

Type the command pytest test_LocalPatientsCalculation.py to run the testcases.


 
