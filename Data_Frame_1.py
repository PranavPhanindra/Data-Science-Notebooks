#!/usr/bin/env python3
import pandas as pd

olympic_data_list = pd.DataFrame({
				'HostCity' : ['London' , 'Tokyo' , 'Sydney' , 'Atlanta' ] ,
				'Year' : [2012 , 2008 , 2000 , 1996] ,
				'Participants' : [205,204,200,197]
				})
print(olympic_data_list)
print("Printing HostCity names")
print(olympic_data_list.HostCity)

print("Creating a data frame from a dictionary")

student = pd.DataFrame({'London':{2012:205} , 'Beijing' : { 2008:204 }})
print(student)

print(student.describe)
print(olympic_data_list.describe)
