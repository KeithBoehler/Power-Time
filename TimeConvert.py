import arrow #this has the functions that i need to work with time. 

#get time from the user  
LocalTime = raw_input('Please enter the local time. YYYY-MM-DD HH:mm:ss ')

#parse from string 
arrow.get(LocalTime)

print LocalTime

#shorthand to go form local to utc 
UTCtime = utc.to('LocalTime').to('utc')

#Test to see if the utc converter worked 
print UTCtime
