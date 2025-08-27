package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

public class MultiFilter {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder()
                .appName("Multi Filter")
                .master("local[*]")
                .getOrCreate();

        Dataset<Row> df = spark.read()
                .option("header", "true")
                .option("inferSchema", "true")
                .csv("C://resources/data.csv");

        Dataset<Row> filtered = df.filter("age > 25 AND salary > 50000");

        filtered.show();

        spark.stop();
    }
}
