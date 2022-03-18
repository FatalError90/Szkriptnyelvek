# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:30:51 2020

@author: masina
"""
from icalendar import Calendar, Event
import re
import vobject
import pandas as pd
import matplotlib.pyplot as plt


# ----------------listák---------------------------------------------------
presentation=list()
begin=list()
end=list()
description=list()
indico_id=list()
name=list()
institute=list()

# ----------------diagram listák--------------------------------------------
countMember=list()
presentationLength=list()
period=0

#-----------------event2007 beolvasása és feldolgozasa---------------------
eventText = open('event2007.txt','rb')
eventCal = Calendar.from_ical(eventText.read())

#--leírás, előadás, kezdő és végdátum kiolvasása, előadások hossza--------
for elements in eventCal.walk():
    if elements.name == "VEVENT":
        description.append((elements.get('DESCRIPTION')))
        presentation.append((elements.get('summary')))
        begin.append((elements.get('dtstart').dt))
        end.append((elements.get('DTEND').dt))  
        period+=(elements.get('DTEND').dt-elements.get('dtstart').dt).total_seconds()
        
eventText.close()

#-------------- indico id név és intézmény kiolvasása---------------------- 
eventText = open("event2007.txt").read()
    
for elements in vobject.readComponents(eventText):
    for component in elements.components():
        search = re.match(r'Speakers:([^(]*)\((.*?)\)$', component.description.valueRepr().split('\n')[0])
        if search is None: 
            continue
        else:
            name.append(search[1].strip())
            institute.append(search[2].strip())

for component in description:
    indico_id.append(component.split('/')[-2])

#-------------- dataframe kialakítása--------------------------------------
df1=pd.DataFrame(list(zip(name, institute, presentation,begin,end,indico_id)), 
                columns =['Name', 'Intézet','Előadás címe','Előadás kezdete','Előadás vége','Indico azonosító' ])
 
#---------dátumokról a timzonok levétele, egyébként ValueError ------------
df1['Előadás kezdete'] = df1['Előadás kezdete'].dt.tz_localize(None)
df1['Előadás vége'] = df1['Előadás vége'].dt.tz_localize(None)

#---------------------Résztvevők számának meghatározása--------------------
countMember.append(len(name))

#---------------------Előadások hosszának meghatározása--------------------
presentationLength.append(period/60)

#--------------------------Listák nullázása--------------------------------
presentation.clear()
begin.clear()
end.clear()
description.clear()
indico_id.clear()
name.clear()
institute.clear()
period=0

#-----------------event2008 beolvasása és feldolgozasa---------------------
eventText = open('event2008.txt','rb')
eventCal = Calendar.from_ical(eventText.read())

#------leírás, előadás, kezdő és végdátum kiolvasása, előadások hossza-----
for elements in eventCal.walk():
    if elements.name == "VEVENT":
        description.append((elements.get('DESCRIPTION')))
        presentation.append((elements.get('summary')))
        begin.append((elements.get('dtstart').dt))
        end.append((elements.get('DTEND').dt))     
        period+=(elements.get('DTEND').dt-elements.get('dtstart').dt).total_seconds()

eventText.close()

#-------------- indico id név és intézmény kiolvasása---------------------- 
eventText = open("event2008.txt").read()
    
for elements in vobject.readComponents(eventText):
    for component in elements.components():
        search = re.match(r'Speakers:([^(]*)\((.*?)\)$', component.description.valueRepr().split('\n')[0])
        if search is None: 
            continue
        else:
            name.append(search[1].strip())
            institute.append(search[2].strip())

for component in description:
    indico_id.append(component.split('/')[-2])

#-------------- dataframe kialakítása--------------------------------------
df2=pd.DataFrame(list(zip(name, institute, presentation,begin,end,indico_id)), 
                columns =['Name', 'Intézet','Előadás címe','Előadás kezdete','Előadás vége','Indico azonosító' ])
 
#---------dátumokról a timzonok levétele, egyébként ValueError ------------
df2['Előadás kezdete'] = df2['Előadás kezdete'].dt.tz_localize(None)
df2['Előadás vége'] = df2['Előadás vége'].dt.tz_localize(None)

#---------------------Résztvevők számának meghatározása--------------------
countMember.append(len(name))

#---------------------Előadások hosszának meghatározása--------------------
presentationLength.append(period/60)

#--------------------------Listák nullázása--------------------------------
presentation.clear()
begin.clear()
end.clear()
description.clear()
indico_id.clear()
name.clear()
institute.clear()
period=0

#-----------------event2009 beolvasása és feldolgozasa---------------------
eventText = open('event2009.txt','rb')
eventCal = Calendar.from_ical(eventText.read())

#------leírás, előadás, kezdő és végdátum kiolvasása, előadások hossza-----
for elements in eventCal.walk():
    if elements.name == "VEVENT":
        description.append((elements.get('DESCRIPTION')))
        presentation.append((elements.get('summary')))
        begin.append((elements.get('dtstart').dt))
        end.append((elements.get('DTEND').dt))
        period+=(elements.get('DTEND').dt-elements.get('dtstart').dt).total_seconds()

eventText.close()

#-------------- indico id név és intézmény kiolvasása---------------------- 
eventText = open("event2009.txt").read()
    
for elements in vobject.readComponents(eventText):
    for component in elements.components():
        search = re.match(r'Speakers:([^(]*)\((.*?)\)$', component.description.valueRepr().split('\n')[0])
        if search is None: 
            continue
        else:
            name.append(search[1].strip())
            institute.append(search[2].strip())

for component in description:
    indico_id.append(component.split('/')[-2])

#-------------- dataframe kialakítása--------------------------------------
df3=pd.DataFrame(list(zip(name, institute, presentation,begin,end,indico_id)), 
                columns =['Name', 'Intézet','Előadás címe','Előadás kezdete','Előadás vége','Indico azonosító' ])
 
#---------dátumokról a timzonok levétele, egyébként ValueError ------------
df3['Előadás kezdete'] = df3['Előadás kezdete'].dt.tz_localize(None)
df3['Előadás vége'] = df3['Előadás vége'].dt.tz_localize(None)

#---------------------Résztvevők számának meghatározása--------------------
countMember.append(len(name))

#---------------------Előadások hosszának meghatározása--------------------
presentationLength.append(period/60)

#--------------------------Listák nullázása--------------------------------
presentation.clear()
begin.clear()
end.clear()
description.clear()
indico_id.clear()
name.clear()
institute.clear()
period=0

#-----------------event2010 beolvasása és feldolgozasa---------------------
eventText = open('event2010.txt','rb')
eventCal = Calendar.from_ical(eventText.read())

#------leírás, előadás, kezdő és végdátum kiolvasása, előadások hossza-----
for elements in eventCal.walk():
    if elements.name == "VEVENT":
        description.append((elements.get('DESCRIPTION')))
        presentation.append((elements.get('summary')))
        begin.append((elements.get('dtstart').dt))
        end.append((elements.get('DTEND').dt))   
        period+=(elements.get('DTEND').dt-elements.get('dtstart').dt).total_seconds()

eventText.close()

#-------------- indico id név és intézmény kiolvasása---------------------- 
eventText = open("event2010.txt").read()
    
for elements in vobject.readComponents(eventText):
    for component in elements.components():
        search = re.match(r'Speakers:([^(]*)\((.*?)\)$', component.description.valueRepr().split('\n')[0])
        if search is None: 
            continue
        else:
            name.append(search[1].strip())
            institute.append(search[2].strip())

for component in description:
    indico_id.append(component.split('/')[-2])

#-------------- dataframe kialakítása--------------------------------------
df4=pd.DataFrame(list(zip(name, institute, presentation,begin,end,indico_id)), 
                columns =['Name', 'Intézet','Előadás címe','Előadás kezdete','Előadás vége','Indico azonosító' ])
 
#---------dátumokról a timzonok levétele, egyébként ValueError ------------
df4['Előadás kezdete'] = df4['Előadás kezdete'].dt.tz_localize(None)
df4['Előadás vége'] = df4['Előadás vége'].dt.tz_localize(None)

#---------------------Résztvevők számának meghatározása--------------------
countMember.append(len(name))

#---------------------Előadások hosszának meghatározása--------------------
presentationLength.append(period/60)

#--------------------------Listák nullázása--------------------------------
presentation.clear()
begin.clear()
end.clear()
description.clear()
indico_id.clear()
name.clear()
institute.clear()
period=0

#-----------------event2011 beolvasása és feldolgozasa---------------------
eventText = open('event2011.txt','rb')
eventCal = Calendar.from_ical(eventText.read())

#------leírás, előadás, kezdő és végdátum kiolvasása, előadások hossza-----
for elements in eventCal.walk():
    if elements.name == "VEVENT":
        description.append((elements.get('DESCRIPTION')))
        presentation.append((elements.get('summary')))
        begin.append((elements.get('dtstart').dt))
        end.append((elements.get('DTEND').dt))
        period+=(elements.get('DTEND').dt-elements.get('dtstart').dt).total_seconds()

eventText.close()

#-------------- indico id név és intézmény kiolvasása---------------------- 
eventText = open("event2011.txt").read()
    
for elements in vobject.readComponents(eventText):
    for component in elements.components():
        search = re.match(r'Speakers:([^(]*)\((.*?)\)$', component.description.valueRepr().split('\n')[0])
        if search is None: 
            continue
        else:
            name.append(search[1].strip())
            institute.append(search[2].strip())

for component in description:
    indico_id.append(component.split('/')[-2])

#-------------- dataframe kialakítása--------------------------------------
df5=pd.DataFrame(list(zip(name, institute, presentation,begin,end,indico_id)), 
                columns =['Name', 'Intézet','Előadás címe','Előadás kezdete','Előadás vége','Indico azonosító' ])
 
#---------dátumokról a timzonok levétele, egyébként ValueError ------------
df5['Előadás kezdete'] = df5['Előadás kezdete'].dt.tz_localize(None)
df5['Előadás vége'] = df5['Előadás vége'].dt.tz_localize(None)

#---------------------Résztvevők számának meghatározása--------------------
countMember.append(len(name))

#---------------------Előadások hosszának meghatározása--------------------
presentationLength.append(period/60)

#--------------------------Listák nullázása--------------------------------
presentation.clear()
begin.clear()
end.clear()
description.clear()
indico_id.clear()
name.clear()
institute.clear()

#-----------------event2012 beolvasása és feldolgozasa---------------------
eventText = open('event2012.txt','rb')
eventCal = Calendar.from_ical(eventText.read())

#------leírás, előadás, kezdő és végdátum kiolvasása, előadások hossza-----
for elements in eventCal.walk():
    if elements.name == "VEVENT":
        description.append((elements.get('DESCRIPTION')))
        presentation.append((elements.get('summary')))
        begin.append((elements.get('dtstart').dt))
        end.append((elements.get('DTEND').dt)) 
        period+=(elements.get('DTEND').dt-elements.get('dtstart').dt).total_seconds()

eventText.close()

#-------------- indico id név és intézmény kiolvasása---------------------- 
eventText = open("event2012.txt").read()
    
for elements in vobject.readComponents(eventText):
    for component in elements.components():
        search = re.match(r'Speakers:([^(]*)\((.*?)\)$', component.description.valueRepr().split('\n')[0])
        if search is None: 
            continue
        else:
            name.append(search[1].strip())
            institute.append(search[2].strip())

for component in description:
    indico_id.append(component.split('/')[-2])

#-------------- dataframe kialakítása--------------------------------------
df6=pd.DataFrame(list(zip(name, institute, presentation,begin,end,indico_id)), 
                columns =['Name', 'Intézet','Előadás címe','Előadás kezdete','Előadás vége','Indico azonosító' ])
 
#---------dátumokról a timzonok levétele, egyébként ValueError ------------
df6['Előadás kezdete'] = df6['Előadás kezdete'].dt.tz_localize(None)
df6['Előadás vége'] = df6['Előadás vége'].dt.tz_localize(None)

#---------------------Résztvevők számának meghatározása--------------------
countMember.append(len(name))

#---------------------Előadások hosszának meghatározása--------------------
presentationLength.append(period/60)

#--------------------------Listák nullázása--------------------------------
presentation.clear()
begin.clear()
end.clear()
description.clear()
indico_id.clear()
name.clear()
institute.clear()
period=0

#-----------------event2020 beolvasása és feldolgozasa---------------------
eventText = open('event2020.txt','rb')
eventCal = Calendar.from_ical(eventText.read())

#------leírás, előadás, kezdő és végdátum kiolvasása, előadások hossza-----
for elements in eventCal.walk():
    if elements.name == "VEVENT":
        description.append((elements.get('DESCRIPTION')))
        presentation.append((elements.get('summary')))
        begin.append((elements.get('dtstart').dt))
        end.append((elements.get('DTEND').dt)) 
        period+=(elements.get('DTEND').dt-elements.get('dtstart').dt).total_seconds()

eventText.close()

#-------------- indico id név és intézmény kiolvasása---------------------- 
eventText = open("event2020.txt").read()
    
for elements in vobject.readComponents(eventText):
    for component in elements.components():
        search = re.match(r'Speakers:([^(]*)\((.*?)\)$', component.description.valueRepr().split('\n')[0])
        if search is None: 
            continue
        else:
            name.append(search[1].strip())
            institute.append(search[2].strip())

for component in description:
    indico_id.append(component.split('/')[-2])

#-------------- dataframe kialakítása--------------------------------------
df7=pd.DataFrame(list(zip(name, institute, presentation,begin,end,indico_id)), 
                columns =['Name', 'Intézet','Előadás címe','Előadás kezdete','Előadás vége','Indico azonosító' ])
 
#---------dátumokról a timzonok levétele, egyébként ValueError ------------
df7['Előadás kezdete'] = df7['Előadás kezdete'].dt.tz_localize(None)
df7['Előadás vége'] = df7['Előadás vége'].dt.tz_localize(None)

#---------------------Résztvevők számának meghatározása--------------------
countMember.append(len(name))

#---------------------Előadások hosszának meghatározása--------------------
presentationLength.append(period/60)

#--------------------------Listák nullázása--------------------------------
presentation.clear()
begin.clear()
end.clear()
description.clear()
indico_id.clear()
name.clear()
institute.clear()
period=0

#-----------------------diagramok-----------------------------------------
years = ['2007','2008','2009','2010','2011','2012','2020']

#-----------------------1. diagram-----------------------------------------
plt.bar(years, presentationLength)
plt.title('Előadások hossza az évek szerint')
plt.xlabel('Évek')
plt.ylabel('Előadások hossza (perc)')
plt.savefig('dia1.png')
plt.close()

#-----------------------2. diagram-----------------------------------------
plt.bar(years, countMember)
plt.title('Résztvevők száma az évek szerint')
plt.xlabel('Évek')
plt.ylabel('Résztvevők száma')
plt.savefig('dia2.png')
plt.close()

#-----------------------3. diagram-----------------------------------------
plt.plot(countMember,presentationLength)
plt.title('Előadások hossza a résztvevők szerint')
plt.xlabel('Résztvevők száma')
plt.ylabel('Előadások hossza (perc)')
plt.savefig('dia3.png')
plt.close()

#-----------------------dataframe a diagramhoz-----------------------------
df8=pd.DataFrame()

#--------------------.xlsx fájlba írás------------------------------------
writer = pd.ExcelWriter('beadando.xlsx', engine='xlsxwriter')

df1.to_excel(writer, sheet_name='2007', encoding='ISO-8859-2', index = False)
df2.to_excel(writer, sheet_name='2008', encoding='ISO-8859-2', index = False)
df3.to_excel(writer, sheet_name='2009', encoding='ISO-8859-2', index = False)
df4.to_excel(writer, sheet_name='2010', encoding='ISO-8859-2', index = False)
df5.to_excel(writer, sheet_name='2011', encoding='ISO-8859-2', index = False)
df6.to_excel(writer, sheet_name='2012', encoding='ISO-8859-2', index = False)
df7.to_excel(writer, sheet_name='2020', encoding='ISO-8859-2', index = False)

df8.to_excel(writer, sheet_name='Diagram')
worksheet = writer.sheets['Diagram']

worksheet.insert_image('A1','dia1.png')
worksheet.insert_image('J1','dia2.png')
worksheet.insert_image('F21','dia3.png')

writer.save()