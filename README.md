# Case_study
Consider the overall goal to be: 
Use the data on sheet "sample_03" for an analysis and a website personalization or segmentation solution

Think of this data set as being just an extract (regarding both columns and rows). You may work with this data or choose a technique to increase the numbers.

This dataset consists of directly collected data with joined information. at the moment you have no idea where columns f++ come from.

Your task:
Describe a model you would choose that would help us get information out the data. and how to use/adjust the model/analysis if used regularly
Describe at least one way how would you deploy your solution; if unsure consider GCP as an environment

Some questions:
· If you look at the data, What do you see? What would you look at in general?
· What has been done already?.What has not been done? .What else should (not)(have) been done?
· How would you choose which data to integrate into the model and and how much of it?
· How would you show accuracy/ precision or relevant statistics of your chosen model?
· What problems / challenges would you see ?
· If you look at the data, What do you see? What would you look at in general?

Presentation
Analysis
· If you look at the data, What do you see? What would you look at in general?
· What has been done already?.What has not been done? .What else should (not)(have) been done?

Model Building + feature engineering:
Looking for outliers
Testing for correlation of numeric and categorical variables
NaNs
Class balance
distribution



Model Evaluation
· How would you show accuracy/ precision or relevant statistics of your chosen model?
There are two parts to model evaluation, measuring the models abaility to predict the label and the models impact on the user, both would have to be monitored and depend on the business goals that are associated with the creation of the model. If a model was deployed to improve customer retention we would measure something different than if we were trying to increase basket size or revenue per visit or time to check out or some other metric. None of those things necessarily have to do with the quality of the models, but models aren’t that useful if they don’t achieve the business goal. 
Model Failures
This could be caused by a metric being calculated differently, data being stored differently, items being added, or some other break in the data pipeline. We could setup logging that detects these things and alerts us. It really depends on what things we think could break



Pipeline + Productionalization
· What problems / challenges would you see ?


Automating the creation of the model - 
Monitoring the model evaluation metrics + monitoring the actual impact on users
What is the meaning of the revenue groups and how can it help marketing target ads/campaigns
Doc


· How would you choose which data to integrate into the model and and how much of it?
If the data was huge you might have to start sampling instead of using all the data, or you might have to use HDFS and spark if it was necessary to have more data




