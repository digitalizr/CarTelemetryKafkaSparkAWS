# Tutorial on Real Time Data Ingestion and Projection

This project is based on a [youtube tutorial](https://www.youtube.com/watch?v=Vv_fvwF41_0).


![Illustration of the application.](https://th.bing.com/th/id/OIP.WcKwgKljM0HXAus2uoVKygHaFW?rs=1&pid=ImgDetMain)

## Project architecture

![image](https://github.com/eremah/SmartCity/assets/75796623/71b08b0f-0484-4347-87f8-237224cd01f7)


spark-submit \--master spark://spark-master:7077 \--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0,org.apache.hadoop:hadoop-aws:3.3.1,com.amazonaws:aws-java-sdk:1.11.469 \jobs/spark-city.py