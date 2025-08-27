package com.SparkExample;

import org.apache.spark.api.java.JavaDoubleRDD;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.sql.SparkSession;
import scala.Tuple2;

public class CharacterCountRDD {
    public static void main(String[] args){
        SparkSession spark = SparkSession.builder()
                .appName("CharacterCountRDD")
                .master("local[*]")
                .getOrCreate();

        JavaRDD<String> lines = spark.sparkContext()
                .textFile("C://resources/input.txt",1)
                .toJavaRDD();

        JavaPairRDD<Character,Integer> characterCounts = lines
                .flatMap(line-> line.replaceAll("\\s+"," ").chars()
                        .mapToObj(c-> (char)c).iterator())
                .mapToPair(c-> new Tuple2<>(c,1))
                .reduceByKey(Integer::sum);

        characterCounts.collect().forEach(t -> System.out.println(t._1 + " : " + t._2));

        spark.stop();

    }

}
