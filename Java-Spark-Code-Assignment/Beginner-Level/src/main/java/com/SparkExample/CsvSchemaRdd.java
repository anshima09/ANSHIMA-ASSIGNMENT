package com.SparkExample;

import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.sql.SparkSession;

public class CsvSchemaRdd {
    public static void main (String[] args){
        SparkSession spark = SparkSession.builder()
                .appName("CsvSchemaRdd")
                .master("local[*]")
                .getOrCreate();

        JavaRDD<String> lines = spark.sparkContext()
                .textFile("C://resources/data.csv",1)
                .toJavaRDD();

        String header = lines.first();

        System.out.println("Header: "+header);

        System.out.println("Number of columns: "+ header.split(",").length);

        spark.stop();


    }
}
