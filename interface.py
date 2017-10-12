import queue_formula

'''
interface with the queue_formula module
'''
menu = '''
Here is a list of the functions available\n
1. Traffic intensity
2. Average number of items in the system \n
3. Average number of elements in the queue, when there is queue\n
4. Average number of elements in the queue inlcuding times when there is no queue\n
5. Average time in the queue\n
6. Average time in the system\n
7. Probability of queueing on arrival\n
8. Probability of not queueing on arrival\n
9. Probabilty of n elements in the system at anytime\n
10. Probability of n or more elements in the system\n
Enter the number of your choice to start, 0 to quit->'''

def main():
     choice = int(input(menu))
     while choice != "q":
          if choice == 1:
               lamda = input("Enter arrival rate")
               mieu = input("Enter service rate")
               trf_ints = queue_formula.traffic_intensity(lamda,mieu)
               print ("Traffic intensity =",trf_ints)
               choice = int(input(menu))
               
          elif choice == 2:
               rho = input("Enter Traffic intensity")
               avg_num = queue_formula.avg_num_items_sys(rho)
               print ("Average number of items in the system = ",avg_num)
               choice = int(input(menu))
               
          elif choice == 3:
               rho = input("Enter Traffic intensity")
               avg_num = queue_formula.avg_num_items_queue(rho)
               print ("Average number of elements in the queue When there is queue = ",avg_num)
               choice = int(input(menu))
               
          elif choice == 4:
               rho = input("Enter Traffic intensity")
               avg_num = queue_formula.avg_num_items_nqueue(rho)
               print ("Average number of elements in the queue including times When there is no queue = ",avg_num)
               choice = int(input(menu))
               
          elif choice == 5:
               rho = input("Enter Traffic intensity")
               mieu = input("Enter service rate")
               avg_time = queue_formula.avgtime_in_queue(rho,mieu)
               time = str(avg_time)
               print ("Average time in the queue = "+time+ "mins")
               choice = int(input(menu))
               
          elif choice == 6:
               rho = input("Enter Traffic intensity")
               mieu = input("Enter service rate")
               avg_time = queue_formula.avgtime_in_system(rho,mieu)
               time = str(avg_time)
               print ("Average time in the system = "+time+ "mins")
               choice = int(input(menu))
               
          elif choice == 7:
               rho = input("Enter Traffic intensity")
               print ("The probability of queueing on arrival = ",rho)
               choice = int(input(menu))
               
          elif choice == 8:
               rho = input("Enter Traffic intensity")
               prob = queue_formula.prob_not_queuing(rho)
               print ("The probability of not queueing on arrival = ",prob)
               choice = int(input(menu))
               
          elif choice == 9:
               rho = input("Enter Traffic intensity")
               number = input("Enter number")
               prob = queue_formula.prob_n_elements_queue(rho,number)
               print ("The probability of n elements in the system at any time = ",prob)
               choice = int(input(menu))
               
          elif choice == 10:
               rho = input("Enter Traffic intensity")
               number = input("Enter number")
               prob = queue_formula.prob_n_or_more(rho,number)
               print ("The probability of n or more elements in the system at any time = ",prob)
               choice = int(input(menu))
          else:
               break

main()
