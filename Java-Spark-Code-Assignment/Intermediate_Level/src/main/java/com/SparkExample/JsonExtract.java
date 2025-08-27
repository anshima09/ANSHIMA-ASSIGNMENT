package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;

public class JsonExtract {
    public static void main(String[] args){
        SparkSession spark = SparkSession.builder()
                .appName("JsonExtract")
                .master("local[*]")
                .getOrCreate();

        Dataset<Row> df = spark.read().option("multiline", "true").json("C://resources/input.json");
        Dataset<Row> selected = df.select("id", "name", "price");

        selected.show();
        spark.stop();
    }
}
