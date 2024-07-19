object marksheet {
	def main(args: Array[String]): Unit = {
    val marks: Array[Double] = Array(70.5, 80.0, 66.5, 90.0, 89)
    marksheet(marks, "UMAR", "23SP-008-SE")
	  
	}
	
	def marksheet(marks: Array[Double], name: String, rollnum:String): Unit = {
	  var sum = 0.0
    
    for (i <- 0 until marks.length) {
      sum = sum + marks(i)
    }
    
    val avg = sum / marks.length
    
    var grade = ""
    
    if (avg >= 90) {
      grade = "A"
    } else if (avg >= 80) {
      grade = "B"
    } else if (avg >= 70) {
      grade = "C"
    } else if (avg >= 60) {
      grade = "D"
    } else {
      grade = "F"
    }
    
    println("Name: " + name)
    println("Roll Number: " + rollnum)
    println("Grade: " + grade)
  }
}