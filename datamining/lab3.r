# ‘arules’ package provides the infrastructure for representing,
#  manipulating, and analyzing transaction data and patterns.
# ’arulesviz’ package is used for
# visualizing Association Rules and Frequent Itemsets
# ‘RColorBrewer‘ is a ColorBrewer Palette which
# provides color schemes for maps and other graphics.

# Loading Libraries
library(arules) # arules which implements the Apriori algorithm
library(arulesViz)
library(RColorBrewer)

# import dataset
data("Groceries") # in built data set in R


# using apriori() function
rules <- apriori(Groceries,
    parameter = list(supp = 0.01, conf = 0.2)
)

# using inspect() function

arules::inspect(rules[1:10]) # inspect() function prints the internal
# representation of an R object or the result of an expression.
# Here, it displays the first 10 strong association rules.

pdf("lab3_plot.pdf") # opening the graphical device
plot(rules, jitter = 0)
dev.off() # closing the graphics device