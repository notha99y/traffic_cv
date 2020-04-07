from pyspark import SparkConf, SparkContext, SQLContext
from ts.flint import FlintContext, summarizers 

conf = SparkConf().setMaster("local").setAppName("TimeSeries")
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)
flintContext = FlintContext(sqlContext)


df = spark.createDataFrame(
  [('2018-08-20', 1.0), ('2018-08-21', 2.0), ('2018-08-24', 3.0)], 
  ['time', 'v']
).withColumn('time', from_utc_timestamp(col('time'), 'UTC'))

# Convert to Flint DataFrame
flint_df = flintContext.read.dataframe(df)

# Use Spark DataFrame functionality
flint_df = flint_df.withColumn('v', flint_df['v'] + 1)

# Use Flint functionality
flint_df = flint_df.summarizeCycles(summarizers.count())