library("party")
a <- c(1:50)
cb <- data.frame(cbind(a))
t <- ctree(a ~ ., data = cb)
pdf("lab9_plot.pdf")
plot(t)
dev.off()
t