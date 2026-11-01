import numpy as np

# ==========================================
# Task 4 - Part 1: File Writing & column_stack
# ==========================================

# 1. Read data from CSV
x_values = np.loadtxt('data.csv', delimiter=',')

# 2. Calculate sin, cos, tan
sin_x = np.sin(x_values)
cos_x = np.cos(x_values)
tan_x = np.tan(x_values)

# 3. Combine columns into a single 2D array
combined_data = np.column_stack((x_values, sin_x, cos_x, tan_x))

# 4. Save to result.txt with the required table format
np.savetxt('result.txt', combined_data, 
           fmt='%7d| %8.3f| %8.3f| %8.3f', 
           header='      x|   sin(x)|   cos(x)|   tan(x)\n-----------------------------------------', 
           comments='')

print("Part 1: 'result.txt' has been created successfully.\n")


# ==========================================
# Task 4 - Part 2: Statistics & argmax
# ==========================================

# 1. Read student data
data_std = np.loadtxt('DataStd.txt')

# 2. Separate IDs and Marks
student_ids = data_std[:, 0]  
marks = data_std[:, 1]        

# 3. Calculate statistics for marks
marks_min = np.min(marks)
marks_max = np.max(marks)
marks_mean = np.mean(marks)
marks_median = np.median(marks)
marks_std = np.std(marks)

# 4. Print statistics exactly as shown in the lab manual
print(f"Min: {int(marks_min)} | Max: {int(marks_max)} | Mean: {marks_mean:.2f}| Median: {marks_median:.2f}| Std: {marks_std:.4f}")

# 5. Find the index of the highest mark, then get the corresponding ID
max_index = np.argmax(marks)
best_student_id = student_ids[max_index]

print(f"the students ID with max mark : {best_student_id:.2f}")
