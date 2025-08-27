package com.SparkExample;

import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.sql.SparkSession;
import scala.Tuple2;

import java.util.Arrays;


public class WordsCountRDD {
    public static void main(String[] args) {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        SparkSession spark = SparkSession.builder()
                .appName("WordsCount")
                .master("local[*]")
                .getOrCreate();

        JavaRDD<String> lines = spark.sparkContext()
                .textFile("C://resources/input.txt",1)
                .toJavaRDD();

        JavaPairRDD<String, Integer> counts = lines
                .flatMap(line-> Arrays.asList(line.split("\\s+")).iterator())
                .mapToPair(word-> new Tuple2<>(word,1))
                .reduceByKey(Integer::sum);

        counts.collect().forEach(t -> System.out.println(t._1 + " : " + t._2));

        spark.stop();

    }
}



