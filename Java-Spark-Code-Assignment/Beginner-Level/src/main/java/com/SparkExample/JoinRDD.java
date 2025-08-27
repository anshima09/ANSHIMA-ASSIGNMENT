package com.SparkExample;

import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.SparkSession;
import scala.Tuple2;

import java.util.Arrays;
import java.util.List;

public class JoinRDD {
    public static void main(String[] args){
        SparkSession spark = SparkSession.builder()
                .appName("JoinRDD")
                .master("local[*]")
                .getOrCreate();

        JavaSparkContext sc = new JavaSparkContext(spark.sparkContext());


        List<Tuple2<Integer, String>> data1 = Arrays.asList(
                new Tuple2<>(1, "Alice"),
                new Tuple2<>(2, "Bob"),
                new Tuple2<>(3, "Charlie")
        );

        List<Tuple2<Integer, Integer>> data2 = Arrays.asList(
                new Tuple2<>(1, 90),
                new Tuple2<>(2, 80),
                new Tuple2<>(3, 85)
        );


        JavaPairRDD<Integer, String> rdd1 = sc
                .parallelizePairs(data1,1);
        JavaPairRDD<Integer, Integer> rdd2 = sc
                .parallelizePairs(data2, 1);

        JavaPairRDD<Integer, Tuple2<String, Integer>> joined = rdd1.join(rdd2);

        joined.collect().forEach(t ->
                System.out.println("ID: " + t._1 + ", Name: " + t._2._1 + ", Score: " + t._2._2));

        spark.stop();
    }

}
