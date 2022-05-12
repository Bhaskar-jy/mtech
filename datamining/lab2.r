data1 <- read.csv("data1.csv", header = TRUE)
distance <- dist(data1, method = "euclidean")
print(distance)
hc <- hclust(distance, method = "complete")

pdf("lab2_plot.pdf")
plot(hc)
dev.off()