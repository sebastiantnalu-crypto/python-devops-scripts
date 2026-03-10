import shutil

total, used, free = shutil.disk_usage("/")

percent = (used / total) * 100

print(f"Disk usage: {percent:.2f}%")

if percent > 80:
    print("WARNING: Disk usage high")
