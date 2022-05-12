data(AirPassengers)
ap <- AirPassengers

ts(ap, frequency = 12, start = c(1949))
pdf("lab6_plot.pdf")
attributes(ap)
plot(ap)
dev.off()