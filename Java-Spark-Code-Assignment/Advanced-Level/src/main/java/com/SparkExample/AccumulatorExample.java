package com.SparkExample;

import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.util.LongAccumulator;

public class AccumulatorExample {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder()
                .appName("Accumulator Example")
                .master("local[*]")
                .getOrCreate();
        JavaSparkContext jsc = new JavaSparkContext(spark.sparkContext());

        LongAccumulator errorCount = jsc.sc().longAccumulator("ErrorCount");

        Dataset<String> lines = spark.read().textFile("C://resources/logs.txt");

        lines.foreach(line -> {
            if (line.contains("ERROR")) {
                errorCount.add(1);
            }
        });

        System.out.println("Total ERROR lines: " + errorCount.value());

        spark.stop();
    }
}
