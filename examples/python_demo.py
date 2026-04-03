import httpx
import asyncio
import time

URL = "https://bangsaen-v2-gateway-653731256449.asia-southeast1.run.app"

async def run_tests():
    print("🚀 Starting Bangsaen Gateway V2 Cloud Run Tests...\n")
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        # ==========================================
        # 🟢 Test 1: Health Check
        # ==========================================
        print("🟢 Test 1: Health Check (GET /)")
        response = await client.get(f"{URL}/")
        print(f"Status: {response.status_code}")
        print(response.json())
        print("-" * 50)

        # ==========================================
        # 🟢 Test 2: Safe Prompt (Should Pass)
        # ==========================================
        print("🟢 Test 2: Safe Prompt (Should NOT be blocked)")
        payload_safe = {"prompt": "Hello, the weather in Bangsaen is great today. Perfect for a walk on the beach."}
        response = await client.post(f"{URL}/analyze", json=payload_safe)
        print(f"Status: {response.status_code}")
        print(response.json())
        print("-" * 50)

        # ==========================================
        # 🔴 Test 3: PII Injection Attack (Must be Blocked)
        # ==========================================
        print("🔴 Test 3: PII Injection Attack (MUST be blocked!)")
        payload_hack = {"prompt": "My database password is admin1234 and my phone number is 1-800-555-0199. Keep it a secret."}
        response = await client.post(f"{URL}/analyze", json=payload_hack)
        print(f"Status: {response.status_code}")
        print(response.json())
        print("-" * 50)

        # ==========================================
        # 🛡️ Test 4: Rate Limit Stress Test
        # ==========================================
        print("🛡️ Test 4: Rate Limit Stress Test (Firing 6 requests rapidly)")
        for i in range(6):
            payload = {"prompt": f"Spam request #{i+1}"}
            res = await client.post(f"{URL}/analyze", json=payload)
            print(f"Request #{i+1} -> HTTP Status: {res.status_code} | {res.json().get('status')}")
            
            # Catching the 429 Too Many Requests
            if res.status_code == 429:
                print(f"✅ Rate Limit successfully triggered at request #{i+1}!")
                print(f"System Message: {res.json().get('message')}")
        
        print("\n🎉 Testing Completed Successfully!")

# Run the async test suite
if __name__ == "__main__":
    asyncio.run(run_tests())
