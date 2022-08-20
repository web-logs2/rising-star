package sparkTest

import org.apache.spark.sql.{DataFrame, SparkSession}

object demo extends App {
  val spark = SparkSession.builder().config("spark.driver.host", "127.0.0.1").appName("basic example").master("local[*]").getOrCreate()
  val df: DataFrame = spark.read.json("resources/people.json")
  df.show()

}
