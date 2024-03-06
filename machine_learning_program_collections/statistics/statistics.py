import pandas as pd
import numpy as np
from scipy.stats import norm
from scipy.stats import uniform
from scipy.stats import expon
from scipy.stats import chi2_contingency
from scipy.stats import levene
from scipy.stats import f_oneway
from scipy import stats
from scipy.stats import f
import matplotlib.pyplot as plt
import seaborn as sns
import math


'''
The common method for identifying outliers in a dataset uses the Interquartile Range (IQR), 
which is the range between the first quartile (Q1) and the third quartile (Q3). However, the 
typical formula for defining outliers is as follows:

Any data point that is less than Q1 - 1.5*IQR is considered an outlier.
Any data point that is greater than Q3 + 1.5*IQR is considered an outlier.
The 1.5 factor in the formula can be adjusted depending on the situation, but 1.5 is a 
common choice and not 0.5 as your statement mentions. Therefore, the provided statement is incorrect.
'''

########################################################################

'''
Standard error Definition:--
The standard error (SE) is a statistical term that measures the accuracy with which a sample represents a 
population. In statistics, a random sample drawn from a population gives you many sets of random variables. 
The standard error of a statistic used to estimate a population parameter tells you how accurately your 
statistic estimates that parameter.

The standard error can be calculated as the standard deviation of the statistical measurement in your 
sample divided by the square root of the sample size:

SE = σ / sqrt(n)

where:

σ is the standard deviation of the sample.
sqrt(n) is the square root of the sample size.
If your data set is a full population (rather than a sample), the calculation for the standard deviation and 
the standard error are the same.
A small standard error indicates that the sample mean is a more accurate reflection of the actual population 
mean. A larger standard error indicates that the sample mean is less reliable as an estimate of the population mean.
'''

########################################################################
########################################################################
########################################################################
########################################################################


##################################################################
# # Sat score and probability density Function 
# sat_score  = pd.read_csv("./sat_scores.csv")
# # sat_score['score'] = sat_score['Verbal'] + sat_score['Math']

# mean = sat_score["score"].mean()
# sigma = sat_score["score"].std()
# print(f"The estimated mean is {round(mean,2)}")
# print(f"The estimated std is {round(sigma,2)}")

# density = pd.DataFrame()
# density["x"] = np.linspace(sat_score["score"].min() - 0.01, sat_score["score"].max() + 0.01, 100)
# density["pdf"] = norm.pdf(density["x"], mean, sigma) # Pdf is probability density function
# fig,ax = plt.subplots()
# sns.histplot(sat_score["score"], ax=ax, kde= True, stat="density")
# ax.plot(density["x"], density["pdf"], color="red")
# plt.title("Normal Distribution")
# plt.show()
##################################################################

# # norm.pdf example

# # Define the mean and standard deviation
# mu = 0
# std_dev = 1

# # Generate a range of values around the mean
# x = np.linspace(mu - 3*std_dev, mu + 3*std_dev, 100)
# print(x)

# # Compute the PDF of these values
# y = norm.pdf(x, mu, std_dev)

# # Plot the PDF
# plt.plot(x, y)
# plt.title('Normal Distribution PDF')
# plt.xlabel('x')
# plt.ylabel('Probability Density')
# plt.show()

##################################################################
# fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12,4))
# x = np.linspace(400,1600,1000)
# ax1.plot(x, norm.pdf(x, loc=1000, scale=200), color='b')
# ax1.set_title('Normal distribution of SAT Scores')
# ax1.set_xlabel('SAT Scores')
# ax1.set_ylabel('Probability')
# ax1.axvline(1350, ymax=0.23, linestyle = '--', color='green')
# x1 = np.linspace(1,36, 100)
# ax2.plot(x1, norm.pdf(x1, loc=20, scale=5), color='r')
# ax2.set_title('Normal Distribution of ACT Scores')
# ax2.set_xlabel('ACT Scores')
# ax2.set_ylabel('Probability')
# ax2.axvline(30, ymax = 0.18, linestyle='--', color='green')
# plt.show()

# # Find the Zscore for ACT and SAT exams
# top_sat = (1350-1200)/200
# print("the Z-Score of highest scorer in SAT among all the applicants", top_sat)

# top_act = (30-20)/5
# print("the Z-Score of highest scorer in ACT among all the applicants", top_act)

# fig, ax = plt.subplots()
# x = np.linspace(-4,4,50)
# ax.plot(x, norm.pdf(x, loc = 0, scale=1), color='b')
# ax.set_title('Standard Normal Distribution')
# ax.set_xlabel('Z-Scores')
# ax.set_ylabel('Probability')
# ax.axvline(top_sat, ymax=0.75, linestyle="--", color='green')
# ax.axvline(top_act, ymax=0.16, linestyle="--", color='black')
# plt.show()

##################################################################
# # Calculate the Z-score

# def normal_cdf(x, mean, stddev):
#   """
#   Returns the probability that a standard normal variable will be less than x.
#   """
#   return (1.0 + math.erf((x - mean) / (stddev * math.sqrt(2.0)))) / 2.0

# mean = 55000
# stddev = 6200

# low = 59000
# high = 67000

# z_low = (low - mean) / stddev
# z_high = (high - mean) / stddev

# print(f"Zscore for ${low} salary is {z_low}")
# print(f"Zscore for ${high} salary is {z_high}")

# probability = normal_cdf(high, mean, stddev) - normal_cdf(low, mean, stddev)

# print(probability)
##################################################################

# # Check how much data is covered by 1std, 2std and 3std
# '''
# The percentages you are referring to (67% and 95%) are related to the properties of the normal distribution. Specifically, they are derived from the empirical rule, or the 68-95-99.7 rule, which states that for a normal distribution:

# About 68% of the values lie within 1 standard deviation of the mean.
# About 95% of the values lie within 2 standard deviations of the mean.
# About 99.7% of the values lie within 3 standard deviations of the mean.
# This is a property of normal distributions specifically, and doesn't apply to all types of distributions.
# '''


# # Generate a random normal distribution
# data = np.random.normal(loc=0, scale=1, size=1000000)  # loc is the mean, scale is the standard deviation

# # Calculate the number of data points within 1, 2 and 3 standard deviations
# within_1_std = np.sum((data >= -1) & (data <= 1)) / len(data)
# within_2_std = np.sum((data >= -2) & (data <= 2)) / len(data)
# within_3_std = np.sum((data >= -3) & (data <= 3)) / len(data)

# print(f"Percentage within 1 std dev: {within_1_std * 100}%")  # Should be approximately 68%
# print(f"Percentage within 2 std dev: {within_2_std * 100}%")  # Should be approximately 95%
# print(f"Percentage within 3 std dev: {within_3_std * 100}%")  # Should be approximately 99%

##################################################################
# CLT in Action
# Central Limit Theorem

# np.random.seed(1)
# #creatimg a uniform distribution population of size 1000 000
# uniform_pop = uniform.rvs(0,10, size=1000000)

# plt.hist(uniform_pop)
# plt.title("Uniform Distribution POpulation")
# plt.xlabel("X~U(0,10)")
# plt.ylabel("Count")
# plt.show()

##################################################
# np.random.seed(1)
# uniform_pop = uniform.rvs(0,10, size=1000000)
# n=5
# sample_means = []
# # THIS IS USING THE     Uniform distribution
# for j in range(500):
#     sample = np.random.choice(uniform_pop, size=n)
#     sample_mean = np.mean(sample)
#     sample_means.append(sample_mean)

# sns.displot(sample_means, kde=True)
# # sns.displot(sample_means)
# plt.title("Distribution of Sample Means for n=" + str(n))
# plt.xlabel("Sample Mean")          
# plt.ylabel("count")
# plt.show()

##################################################################

# np.random.seed(1)

# # Create Normal distribution of population
# normal_pop = norm.rvs(0,1, size=1000000)

# # Uniform distribution
# # normal_pop = uniform.rvs(0,1, size=1000000)

# #Create an exponential distribution
# normal_pop = expon.rvs(0,1,size=1000000)

# plt.hist(normal_pop, 200)
# plt.title("Normal distribution Population")
# plt.xlabel("X~N(0,1)")
# plt.ylabel("Count")
# plt.show()

##################################################################
'''
code to collect sample means of
600 samples of size 50 from an exponential population?
The exponential population is generated using the code below:
'''

# from scipy.stats import expon
# exp_pop = expon.rvs(size = 100000)

# import numpy as np
# sample_means=[]
# for j in range(600):
#     sample = np.random.choice(exp_pop, size = 50)
#     sample_mean = np.mean(sample)   
#     sample_means.append(sample_mean) 

##################################################################

# sample = np.array([120,55,60,10,8,150,44,58,62,123])
# x_bar = np.mean(sample)
# print(x_bar)

##################################################################

# # Find the confidence interval with a given mean, std and the confidence percentage
# # for the 50 times coffee is dspensed from coffee machine

# x_bar, sigma = 110,7
# # n = 1
# n = 50

# # construct the confidence interval
# x = np.round(norm.interval(0.95, loc= x_bar, scale=sigma/np.sqrt(n)),2)
# print(x)

##################################################################

# x_bar, sigma = 1000, 200
# # n = 1
# n = 100

# # construct the confidence interval
# x = np.round(norm.interval(0.95, loc= x_bar, scale=sigma/np.sqrt(n)),2)
# print(x)
##################################################################
# Hypothesis Test for population Mean

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import scipy.stats as stats
# from scipy.stats import norm

# # Hypothesis is: Mean delivery time 5 days
# # Standard deviation:  1.3 days
# # Someone claiming that 5 day delivery time is wrong and its actually 5.25
# # Null hypothesis in this case would be deivery_time >5

# mu, sigma = 5, 1.3
# x_bar = 5.25
#                   # (Sample mean - populatin mean)/ sigma/sqrt(45)
# test_statistic = (x_bar - mu)/(sigma/np.sqrt(45))
# print(test_statistic)

# x = np.linspace(-4,4,100)
# plt.plot(x, norm.pdf(x,0,1))
# plt.axvline(x=test_statistic, c='r')
# plt.show()

# test_statistics_to_the_right = 1 - norm.cdf(test_statistic)

# # find the critical value
# critical_val = norm.pdf(1-0.5)

# x = np.linspace(-4,4,100)
# plt.plot(x,norm.pdf(x,0,1))
# plt.axvline(x= critical_val, c='r')
# x1 = np.linspace(critical_val,4,50)
# plt.fill_between(x1, norm.pdf(x1,0,1), color='r')
# plt.annotate("Reject Null",(2,0.2))
# plt.show()
##################################################################

'''
The code you provided performs a t-test to check if the scores of group 0 and group 1 
students are indeed different. The t-test is a statistical test that is used to compare 
the means of two independent groups. The output of the t-test is a t-statistic and a p-value. 
The t-statistic tells you how far apart the two means are, and the p-value tells you the 
probability of getting a t-statistic as extreme as the one you observed if the null hypothesis 
is true.
In this case, the t-statistic is -0.607695, and the p-value is 0.550986. The t-statistic is 
not very large, and the p-value is greater than 0.05, which is the standard threshold for 
statistical significance. Therefore, we cannot reject the null hypothesis that the means of the 
two groups are equal. In other words, there is not enough evidence to conclude that the scores of 
group 0 and group 1 students are indeed different.
Here is a breakdown of the output of the t-test:
statistic: The t-statistic, which is -0.607695.
pvalue: The p-value, which is 0.550986.
dtype: The data type of the output, which is float64.
I hope this helps! Let me know if you have any other questions.
'''

# # What is the p-value (rounded to two decimal places) returned by the following code?
# import scipy.stats as stats
# import numpy as np

# # scores of two groups (0 and 1) of students
# energ = np.array([[49, 0],[53, 1],[56, 1],[43, 1],[45, 1],[53, 1],[45, 1],[56, 1],[51, 0],[43, 0],[47, 1],[44, 0],[51, 0],[53, 1],[50, 0],[54, 0],[51, 0],[51, 1],[46, 0],[47, 1]])

# # Separating the data into 2 groups

# group1 = energ[:, 1] == 0 # Extracting the elements of the array where group == 0
# group1 = energ[group1][:, 0] # Extracting the scores of group 0 students
# group2 = energ[:, 1] == 1 # Extracting the elements of the array where group == 1
# group2 = energ[group2][:, 0] # Extracting the scores of group 1 students

# #applying t-test to check if the scores of group 0 and group 1 students are indeed different
# stats.ttest_ind(group1, group2, equal_var = False)

##################################################################
'''
What is the p-value (rounded to three decimal places) returned by the following code?
'''

# import scipy.stats as stats
# import numpy as np
# intake = np.array([[5260, 2400],[7500, 5500],[5640, 3885],[6180, 3160],[6390, 5645],[6515, 8680],[6805, 9265],[7515, 5975],[7515, 2790],[8230, 1900],[8770, 1335]])
# # Separating data into 2 groups

# pre = intake[:, 1] # Extracting the pre intake values from array
# post = intake[:, 0] # Extracting the post intake values from array

# x = stats.ttest_rel(post, pre, alternative = 'greater') # Applying T-test to check if the post intake is greater than pre intake
# print(x)

##################################################################

# p-value from proportions

# from statsmodels.stats.proportion import proportions_ztest
# test_stat, p_value = proportions_ztest(24,90, value=0.5, alternative='larger')
# print("The p-value is " + str(p_value))

##################################################################
'''
A Company sells computers and computer parts. The company claims that at least 90% of all orders are 
mailed within 72 hours after they are received. The quality control department at the company often 
takes samples to check if this claim is valid. A recently taken sample of 150 orders showed that 129 
of them were mailed within 72 hours.

Which of the following code is the most appropriate one to get the test statistic and p-value for 
the given data and below formulated hypothesis?

Null Hypothesis - Ho: p0 >= 0.90
Alternate Hypothesis - Ha : p0 < 0.90
'''

# from statsmodels.stats.proportion import proportions_ztest
# x = proportions_ztest(129, 150, value = 0.9, alternative = 'smaller')
# print(x)

# As the p-value is greater than 0.05, we can not reject the null hypothesis. Thus, there is not enough 
# statistical 
# evidence to say that the company's claim is true.

##################################################################

# p-value with proportions

# In Below we need to check if 20 defective bulb out of 200 is better than 25 defective bulb out of 400

# from statsmodels.stats.proportion import proportions_ztest

# defect_count = np.array([20,25])
# nobs = np.array([200,400])
# test_stat, p_value = proportions_ztest(defect_count, nobs)
# print(p_value)

##################################################################
'''
A survey is done on Indian college students to determine whether female students smoke less than male students. 
From the survey, we get that 40 out of 150 males smoke and 20 out of 100 females smoke. 
Which of the following snippet is the most appropriate one to get the p-value?
'''

# from statsmodels.stats.proportion import proportions_ztest
# x = proportions_ztest([20, 40], [100, 150], value = 0, alternative = 'smaller')
# print(x)

##################################################################

# Chi-square methods
# from scipy.stats import chi2

# def chi_var(pop_var, sample_var, n):
#     test_stat = (n-1) * sample_var /pop_var
#     p_value = 1 - chi2.cdf(test_stat, n-1)
#     return (test_stat, p_value)

# n = 32
# sigma_2, s_2 = 22.4**2, 26.4**2                  #22.4 is Null Hypothesis value, 26.4 is sample value
# test_stat, p_value = chi_var(sigma_2, s_2, n)     # n = 32 is number of observations
# print(p_value)

##################################################################
# # Test for equality of variances for two sample problem
# # Random Sampling from the population
# # In order to compare two test we need to do f-test

# bagweight = pd.read_csv('~/professional_courses/data_set/Bags1.csv')
# print(bagweight.head())

# def f_test(x,y):
#     x = np.array(x) 
#     y = np.array(y)
#     test_stat = np.var(x, ddof=1)/np.var(y, ddof=1) # Calculate F test statistics
#     dfn = x.size-1
#     dfd = y.size-1
#     p = (1-f.cdf(test_stat, dfn, dfd))
#     p1 = p*2
#     print("The p_value is {}".format(round(p,8)))

# f_test(bagweight.dropna()['Machine 1'], bagweight.dropna()['Machine 2'])


##################################################################
# # Chi-square test of independence for beverage

# beverage = pd.read_csv("~/professional_courses/data_set/Beverage.csv")
# print(beverage.head())

# chi, p_value, dof, expected = chi2_contingency(beverage.drop('Age', axis=1))
# print(p_value)

# # Here p-value is low, so Null hypothesis should hold, that means independence 
# # is rejected, which implies drinking beverage is related to age. This is from the beverage.csv dataset
##################################################################

# # What will be the appropriate null and alternative hypothesis for the above contingency table?

# #               Male        Female      Total
# # Smoker        120         100         220
# # Non-smoker	60	        140	        200
# # Total	        180	        240	        420
# # What will be the appropriate null and alternative hypothesis for the above contingency table?

# # H0: Smoking habit and gender are independent
# # Ha: Smoking habit and gender are not independent

# # We can use the below code to find this

# import pandas as pd
# from scipy.stats import chi2_contingency
# df = pd.DataFrame({'Male': [120, 60], 'Female': [100, 140]}, index = ['Smoker', 'Non-smoker'])
# chi2, pval, dof, exp_freq = chi2_contingency(df)
# print(pval)

##################################################################
# # Analysis of variance is a test of comparing means.
# # Its also called as ANOVA

# # Statistical test	What it is used for
# # ANOVA	Comparing the means of two or more groups
# # F-test	Comparing variances
# # t-test	Comparing the means of two groups
# # z-test	Comparing the mean of a sample to the mean of a population
# # Chi-square test	Comparing the distribution of a categorical variable to a theoretical distribution

# aovdata = pd.read_csv("~/professional_courses/data_set/AOVData.csv")
# print(aovdata.head())

# print(aovdata['fuel_type'].value_counts())
# print(aovdata.groupby("fuel_type")["co_emissions"].mean())

# fig, ax = plt.subplots(figsize = (6,6))
# a = sns.boxplot(x="fuel_type", y='co_emissions', data = aovdata, hue='fuel_type')
# a.set_title("Carbon Emission w.r.t Fuel type (3 levels)", fontsize=15)
# plt.show()

# ## Shapiro-wils Test
# w, p_value = stats.shapiro(aovdata['co_emissions'])
# print("The p-value is ", p_value)   # We cannot reject the NUll hypothesis becase the p-value is coming to be 0.4972


# ## Leven's Test
# statistic, p_value = levene(aovdata['co_emissions'][aovdata['fuel_type'] == "Petrol"],
#                             aovdata['co_emissions'][aovdata['fuel_type'] == "E85"],
#                             aovdata['co_emissions'][aovdata['fuel_type'] == "LPG"])
# print("levene- the p-value is", p_value)

# statistic, p_value = f_oneway(aovdata.loc[aovdata['fuel_type'] == "Petrol", 'co_emissions'],
#                             aovdata.loc[aovdata['fuel_type'] == "E85", 'co_emissions'],
#                             aovdata.loc[aovdata['fuel_type'] == "LPG", 'co_emissions'])
# print("f_oneway the p-value is", p_value)

# # Tukey HSD problem
# from statsmodels.stats.multicomp import pairwise_tukeyhsd

# m_comp = pairwise_tukeyhsd(endog = aovdata['co_emissions'], groups = aovdata['fuel_type'], alpha=0.05)
# print(m_comp)

##################################################################

##################################################################