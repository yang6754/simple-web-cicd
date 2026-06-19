import subprocess
import sys

remote_host = "121.43.104.110"
remote_user = "root"
remote_pass = "hzxy,002517"

commands = [
    f"sshpass -p '{remote_pass}' ssh -o StrictHostKeyChecking=no {remote_user}@{remote_host} 'killall python3 2>/dev/null || true'",
    f"sshpass -p '{remote_pass}' ssh -o StrictHostKeyChecking=no {remote_user}@{remote_host} 'cd /opt/simple-web && python3 -c \"\nwith open(\\\"app.py\\\", \\\"r\\\") as f:\n    content = f.read()\ncontent = content.replace(\\\"port=8080\\\", \\\"port=80\\\")\ncontent = content.replace(\\\"debug=True\\\", \\\"debug=False\\\")\nwith open(\\\"app.py\\\", \\\"w\\\") as f:\n    f.write(content)\nprint(content[-200:])\n\"'",
    f"sshpass -p '{remote_pass}' ssh -o StrictHostKeyChecking=no {remote_user}@{remote_host} 'cd /opt/simple-web && nohup python3 app.py > /tmp/app.log 2>&1 &'",
    f"sshpass -p '{remote_pass}' ssh -o StrictHostKeyChecking=no {remote_user}@{remote_host} 'sleep 3 && netstat -tlnp | grep python'",
]

for cmd in commands:
    print(f"\n=== Running: {cmd[:50]}... ===")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    print("Return code:", result.returncode)
