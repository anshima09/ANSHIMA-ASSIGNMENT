package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

public class JoinsExample {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder().appName("JoinsExample").master("local[*]").getOrCreate();

        Dataset<Row> df1 = spark.read().option("header", "true").csv("C://resources/customer.csv");
        Dataset<Row> df2 = spark.read().option("header", "true").csv("C://resources/orders.csv");

        df1.join(df2, df1.col("id").equalTo(df2.col("customer_id")), "inner").show();
        df1.join(df2, df1.col("id").equalTo(df2.col("customer_id")), "left").show();
        df1.join(df2, df1.col("id").equalTo(df2.col("customer_id")), "right").show();

        spark.stop();
    }
}
