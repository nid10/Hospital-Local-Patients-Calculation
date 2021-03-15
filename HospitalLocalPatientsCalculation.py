import datetime

class Hospital:
    def __init__(self,name,place):
        self.name = name.upper()
        self.place = place.upper()
        self.patients_list = []

    def addPatients(self, *patientObjects):
        for i in patientObjects:
            self.patients_list.append(i)

    def getLocalPatientPercentageforDates(self,startDate,endDate):
        year, month, day = map(int, startDate.split('-'))
        startDate = datetime.date(year, month, day)
        year, month, day = map(int, endDate.split('-'))
        endDate = datetime.date(year, month, day)
        filteredPatient = list(filter(lambda i:(self.place == i.place and i.registrationDate >=startDate and i.registrationDate<=endDate), self.patients_list))
        return ((len(filteredPatient)/len(self.patients_list))*100)

class Patient:
    def __init__(self,name,place,dateofRegistration):
        self.name = name.upper()
        self.place = place.upper()
        year, month, day = map(int, dateofRegistration.split('-'))
        registrationDate = datetime.date(year, month, day)
        self.registrationDate = registrationDate

