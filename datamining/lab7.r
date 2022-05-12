library(caret) # The caret package (short for
# Classification And REgression Training) contains
# functions to streamline the model training process
# for complex regression and classification problems.
library(e1071) # e1071 is a package for R programming
# that provides functions for statistic and probabilistic
# algorithms like a fuzzy classifier, naive Bayes classifier,
# bagged clustering, short-time Fourier transform, support vector machine, etc..
test <- factor(c("cancer", "cancer", "cancer", "cancer", "cancer"))
levels(test) # display different values in test i,e cancer
final <- factor(c("cancer", "cancer", "cancer", "cancer", "normal"))
levels(final) # levels will be  cancer and normal
levels(test) <- c("cancer", "normal") # making the levels equals
confusionMatrix(final, test) # showing the accuracy in matrix format