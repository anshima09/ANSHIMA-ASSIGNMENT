package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import static org.apache.spark.sql.functions.*;

public class FilterNumEmpty {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder().appName("FilterNullEmpty").master("local[*]").getOrCreate();

        Dataset<Row> df = spark.read().option("header", "true").csv("C://resources/data.csv");

        Dataset<Row> cleaned = df.filter(col("name").isNotNull().and(length(trim(col("name"))).gt(0)));

        cleaned.show();
        spark.stop();
    }
}
