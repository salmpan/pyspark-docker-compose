from pyspark.sql import SparkSession

def init_spark():
    sql = SparkSession.builder\
        .appName("dummy-app")\
        .getOrCreate()
    sc = sql.sparkContext
    return sql, sc

def main():
    csv_file = "/opt/data/iris.csv"
    sql, sc = init_spark()

    df = sql.read.load(csv_file, format = "csv", inferSchema="true", sep=",", header="true")
    df.where(df.variety == 'Setosa') \
        .write.csv("/opt/data/out")


if __name__ == '__main__':
    main()
