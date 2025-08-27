package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.apache.spark.sql.SaveMode;

import static org.apache.spark.sql.functions.*;

public class ECommerceSalesAnalysis {
    public static void main(String[] args) {
        if (args.length < 3) {
            System.err.println("Usage: ECommerceSalesAnalysis <orders.csv> <users.csv> <outputDir>");
            System.exit(1);
        }
        String ordersPath = args[0];
        String usersPath = args[1];
        String outputPath = args[2];

        SparkSession spark = SparkSession.builder()
                .appName("E-Commerce Sales Analysis")
                .master("local[*]") // remove or change when running on cluster
                .getOrCreate();

        // 1) Read CSVs (header + schema inference)
        Dataset<Row> orders = spark.read()
                .option("header", "true")
                .option("inferSchema", "true")
                .option("timestampFormat", "yyyy-MM-dd HH:mm:ss")
                .csv(ordersPath);

        Dataset<Row> users = spark.read()
                .option("header", "true")
                .option("inferSchema", "true")
                .csv(usersPath);

        // 2) Clean / cast columns and create revenue column
        orders = orders
                .withColumn("quantity", col("quantity").cast("double"))
                .withColumn("price", col("price").cast("double"))
                .withColumn("revenue", col("quantity").multiply(col("price")))
                .withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd"));

        // 3) Total sales per product
        Dataset<Row> salesPerProduct = orders.groupBy(col("product_id"))
                .agg(
                        sum("revenue").alias("total_revenue"),
                        sum("quantity").alias("total_quantity"),
                        countDistinct("order_id").alias("num_orders")
                )
                .orderBy(col("total_revenue").desc());

        // Show top rows (for debug)
        salesPerProduct.show(10, false);

        // 4) Top 10 products by revenue
        Dataset<Row> top10Products = salesPerProduct.limit(10);
        top10Products.show(false);

        // 5) Top 5 locations by revenue (join orders -> users)
        // If users is small you can use broadcast(users) to speed up the join.
        Dataset<Row> ordersWithUsers = orders.join(users, "user_id");
        Dataset<Row> revenueByLocation = ordersWithUsers.groupBy(col("location"))
                .agg(sum("revenue").alias("total_revenue"),
                        countDistinct("user_id").alias("unique_users"))
                .orderBy(col("total_revenue").desc())
                .limit(5);
        revenueByLocation.show(false);

        // 6) Repeat customers: users with more than 5 orders
        Dataset<Row> orderCounts = orders.groupBy(col("user_id"))
                .agg(countDistinct(col("order_id")).alias("order_count"));

        Dataset<Row> repeatCustomers = orderCounts.filter(col("order_count").gt(5))
                .join(users, "user_id")
                .select("user_id", "user_name", "location", "order_count")
                .orderBy(col("order_count").desc());

        repeatCustomers.show(false);

        // 7) Save results as Parquet
        // Use partitioning if helpful (e.g. by year/month or product_id for queries)
        salesPerProduct.write().mode(SaveMode.Overwrite).parquet(outputPath + "/sales_per_product");
        top10Products.write().mode(SaveMode.Overwrite).parquet(outputPath + "/top10_products");
        revenueByLocation.write().mode(SaveMode.Overwrite).parquet(outputPath + "/top5_locations");
        repeatCustomers.write().mode(SaveMode.Overwrite).parquet(outputPath + "/repeat_customers");

        spark.stop();
    }
}
