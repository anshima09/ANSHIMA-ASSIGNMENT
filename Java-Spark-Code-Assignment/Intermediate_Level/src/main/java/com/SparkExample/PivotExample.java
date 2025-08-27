package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import static   org.apache.spark.sql.functions.*;

public class PivotExample {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder().appName("PivotExample").master("local[*]").getOrCreate();

        Dataset<Row> df = spark.read().option("header", "true").csv("C://resources/sales.csv");

        Dataset<Row> pivotDF = df.groupBy("product").pivot("region")
                .agg(sum(df.col("amount").cast("double")));

        pivotDF.show();
        spark.stop();
    }
}
