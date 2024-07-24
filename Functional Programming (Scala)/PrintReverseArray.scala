object printreverse {
	def main(args: Array[String]): Unit = {
	  var arr = Array(12,32,14,12,43,22)
	  
	  for(i <- (arr.length-1 to 0 by -1)) {
	    println(arr(i))
	  }
	}
}