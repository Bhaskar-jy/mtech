write.csv(Your DataFrame,"Path to export the DataFrame\\File Name.csv", row.names = FALSE)

PDF
# Opening the graphical device
pdf("my_plot.pdf")

# Creating a plot
plot(rnorm(20))

# Closing the graphical device
dev.off() 

# Customizing the output
pdf("my_plot.pdf",         # File name
    width = 8, height = 7, # Width and height in inches
    bg = "white",          # Background color
    colormodel = "cmyk"    # Color model (cmyk is required for most publications)
    paper = "A4")          # Paper size

# Creating a plot
plot(rnorm(20))

# Closing the graphical device
dev.off() 

SVG
# SVG graphics device
svg("my_plot.svg")

# Code of the plot
plot(rnorm(20))

# Close the graphics device
dev.off() 