time_values = '1h 45m,360s,25m,30m 120s,2h 60s'
times=time_values.replace(' ','').split(',') #Превратим строку в список
for time in times: 
   time=time.replace('h', '*60+').replace('m', '+').replace('s', '/60+') #Приведем все элементы списока к минутам
   if time[-1]=='+': #Уберем в конце + если он существует 
      time=time[:-1] 
sum_time=int(eval(time))

print(f"Сумма минут в строке {sum_time}")
#
