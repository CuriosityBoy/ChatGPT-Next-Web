import requests

def trigger_netlify_deploy():
    webhook_url = "https://api.netlify.com/build_hooks/6651f5499c181f5a768e1573"
    response = requests.post(webhook_url)
    if response.status_code == 200:
        print("Netlify deploy triggered successfully!")
    else:
        print("Failed to trigger Netlify deploy.")

trigger_netlify_deploy()
