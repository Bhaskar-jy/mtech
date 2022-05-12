library(datasets)
head(iris)
data1 <- iris

# deleting species column
data1$Species <- NULL # nolint

head(data1)

result <- kmeans(data1, 3)
print("Result: ")
result
pdf("lab4_plot.pdf")
plot(iris[c("Petal.Length", "Petal.Width")], col = result$cluster)
dev.off()