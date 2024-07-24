object HelloWorld {
	def main(args: Array[String]): Unit = {
	  var arr = Array(40, 50, 30, 40, 50, 30, 30, 40, 30, 20, 30)
	  
	  var count = 0
	  var maxcount = 0
	  var msrv = 0
	  for(i <- 0 to arr.length-1){
	    for(j <- 0 to arr.length-1){
	      if (arr(i) == arr(j)) { 
          count = count +1 
        } 
	    }
	    if (count > maxcount) { 
        maxcount = count 
        msrv = arr(i)
      } 
	  }
	  
	  println("Most Repeated Value is: " + msrv)
	}
}