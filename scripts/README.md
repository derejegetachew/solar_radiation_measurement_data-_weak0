data_cleaning.py: Cleans the raw data by handling missing values and anomalies.

eda_statistics.py: Calculate the mean, median, standard deviation, and other statistical measures for each numeric column to understand data distribution.

bubble_chart_analysis.py: explore complex relationships between variables, such as GHI vs. Tamb vs. WS, with bubble size representing an additional variable like RH or BP (Barometric Pressure)

correlation_analysis.py: visualize the correlations between solar radiation components (GHI, DNI, DHI) and temperature measures (TModA, TModB). Investigate the relationship between wind conditions (WS, WSgust, WD) and solar irradiance using scatter matrices.

data_quality_check.py: Look for missing values, outliers, or incorrect entries in columns like GHI, DNI, and DHI and check for outliers, especially in sensor readings (ModA, ModB) and wind speed data (WS, WSgust).

evaluate_cleaning_impact.py :Evaluate the impact of cleaning (using the 'Cleaning' column) on the sensor readings (ModA, ModB) over time.

histogram_analysis.py: Create histograms for variables like GHI, DNI, DHI, WS, and temperatures to visualize the frequency distribution of these variables.

temperature_analysis.py : Examine how relative humidity (RH) might influence temperature readings and solar radiation.

time_series_analysis.py : Plot bar charts of GHI, DNI, DHI, and Tamb over time to observe patterns by month, trends throughout day, or anomalies, such as peaks in solar irradiance or temperature fluctuations.

wind_analysis.py: Use wind roses Identify trends and significant wind events by showing the distribution of wind speed and direction, along with how variable the wind direction tends to be.

z_score.py: Calculate Z-scores to flag data points that are significantly different from the mean