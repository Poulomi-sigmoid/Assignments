object bucketiseArray {
  
  def truncate_decimal_upto_three(x: Double, p: Int): Double = {
    val v = math.pow(10, p)
    (x * v).toInt / v
  }

  def bucket(y: Double): (Double, Double) = {
    var initialVal: Double = (y / 0.05).floor * 0.05;
    var finalVal: Double = (y / 0.05).floor * 0.05 + 0.049;
    return (truncate_decimal_upto_three(initialVal, 3), truncate_decimal_upto_three(finalVal, 3))
  }

  def main(args: Array[String]): Unit = {
    var input_values: Array[Double] = Array(12.05, 12.03, 10.33, 11.45, 13.5)
    for (num <- input_values) {
      print(s"$num - ")
      println(bucket(num))
    }
  }
}