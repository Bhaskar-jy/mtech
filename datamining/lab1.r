# x1 dataset
x1 <- c(1, 1.5, 3, 4, 3)
# x2 dataset
x2 <- c(1, 1.5, 5, 4, 3.5)

pdf("lab1_plot.pdf")
# scatter plot
plot(x1, x2)
# histogram
hist(x1)
hist(x2)
# box plot
boxplot(x1)
boxplot(x2)
# mean
x1_mean <- mean(x1)
x2_mean <- mean(x2)
# standard deviation
x1_sd <- sd(x1)
x2_sd <- sd(x2)
# combine dataset
cbind(x1, x2)
sprintf("Mean of X1: %f", x1_mean)
sprintf("Mean of X2: %f", x2_mean)
sprintf("Standard Deviation of X1: %f", x1_sd)
sprintf("Standard Deviation of X2: %f", x2_sd)
dev.off()