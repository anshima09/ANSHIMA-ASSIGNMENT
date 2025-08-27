package com.SparkExample;


import org.apache.spark.sql.*;

public class SimpleETL {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder()
                .appName("Simple ETL")
                .master("local[*]")
                .getOrCreate();

        Dataset<Row> df = spark.read()
                .option("header", "true")
                .csv("C://resources/data.csv");

        // Example transformation: uppercase a column
        Dataset<Row> transformed = df.withColumn("name_upper", functions.upper(df.col("name")));

        transformed.write()
                .mode(SaveMode.Overwrite)
                .parquet("output.parquet");
        transformed.show();

        spark.stop();
    }
}
