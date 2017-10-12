'''
The following formulas can be derived for simple queues,
here i have simply created functions for each of the
queing formulas
'''
#rho = traffic floatensity
#mieu = service rate
#lamda = arrival rate (had to change the spelling because 'lambda' is a key word)

def traffic_intensity(lamda,mieu):
     u = float(mieu)
     h = float(lamda)
     rho = h/u
     return rho

def avg_num_items_sys(rho):
     p = float(rho)
     avg_num = p/(1-p)
     return avg_num

def avg_num_items_queue(rho):
     #this is the average number, when there is a queue
     p = float(rho)
     avg_num = 1/(1-p)
     return avg_num

def avg_num_items_nqueue(rho):
     #this is the average number, when there is no queue,n stands for 'no'
     p = float(rho)
     avg_num = (p**2)/(1-p)
     return avg_num

def avgtime_in_queue(rho,mieu):
     p = float(rho)
     u = float(mieu)
     #this is the average time spent in the queue
     #number in the system
     avg_num = p/(1-p)
     #average service? rate
     service_rate = 1/u
     avg_time = float(avg_num) * float(service_rate)
     #convert to minutes
     avg_time_mins = float(avg_time) * 60
     return avg_time_mins

def avgtime_in_system(rho,mieu):
     p = float(rho)
     u = float(mieu)
     #this is the average time spent in the system
     #number in the queue
     avg_num = 1/(1-p)
     #average service? rate
     service_rate = 1/u
     avg_time = float(avg_num) * float(service_rate)
     #convert to minutes
     avg_time_mins = float(avg_time) * 60
     return avg_time_mins

def prob_not_queuing(rho):
     #probability of not queueing on arrival
     p = float(rho)
     prob = 1-p
     return prob

def prob_n_elements_queue(rho,number):
     #probability of n elements in the system at any time
     p = float(rho)
     n = float(number)
     prob = (1-p)* (p**n)
     return prob

def prob_n_or_more(rho,number):
     #probability of n OR MORE elements in the system at any time
     p = float(rho)
     n = float(number)
     prob = p**n
     return prob

     