# making 4X4 matrix
m <- c(1:16)
dim(m) <- c(4, 4)
m
print("Euclidean Distance Matrix of m: ")
dist(m, method = "euclidean")

print("Manhattan Distance Matrix of m: ")
dist(m, method = "manhattan")

print("Minkowski Distance Matrix of m: ")
dist(m, method = "minkowski")