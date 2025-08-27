package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SaveMode;
import org.apache.spark.sql.SparkSession;

public class RepartitionCoalesce {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder()
                .appName("Repartition & Coalesce")
                .master("local[*]")
                .getOrCreate();

        Dataset<Row> df = spark.read()
                .option("header", "true")
                .csv("C://resources/data.csv");

        Dataset<Row> repartitioned = df.repartition(10); // increase partitions
        Dataset<Row> coalesced = repartitioned.coalesce(2); // reduce partitions

        coalesced.write().mode(SaveMode.Overwrite).parquet("output_partitioned.parquet");
        coalesced.show();

        spark.stop();
    }
}
