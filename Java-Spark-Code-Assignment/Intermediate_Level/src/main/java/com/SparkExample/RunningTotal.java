package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.expressions.WindowSpec;
import org.apache.spark.sql.expressions.Window;

import static org.apache.spark.sql.functions.*;


public class RunningTotal {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder()
                .appName("SalesPerProduct")
                .master("local[*]")
                .getOrCreate();
        Dataset<Row> df = spark.read().option("header", "true").csv("C://resources/sales.csv");

        WindowSpec w = Window.orderBy("date").rowsBetween(Window.unboundedPreceding(), Window.currentRow());

        Dataset<Row> withRunningTotal = df.withColumn("running_total",
                sum(df.col("amount").cast("double")).over(w));

        withRunningTotal.show();
        spark.stop();
    }

}
