package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

public class unpivotExample {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder().appName("UnpivotExample").master("local[*]").getOrCreate();
        Dataset<Row> df = spark.read().option("header", "true").csv("C://resources/pivoted.csv");

        String[] regions = {"North", "South", "East", "West"};

        Dataset<Row> unpivotDF = df.selectExpr("product",
                "stack(" + regions.length + ", " +
                        String.join(", ",
                                java.util.Arrays.stream(regions)
                                        .map(r -> "'" + r + "', " + r)
                                        .toArray(String[]::new))
                        + ") as (region, amount)");

        unpivotDF.show();
        spark.stop();
    }
}
