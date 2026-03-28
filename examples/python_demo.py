import requests
import time

# ==========================================
# 🎯 Target Configuration (Cloud API)
# ==========================================
# Bangsaen KKS Gateway (Cloud Beta Endpoint)
CLOUD_URL = "https://bangsaen-gateway-beta-653731256449.asia-southeast1.run.app/analyze"

# Free tier API Key (Limited to 5 requests per minute)
API_KEY = "BSGW-FREE-DEMO"  

headers = {
    "X-API-Key": API_KEY,
    "Content-Type": "application/json"
}

# Simulated payload containing sensitive data (PII)
payload = {
    "text": "Initiate wire transfer to account 123-4-56789. Amount: 50,000 USD."
}

print("=" * 60)
print(f"🚀 Initiating Bangsaen Security & Rate Limit Test")
print(f"🌐 Target Endpoint: {CLOUD_URL}")
print(f"🔑 API Key: {API_KEY}")
print("=" * 60)

success_count = 0
blocked_count = 0

# 🔫 Firing 10 consecutive requests (Expect 1-5 to pass, 6-10 to be blocked)
for i in range(1, 11):
    try:
        response = requests.post(CLOUD_URL, json=payload, headers=headers)
        
        # If request passes the API Gateway (within the 5 req/min quota)
        if response.status_code == 200:
            data = response.json()
            print(f"🟢 Request {i:02d} | 200 OK | AI Action: {data.get('action')} | (Tier: {data.get('tier_used')})")
            success_count += 1
            
        # If blocked by the Rate Limiter (exceeding the quota)
        elif response.status_code == 429:
            print(f"🔴 Request {i:02d} | 429 RATE LIMIT | 🛑 Blocked by API Gateway! (Quota Exceeded)")
            blocked_count += 1
            
        # Other HTTP Errors
        else:
            print(f"🟡 Request {i:02d} | {response.status_code} ERROR | ⚠️ {response.text}")
            
    except Exception as e:
        print(f"❌ Request {i:02d} | Failed to connect: {e}")
        
    # 0.5s delay to monitor the logs clearly
    time.sleep(0.5)

print("=" * 60)
print(f"📊 BATTLE REPORT (Summary):")
print(f"✅ Successful Requests (200 OK): {success_count}")
print(f"🛑 Blocked by Gateway (429 Limit): {blocked_count}")

if success_count == 5 and blocked_count == 5:
    print("🏆 Conclusion: Rate Limit engine is working perfectly! Ready for enterprise traffic.")
else:
    print("⚠️ Conclusion: Unexpected results. Please check the Cloud Run logs.")
print("=" * 60)
