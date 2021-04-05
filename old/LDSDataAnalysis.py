#!/usr/bin/python3
import pandas as pd

rls2007df = pd.read_spss('dataset_Religious_Landscape_Survey_Data/Religious Landscape Survey Data - Continental US.sav')
print("2007 RLS Data Frame")
print(rls2007df)


rls2014df = pd.read_spss('Pew-Research-Center-2014-U.S.-Religious-Landscape-Study/Dataset - Pew Research Center 2014 Religious Landscape Study National Telephone Survey - Version 1.1 - December 1 2016.sav')
print("2014 RLS Data Frame")
print(rls2014df)




rls2007WeightTotal=rls2007df['weight'].sum()
print("2007 weight total: " + str(rls2007WeightTotal))
rls2014WeightTotal=rls2014df['WEIGHT'].sum()
print("2014 weight total: " + str(rls2014WeightTotal))



rls2007LDSdf=rls2007df.loc[rls2007df['denom']==' Church of Jesus Christ of Latter Day Saints']
rls2007LDSWeightTotal=rls2007LDSdf['weight'].sum()
rls2007Mormondf=rls2007df.loc[rls2007df['reltrad']==' Mormon']
rls2007MormonWeightTotal=rls2007Mormondf['weight'].sum()

print('2007RLS: % LDS = ' + str(rls2007LDSWeightTotal/rls2007WeightTotal))
print('2007RLS: % Mormon = ' + str(rls2007MormonWeightTotal/rls2007WeightTotal))




rls2014LDSdf=rls2014df.loc[rls2014df['DENOM']=='Church of Jesus Christ of Latter Day Saints']
rls2014LDSWeightTotal=rls2014LDSdf['WEIGHT'].sum()
rls2014Mormondf=rls2014df.loc[rls2014df['RELTRAD']=='Mormon']
rls2014MormonWeightTotal=rls2014Mormondf['WEIGHT'].sum()


print('2014RLS: % LDS = ' + str(rls2014LDSWeightTotal/rls2014WeightTotal))
print('2014RLS: % Mormon = ' + str(rls2014MormonWeightTotal/rls2014WeightTotal))


#Don't Know
rls2007LDSDontKnowAttenddf=rls2007LDSdf.loc[rls2007LDSdf['q20']=="Don't know/Refused (VOL.)"]
rls2007LDSDontKnowAttendWeightTotal=rls2007LDSDontKnowAttenddf['weight'].sum()
rls2007LDSDontKnowAttendWeightTotal
rls2007LDSDontKnowAttendFrac=rls2007LDSDontKnowAttendWeightTotal/rls2007LDSWeightTotal

#Never
rls2007LDSNeverAttenddf=rls2007LDSdf.loc[rls2007LDSdf['q20']=='Never']
rls2007LDSNeverAttendWeightTotal=rls2007LDSNeverAttenddf['weight'].sum()
rls2007LDSNeverAttendWeightTotal
rls2007LDSNeverAttendFrac=rls2007LDSNeverAttendWeightTotal/rls2007LDSWeightTotal


#Seldom
rls2007LDSSeldomAttenddf=rls2007LDSdf.loc[rls2007LDSdf['q20']=='Seldom']
rls2007LDSSeldomAttendWeightTotal=rls2007LDSSeldomAttenddf['weight'].sum()
rls2007LDSSeldomAttendWeightTotal
rls2007LDSSeldomAttendFrac=rls2007LDSSeldomAttendWeightTotal/rls2007LDSWeightTotal


#A few times a year
rls2007LDSYearAttenddf=rls2007LDSdf.loc[rls2007LDSdf['q20']=='A few times a year']
rls2007LDSYearAttendWeightTotal=rls2007LDSYearAttenddf['weight'].sum()
rls2007LDSYearAttendWeightTotal
rls2007LDSYearAttendFrac=rls2007LDSYearAttendWeightTotal/rls2007LDSWeightTotal


#Once or twice a month
rls2007LDSMonthAttenddf=rls2007LDSdf.loc[rls2007LDSdf['q20']=='Once or twice a month']
rls2007LDSMonthAttendWeightTotal=rls2007LDSMonthAttenddf['weight'].sum()
rls2007LDSMonthAttendWeightTotal
rls2007LDSMonthAttendFrac=rls2007LDSMonthAttendWeightTotal/rls2007LDSWeightTotal


#Once a week
rls2007LDSWeekAttenddf=rls2007LDSdf.loc[rls2007LDSdf['q20']=='Once a week']
rls2007LDSWeekAttendWeightTotal=rls2007LDSWeekAttenddf['weight'].sum()
rls2007LDSWeekAttendWeightTotal
rls2007LDSWeekAttendFrac=rls2007LDSWeekAttendWeightTotal/rls2007LDSWeightTotal


#More than once a week
rls2007LDSMoreAttenddf=rls2007LDSdf.loc[rls2007LDSdf['q20']=='More than once a week']
rls2007LDSMoreAttendWeightTotal=rls2007LDSMoreAttenddf['weight'].sum()
rls2007LDSMoreAttendWeightTotal
rls2007LDSMoreAttendFrac=rls2007LDSMoreAttendWeightTotal/rls2007LDSWeightTotal



rls2007LDSDontKnowAttendFrac
rls2007LDSNeverAttendFrac
rls2007LDSSeldomAttendFrac
rls2007LDSYearAttendFrac
rls2007LDSMonthAttendFrac
rls2007LDSWeekAttendFrac
rls2007LDSMoreAttendFrac


rls2007AttendFracCheck=rls2007LDSDontKnowAttendFrac + rls2007LDSNeverAttendFrac + rls2007LDSSeldomAttendFrac + rls2007LDSYearAttendFrac + rls2007LDSMonthAttendFrac + rls2007LDSWeekAttendFrac + rls2007LDSMoreAttendFrac
rls2007AttendFracCheck


rls2007AttendCheckWeightTotal=rls2007LDSDontKnowAttendWeightTotal + rls2007LDSNeverAttendWeightTotal + rls2007LDSSeldomAttendWeightTotal + rls2007LDSYearAttendWeightTotal + rls2007LDSMonthAttendWeightTotal + rls2007LDSWeekAttendWeightTotal + rls2007LDSMoreAttendWeightTotal
rls2007AttendCheckWeightTotal



#Code to print all answers to q20, attendance:
#for i in rls2007LDSdf['q20']:
# print(i)



