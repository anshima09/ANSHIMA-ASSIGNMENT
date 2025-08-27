package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

public class CorelationExample {
    public static void main(String[] args) {

        SparkSession spark = SparkSession.builder()
                .appName("Correlation Example")
                .master("local[*]")
                .getOrCreate();

        Dataset<Row> df = spark.read()
                .option("header", "true")
                .option("inferSchema", "true")
                .csv("C://resources/data1.csv");

        double correlation = df.stat().corr("col1", "col2");
        System.out.println("Correlation between col1 and col2: " + correlation);

        spark.stop();
    }
}
