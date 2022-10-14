"""
Checks if the serpentines we characterized are good for what we want to achieve.
!!! ONLY run this program after reading Optimus surrogate analysis successfully and making sure the obj_req_lin_str.p file in constraintSatisfaction is validated.
"""
import pickle

obj_req_lin_str = pickle.load(open("../constraintSatisfaction/obj_req_lin_str.p", "rb"))
max_linear_stretch = 16.66  # This stretchability is achieved by 10-leg, 1.55mm NTN_Half model. This value to increase if we achieve better models.

sorted_lin_str = sorted(obj_req_lin_str, reverse=True)

print("5 maximum required stretches are: " + str(sorted_lin_str[0:5]))
if sorted_lin_str[0] < max_linear_stretch - 1:
	print("We should be able to find good serpentines for our requirements")
else:
	print(
		"The design is clearly too large for what we have. Scale down or change the objective node requirements and/or design better serpentines.")
