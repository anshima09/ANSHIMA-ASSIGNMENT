package com.SparkExample;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaPairRDD;
import scala.Tuple2;

import java.util.Arrays;

public class GroupByCountRDD {



        public static void main(String[] args) {
            SparkSession spark = SparkSession.builder()
                    .appName("GroupByCountRDD")
                    .master("local[*]")
                    .getOrCreate();

            JavaRDD<String> lines = spark.sparkContext()
                    .textFile("C://resources/data.csv", 1)
                    .toJavaRDD();

            String header = lines.first();
            int colIndex = 1; // column to group by

            JavaPairRDD<String, Integer> grouped = lines
                    .filter(line -> !line.equals(header))
                    .mapToPair(line -> new Tuple2<>(line.split(",")[colIndex], 1))
                    .reduceByKey(Integer::sum);

            grouped.collect().forEach(t -> System.out.println(t._1 + " : " + t._2));

            spark.stop();

    }

}
