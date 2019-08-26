import requests

#url = "http://product-service/"

myResponse = requests.get('http://product-service/')
#print (myResponse.status_code)

# For successful API call, response code will be 200 (OK)
if(myResponse.ok):

    
    print("The response contains {0} properties")
    print("\n")
   
else:
  # If response code is not ok (200), print the resulting http error code with description
    myResponse.raise_for_status()
