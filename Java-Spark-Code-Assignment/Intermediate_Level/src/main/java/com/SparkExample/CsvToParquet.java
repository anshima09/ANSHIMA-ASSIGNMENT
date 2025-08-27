package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

public class CsvToParquet {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder().appName("CsvToParquet").master("local[*]").getOrCreate();

        Dataset<Row> df = spark.read().option("header", "true").csv("C://resources/data.csv");
        df.write().parquet("output.parquet");

        Dataset<Row> parquetDF = spark.read().parquet("output.parquet");
        parquetDF.show();

        spark.stop();
    }
}
