from justdial import*

if __name__ == "__main__" :
   state = ["Ahmedabad","Bangalore","Chandigarh","Chennai","Coimbatore","Delhi","Goa","Gurgaon","Hyderabad","Indore","Jaipur","Kolkata","Mumbai","Noida","Pune"]
   keyword = raw_input("Enter the keyword you want to crawl : ")
   for i in state:
     try:
       justdial(keyword,i)
     except:
       print "error @ "+i
    
