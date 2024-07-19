import java.util.Scanner
object DogYearCal {
	def main(args: Array[String]): Unit = {
	  var sc = new Scanner(System.in)
	  println("Please enter your age: ")
	  var num = sc.nextInt()
	  
	  var dgyr = 0.0
	  
	  for(i <- 1 to num){
	    if(i <= 2){
	      dgyr += 10.5
	    }else{
	      dgyr += 4
	    }
	  }
	  println("Your DOG age in human aging is: " + dgyr)
	  
	}
}