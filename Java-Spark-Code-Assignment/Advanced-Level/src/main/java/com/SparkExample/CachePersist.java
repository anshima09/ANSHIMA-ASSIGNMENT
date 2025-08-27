package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.storage.StorageLevel;

public class CachePersist {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder()
                .appName("Cache & Persist")
                .master("local[*]")
                .getOrCreate();

        Dataset<Row> df = spark.read()
                .option("header", "true")
                .csv("C://resources/data.csv");

        df.cache(); // memory only
        df.persist(StorageLevel.MEMORY_AND_DISK()); // memory + disk

        df.count(); // action triggers caching
        df.show();

        spark.stop();
    }
}
