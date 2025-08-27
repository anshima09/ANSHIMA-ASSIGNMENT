package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.expressions.Window;
import org.apache.spark.sql.expressions.WindowSpec;

import static org.apache.spark.sql.functions.*;

public class MovingAverage {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder().appName("MovingAverage").master("local[*]").getOrCreate();

        Dataset<Row> df = spark.read().option("header", "true").csv("C://resources/sales.csv");

        WindowSpec w = Window.orderBy("date").rowsBetween(-2, 0); // 3-day moving avg

        Dataset<Row> withMovingAvg = df.withColumn("moving_avg",
                avg(df.col("amount").cast("double")).over(w));

        withMovingAvg.show();
        spark.stop();
    }
}
