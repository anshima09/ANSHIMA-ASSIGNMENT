package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import static org.apache.spark.sql.functions.*;
public class Top5Words {
    public static void main(String[] args){
        SparkSession spark = SparkSession.builder()
                .appName("SalesPerProduct")
                .master("local[*]")
                .getOrCreate();

        Dataset<Row> textDF = spark.read().text("C://resources/input.txt");

        Dataset<Row> words = textDF.select(explode(split(col("value"), "\\s+")).alias("word"))
                .filter(col("word").notEqual(""));

        Dataset<Row> wordCounts = words.groupBy("word").count().orderBy(col("count").desc());

        wordCounts.limit(5).show();
        spark.stop();
    }
}
