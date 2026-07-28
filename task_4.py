new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005'] 
completed_tasks = ['task_002', 'task_012', 'task_006']

completed_tasks.append(new_tasks.pop(new_tasks.index('task_005'))) #Удаляем Task005 из одного списка и добавляем в другой
new_tasks.remove('task_007') #Удаляем Task007
print('Взять в работу '+new_tasks[-1] ) #Взять в работу 
print(new_tasks,completed_tasks) 
#