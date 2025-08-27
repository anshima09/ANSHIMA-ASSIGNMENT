package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.functions;

import javax.xml.crypto.Data;

public class SalesPerProduct {
    public static void main(String[] args){
        SparkSession spark = SparkSession.builder()
                .appName("SalesPerProduct")
                .master("local[*]")
                .getOrCreate();

        Dataset<Row> df =spark.read().option("header","true").csv("C://resources/sales.csv");
        Dataset<Row> totalSales = df.groupBy("product")
                .agg(functions.sum(df.col("amount").cast("double")).alias("total_sales"));
        totalSales.show();
        spark.stop();

    }
}
