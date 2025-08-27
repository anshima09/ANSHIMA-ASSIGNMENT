package com.SparkExample;


import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

public class RemoveDuplicates {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder()
                .appName("RemoveDuplicates")
                .master("local[*]")
                .getOrCreate();

        Dataset<Row> df = spark.read().option("header","true").csv("C://resources/data.csv");

        Dataset<Row> distinctDf = df.dropDuplicates();

        distinctDf.show();
        spark.stop();
    }
}
