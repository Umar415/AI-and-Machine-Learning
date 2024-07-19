object strPrnt {
	def main(args: Array[String]): Unit = {
	  var strarr = new Array[String](5)
    strarr(0) = "This"
    strarr(1) = "is"
    strarr(2) = "the"
    strarr(3) = "scala"
    strarr(4) = "language"
    var strmin = ""
    for(i <- 0 to (strarr.length - 1)){
      for(j <- 0 to (strarr.length - 1)){
          if(strarr(i).length < strarr(j).length){
          strmin = strarr(j)
          strarr(j) = strarr(i)
          strarr(i) = strmin
        }
      }
    }
    for(i <- strarr){
      print(i + " ")
    }
	}
}