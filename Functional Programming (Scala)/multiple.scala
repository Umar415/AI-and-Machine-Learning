object multiple {
	def main(args: Array[String]): Unit = {
    multiple(50)
	}
	
	def multiple(num: Int): Unit = {
    for (i <- 1 until num) {
      if (i % 3 == 0) {
        println(i)
      }
    }
  }
}