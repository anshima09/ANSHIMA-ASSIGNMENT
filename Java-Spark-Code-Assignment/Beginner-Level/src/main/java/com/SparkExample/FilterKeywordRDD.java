package com.SparkExample;

import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.sql.SparkSession;

public class FilterKeywordRDD {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder()
                .appName("FilterKeywordRDD")
                .master("local[*]")
                .getOrCreate();

        String keyword = "Spark";
        JavaRDD<String> lines = spark.sparkContext()
                .textFile("C://resources/input.txt", 1)
                .toJavaRDD();

        JavaRDD<String> filtered = lines.filter(line -> line.contains(keyword));

        filtered.collect().forEach(System.out::println);

        spark.stop();
    }

}
