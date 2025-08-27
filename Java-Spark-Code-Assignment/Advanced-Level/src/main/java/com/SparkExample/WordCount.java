package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.functions;

public class WordCount {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder()
                .appName("Word Count")
                .master("local[*]")
                .getOrCreate();

        Dataset<Row> df = spark.read().text("C://resources/sentences.txt");

        Dataset<Row> words = df.select(functions.explode(functions.split(df.col("value"), " ")).alias("word"));

        Dataset<Row> wordCounts = words.groupBy("word").count();

        wordCounts.show();

        spark.stop();
    }
}
