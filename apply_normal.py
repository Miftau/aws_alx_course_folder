from normal_dist import Gaussian

normal_one = Gaussian(25, 10)
normal_two = Gaussian(15, 6)

summed_dist = normal_one + normal_two

print(normal_one.mean)
print(normal_one.stdev)

print(normal_two.mean)
print(normal_two.stdev)

print(summed_dist)

var = normal_one.calculate_var()
print(var)

data_set = [4, 4, 4]

normal_two.data = data_set

geo_mean = normal_two.calculate_geo_mean()

print(geo_mean)

mean = normal_two.calculate_mean()
print(mean)

harmonic = normal_two.calculate_harm_mean()
print(harmonic)


