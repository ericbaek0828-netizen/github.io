import urllib.request, json, zipfile, io

url = 'https://api.github.com/repos/ericbaek0828-netizen/github.io/actions/runs/29155496902/logs'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        with zipfile.ZipFile(io.BytesIO(response.read())) as z:
            for filename in z.namelist():
                if 'Deploy' in filename or 'Build' in filename or 'Install' in filename:
                    print(f'\n--- {filename} ---')
                    content = z.read(filename).decode('utf-8', errors='replace')
                    lines = content.split('\n')
                    print('\n'.join(lines[-50:])) # print last 50 lines
except Exception as e:
    print('Error:', e)
