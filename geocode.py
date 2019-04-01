import reverse_geocoder as rg 
import pprint 
  
def reverseGeocode(coordinates): 
    result = rg.search(coordinates) 
      
    # result is a list containing ordered dictionary. 
    pprint.pprint(result)  
  
# Driver function 
if __name__=="__main__":
	

	#coordinates =(28.613939, 77.209023)
    print("Please Enter the Latitude :") 
    coordinates1=input()
    print("Please Enter the Longitude : ")
    coordinates2=input()
    coordinates=(coordinates1,coordinates2)
    reverseGeocode(coordinates)  