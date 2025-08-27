package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.functions;

public class SaltingExample {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder()
                .appName("Salting Example")
                .master("local[*]")
                .getOrCreate();

        Dataset<Row> df = spark.read().option("header", "true").csv("C://resources/orders.csv");

        // Add a salt column to distribute skewed keys
        Dataset<Row> salted = df.withColumn("salted_key",
                functions.concat(df.col("customer_id"), functions.lit("_"), functions.floor(functions.rand().multiply(10))));

        salted.groupBy("salted_key").count().show();

        spark.stop();
    }
}
