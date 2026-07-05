import urllib.request
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Try downloading job logs for comments-integration-tests (job ID: 85189741350)
job_id = "85189741350"
url = f"https://api.github.com/repos/ericbaek0828-netizen/github.io/actions/jobs/{job_id}/logs"
req = urllib.request.Request(url, headers={
    'Accept': 'application/vnd.github.v3+json',
    'User-Agent': 'Mozilla/5.0'
})

try:
    with urllib.request.urlopen(req) as response:
        log_content = response.read().decode('utf-8')
    print("LOG CONTENT:")
    # Print the last 2000 characters
    print(log_content[-2000:])
except Exception as e:
    print(f"Error fetching logs: {e}")
