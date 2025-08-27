package com.SparkExample;

import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SaveMode;
import org.apache.spark.sql.SparkSession;

import java.util.Properties;

public class JDBCExample {
    public static void main(String[] args) {
        SparkSession spark = SparkSession.builder()
                .appName("JDBC Example")
                .master("local[*]")
                .getOrCreate();

        Properties connectionProperties = new Properties();
        connectionProperties.put("user", "root");
        connectionProperties.put("password", "anshima@1123");
        connectionProperties.put("driver", "com.mysql.cj.jdbc.Driver");

        Dataset<Row> df = spark.read()
                .jdbc("jdbc:mysql://localhost:3306/testdb", "employees", connectionProperties);

        df.show();

        df.write()
                .mode(SaveMode.Overwrite)
                .jdbc("jdbc:mysql://localhost:3306/testdb", "employees_copy", connectionProperties);

        spark.stop();
    }
}
