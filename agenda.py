from tkinter import W
import numpy as np
import pandas as pd
import datetime
import os
import fnmatch
import pickle

class Document(object):
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages
        self.docs = []

class Week(object):
    def __init__(self,week_nb):
        self.table = np.zeros([7,24])
        self.docs=[]
        self.week_nb = week_nb
        
    def addDocument(self,doc,hour,day,week):
        pages=doc.pages
        title=doc.title
        print(title,self.docs)
        if title in self.docs:
            doc_nb = self.docs.index(title)+1
        else :
            self.docs.append(title)
            doc_nb = len(self.docs)
        for d in range(0,5):
            for h in range(4,20):
                if (title == "BlipBloup"): print("BlipBloup SPOTTED ",self.week_nb,week)
                else: print("======"+str(title))
                if (((week == self.week_nb) and (d > day) and (h > hour)) or (week == self.week_nb)):
                     
                    if pages == 0 :
                        break
                    if self.table[d,h] == 0:
                        if pages > 3600 : 
                            pages = pages - 3600
                            self.table[d,h] = doc_nb
                        else :
                            pages = 0
                            self.table[d,h] = doc_nb
        print(self.week_nb,title,self.docs)
        return pages
        
class Calendar(object):
    def __init__(self,data_path):
        self.data_path = data_path
        
    def add_document(self,title,pages):
           
        doc = Document(title,pages)
        date = datetime.datetime.now()
        isocalendar = datetime.date(date.year, date.month, date.day).isocalendar()
        week_nb = isocalendar[1]
        day_nb = isocalendar[2]
        hour_nb = date.hour
        while doc.pages != 0:
            week_path = "week_"+str(week_nb)+".pkl"
            if os.path.exists(self.data_path+'/'+week_path):
                if (title =="BlipBloup") : print("EXISTS !!!!! "+str(week_nb),self.data_path+'/'+week_path)
                with open(self.data_path+'/'+week_path,'rb') as data:
                    week = pickle.load(data) 
            else :
                week = Week(week_nb)
            
            pages = week.addDocument(doc,hour_nb,day_nb,week_nb)
            self.save_week(week)   
            doc = Document(title,pages)
            week_nb +=1
            print(pages)
        return pages
        
        
    def save_week(self,week):
        file = "week_"+str(week.week_nb)+".pkl"
        with open(self.data_path+'/'+file,'wb') as file:
            pickle.dump(week,file,pickle.HIGHEST_PROTOCOL)

    def get_week(self,week):
        for file in sorted(os.listdir(self.data_path)):
            if fnmatch.fnmatch(file,'week_[0123456789][0123456789].pkl'):
                if (int(file[5:7]) == week):
                    print(week)
                    with open(self.data_path+'/'+file,'rb') as data:
                        week = pickle.load(data)
                    return week.table
        return 0

    def reset(self):
        for file in sorted(os.listdir(self.data_path)):
            if fnmatch.fnmatch(file,'week_[0123456789][0123456789].pkl'):
                os.remove(self.data_path+"/"+file)



cal = Calendar("calendar")
cal.reset()
cal.add_document("docX",45000)
cal.add_document("BlipBloup",12000)
cal.add_document("Yannick Hervé",1)
cal.add_document("BlipBloup",400000)
print(cal.get_week(42))
print(cal.get_week(43))
print(cal.get_week(44))




