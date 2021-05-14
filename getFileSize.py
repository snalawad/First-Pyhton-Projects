import os.path
import os

totalSize = 0
for filename in os.listdir("C:\\Windows\\System32")
    totalSize = totalSize + os.path.getsize(os.path.join("C:\\Windows\\System32"))
print(totalSize)
