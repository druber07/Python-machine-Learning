#Imports for use:
import numpy
from scipy import stats
import matplotlib.pyplot as plt


#Machine Learning: Lesson no.1
"""
    Mean - The average value
    Median - The mid point value
    Mode - The most common value
"""

def lesson1():
    speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

    print(numpy.mean(speed))
    print(numpy.median(speed))
    print(stats.mode(speed))



#Machine Learning: Lesson no.2
"""
    Standard deviation   A low standard deviation means that most of the numbers are close to the mean (average) value.
    (σ) - a number that describes how spread out the values are.
    A high standard deviation means that the values are spread out over a wider range.
"""
def lesson2_0():
    speed = [86,87,88,86,87,85,86]
    print(numpy.std(speed))
    # Meaning that most of the values are within the range of 0.9 from the mean value, which is 86.4.

    speed = [32,111,138,28,59,77,97]
    print(numpy.std(speed))
    # Meaning that most of the values are within the range of 37.85 from the mean value, which is 77.4.
    # As you can see, a higher standard deviation indicates that the values are spread out over a wider range.


"""
    Variance (σ^2)- another number that indicates how spread out the values are.
    In fact, if you take the square root of the variance, you get the standard deviation!
    Or the other way around, if you multiply the standard deviation by itself, you get the variance!
"""
def lesson2_1():
    speed = [86,87,88,86,87,85,86]
    print(numpy.var(speed))
    speed = [32,111,138,28,59,77,97]
    print(numpy.var(speed))




#Machine Learning: Lesson no.3
"""
    Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.
"""
def lesson3():
    ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
    print(numpy.percentile(ages, 75))
    ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
    print(numpy.percentile(ages, 90))




#Machine Learning: Lesson no.4
"""
    Data Distribution
        Earlier in this tutorial we have worked with very small amounts of data in our examples, just to understand the different concepts.
        In the real world, the data sets are much bigger, but it can be difficult to gather real world data, at least at an early stage of a project.

    How Can we Get Big Data Sets?
        To create big data sets for testing, we use the Python module NumPy, which comes with a number of methods to create random data sets, of any size.
""" 
def lesson4_0():
    #Create an array containing 250 random floats between 0 and 5:
    x = numpy.random.uniform(0.0, 5.0, 250)
    print(x)

"""
    Histogram - used to visualize the data set we can draw a histogram with the data we collected.
"""
def lesson4_1():
    #Create an array containing 250 random floats between 0 and 5:
    x = numpy.random.uniform(0.0, 5.0, 250)
    plt.hist(x, 5)
    plt.show()

"""
    Normal Data Distribution
        In the previous chapter we learned how to create a completely random array, of a given size, and between two given values.
        In this chapter we will learn how to create an array where the values are concentrated around a given value.
        In probability theory this kind of data distribution is known as the normal data distribution,
        or the Gaussian data distribution, after the mathematician Carl Friedrich Gauss who came up with the formula of this data distribution.
"""
def lesson4_2():
    x = numpy.random.normal(5.0, 1.0, 100000)
    plt.hist(x, 100)
    plt.show()
"""
We use the array from the numpy.random.normal() method, with 100000 values,  to draw a histogram with 100 bars.
We specify that the mean value is 5.0, and the standard deviation is 1.0.
Meaning that the values should be concentrated around 5.0, and rarely further away than 1.0 from the mean.
And as you can see from the histogram, most values are between 4.0 and 6.0, with a top at approximately 5.0.
"""



#Machine Learning: Lesson no.5
"""
    Scatter Plot - A scatter plot is a diagram where each value in the data set is represented by a dot.
"""
def lesson5_0():
    x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
    y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
    plt.scatter(x, y)
    plt.show()

def lesson5_1():
    x = numpy.random.normal(5.0, 1.0, 1000)
    y = numpy.random.normal(10.0, 2.0, 1000)

    plt.scatter(x, y)
    plt.show()