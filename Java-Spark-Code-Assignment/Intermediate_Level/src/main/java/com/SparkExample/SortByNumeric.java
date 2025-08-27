package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

import javax.xml.crypto.Data;

public class SortByNumeric {
    public static void main(String[] args){
        SparkSession spark = SparkSession.builder()
                .appName("SortByNumeric")
                .master("local[*]")
                .getOrCreate();

        Dataset<Row> df = spark.read().option("header","true").csv("C://resources/data.csv");
        Dataset<Row> sortDF = df.orderBy(df.col("amount").desc());

        sortDF.show();
        spark.stop();
    }
}
