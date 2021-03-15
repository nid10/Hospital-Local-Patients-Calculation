import pytest
from HospitalLocalPatientsCalculation import *

def test_LocalPatientsPercentageTest1():
    ChinmayaHospital = Hospital("Chinmaya", "Bangalore")

    Priyanka = Patient('Priyanka', 'bangalore', '2021-03-12')
    Priya = Patient('Priya', 'bangalore', '2021-03-11')
    Vijayalaxmi = Patient('Vijayalaxmi', 'jaipur', '2021-03-10')
    Nikita = Patient('Nikita', 'bangalore', '2021-03-09')

    ChinmayaHospital.addPatients(Priyanka, Priya, Vijayalaxmi, Nikita)

    actualPercentage = ChinmayaHospital.getLocalPatientPercentageforDates("2021-03-11", "2021-03-12")
    expectedPercentage = 50.0
    assert actualPercentage == expectedPercentage


def test_LocalPatientsPercentageTest2():
    ApolloHospital = Hospital("Apollo", "Bangalore")

    Pooja = Patient('Pooja', 'bangalore', '2021-03-08')
    Nishi = Patient('Nishi', 'bangalore', '2021-03-08')
    Vaishali = Patient('Vaishali', 'bangalore', '2021-03-06')
    Supriya = Patient('Supriya', 'bangalore', '2021-03-05')

    ApolloHospital.addPatients(Pooja, Nishi, Vaishali, Supriya)

    actualPercentage = ApolloHospital.getLocalPatientPercentageforDates("2021-03-06", "2021-03-08")
    expectedPercentage = 75.0
    assert actualPercentage == expectedPercentage


def test_LocalPatientsPercentageTest3():
    FortisHospital = Hospital("Fortis", "Bangalore")

    Khushi = Patient('Khushi', 'Chandigarh', '2021-03-08')
    Prachi = Patient('Prachi', 'mumbai', '2021-03-08')
    Nimisha = Patient('Nimisha', 'jaipur', '2021-03-06')
    Anjali = Patient('Anjali', 'Chandigarh', '2021-03-05')

    FortisHospital.addPatients(Khushi,Prachi,Nimisha,Anjali)

    actualPercentage = FortisHospital.getLocalPatientPercentageforDates("2021-03-06","2021-03-08")
    expectedPercentage = 0.0
    assert actualPercentage == expectedPercentage