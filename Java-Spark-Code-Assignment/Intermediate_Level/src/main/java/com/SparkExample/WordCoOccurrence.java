package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import static org.apache.spark.sql.functions.*;

public class WordCoOccurrence {
    public static void main(String[] args){
        SparkSession spark = SparkSession.builder()
                .appName("SalesPerProduct")
                .master("local[*]")
                .getOrCreate();

        Dataset<Row> textDF = spark.read().text("C://resources/input.txt");

        Dataset<Row> wordsPerLine = textDF.select(split(col("value"), "\\s+").alias("words"));

        Dataset<Row> exploded = wordsPerLine.selectExpr("explode(words) as word1", "explode(words) as word2")
                .filter("word1 != word2");

        Dataset<Row> coOccurrence = exploded.groupBy("word1", "word2").count();

        coOccurrence.show();
        spark.stop();

    }
}
