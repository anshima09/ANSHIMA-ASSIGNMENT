package com.SparkExample;

import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.sql.SparkSession;

import java.io.Serializable;
import java.util.Comparator;

public class CsvOperationsRdd {
    public static void main(String[] args){
        SparkSession spark = SparkSession.builder()
                .appName("CsvOperationsRdd") // It's good practice to name your app
                .master("local[*]")
                .getOrCreate();

        JavaRDD<String> lines = spark.sparkContext()
                .textFile("C://resources/data.csv", 1)
                .toJavaRDD();

        String header = lines.first();
        int colIdx = 2;

        // Create the RDD of doubles and then cache it
        JavaRDD<Double> vals = lines
                .filter(line -> !line.equals(header))
                .map(line -> Double.parseDouble(line.split(",")[colIdx]))
                .cache(); // <-- **CACHE THE RDD HERE**

        // Now, all subsequent actions will use the cached RDD from memory
        // instead of re-reading and re-processing the original file.
        double sum = vals.reduce(Double::sum);
        long count = vals.count();
        double min = vals.min((Comparator<Double> & Serializable) Double::compareTo);
        double max = vals.max((Comparator<Double> & Serializable) Double::compareTo);

        // Avoid division by zero if the file is empty or has only a header
        if (count > 0) {
            System.out.println("Average: " + (sum / count));
            System.out.println("Min: " + min);
            System.out.println("Max: " + max);
        } else {
            System.out.println("No data found to process.");
        }

        spark.stop();
    }
}