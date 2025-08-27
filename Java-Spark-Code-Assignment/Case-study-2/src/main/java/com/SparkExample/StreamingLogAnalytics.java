package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import static org.apache.spark.sql.functions.*;
import org.apache.spark.sql.streaming.StreamingQuery;
import org.apache.spark.sql.streaming.OutputMode;
import java.io.File;
import org.apache.spark.sql.types.*;
import java.util.concurrent.TimeoutException;
import org.apache.spark.sql.streaming.StreamingQueryException;
public class StreamingLogAnalytics {

    public static void main(String[] args) throws java.util.concurrent.TimeoutException  {
        if (args.length < 2) {
            System.err.println("Usage: StreamingLogAnalytics <inputDir> <outputDir>");
            System.exit(1);
        }


        StructType schema = new StructType()
                .add("user_id", DataTypes.StringType)
                .add("video_id", DataTypes.StringType)
                .add("watch_time", DataTypes.IntegerType)
                .add("timestamp", DataTypes.StringType); // will convert to Timestamp later


        String inputDir = args[0];
        String outputDir = args[1];

        new File(outputDir).mkdirs();

        SparkSession spark = SparkSession.builder()
                .appName("Streaming Log Analytics")
                .master("local[*]")
                .getOrCreate();

        Dataset<Row> logs = spark.readStream()
                .option("header", true)
                .schema(schema)  // ✅ specify schema explicitly
                .csv(inputDir)
                .withColumn("timestamp", to_timestamp(col("timestamp"), "yyyy-MM-dd HH:mm:ss"));


        Dataset<Row> filteredLogs = logs.filter(col("watch_time").geq(120));

        Dataset<Row> watchTimePerUser = filteredLogs
                .withWatermark("timestamp", "1 minute") // <-- add watermark
                .groupBy(col("user_id"), window(col("timestamp"), "5 minutes"))
                .agg(sum("watch_time").alias("total_watch_time"));



        Dataset<Row> topVideos = filteredLogs
                .groupBy(col("video_id"), window(col("timestamp"), "10 minutes"))
                .agg(sum("watch_time").alias("total_watch_time"));

// NO .orderBy() here


        StreamingQuery userQuery = watchTimePerUser.writeStream()
                .outputMode(OutputMode.Update())
                .format("console")
                .option("truncate", false)
                .start();

        StreamingQuery topVideoQuery = topVideos.writeStream()
                .outputMode(OutputMode.Update())
                .format("console")
                .option("truncate", false)
                .start();

        watchTimePerUser.writeStream()
                .outputMode("complete") // for aggregated streaming DF
                .format("console")
                .option("truncate", false)
                .start();


        topVideos.writeStream()
                .outputMode("complete")   // Must be complete mode
                .format("console")
                .option("truncate", false)
                .start();


        try {
            spark.streams().awaitAnyTermination();
        } catch (org.apache.spark.sql.streaming.StreamingQueryException e) {
            e.printStackTrace();
        }
    }
}
