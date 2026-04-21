import subprocess

# দুটি ফাইলকে আলাদা প্রসেসে স্টার্ট করা
subprocess.Popen(["python", "bot.py"])
subprocess.Popen(["python", "otp_monitor.py"])

# মেইন থ্রেডকে চালু রাখা
while True:
    pass