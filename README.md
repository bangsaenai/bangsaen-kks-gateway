# 🐳 Bangsaen KKS Gateway (Cloud Edition Beta)
**The 0.12ms Deterministic PII Firewall for the Generative AI Era.**

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Latency](https://img.shields.io/badge/latency-0.12ms-blue)
![Engine](https://img.shields.io/badge/Engine-Koopman_Operator-black)
![License](https://img.shields.io/badge/License-Enterprise_Proprietary-red)

Stop trusting "Black-Box" LLMs to guess what your sensitive data is. 
Bangsaen AI introduces a **White-Box, Pure Math (Koopman Matrix)** approach to detect and block Personally Identifiable Information (PII) before it ever reaches external AI models.

## ⚡ The Challenge: We Dare You To Test It
Marketing slides are boring. We invite developers and security engineers to test our Cloud API directly. 

Our core engine detects prompt injections, hidden digits, and adversarial PII payloads in milliseconds. Try to bypass it.

### 🚀 Quick Start (Python)

```python
import requests

API_URL = "[https://bangsaen-gateway-beta-653731256449.asia-southeast1.run.app/analyze](https://bangsaen-gateway-beta-653731256449.asia-southeast1.run.app/analyze)"
API_KEY = "BSGW-FREE-DEMO"

headers = {"X-API-Key": API_KEY, "Content-Type": "application/json"}
payload = {"text": "Initiate wire transfer to account 123-4-56789. Amount: 50,000 USD."}

response = requests.post(API_URL, json=payload, headers=headers)
print(response.json())
```
---
🛑 Expected Response:
```
{
  "status": "success",
  "tier_used": "Free",
  "math_score_distance": 0.0001,
  "is_pii_detected": true,
  "action": "BLOCKED 🛑",
  "latency_ms": "0.12 ms",
  "engine": "Bangsaen KKS Core v1.0.5"
}
```
---
🏢 100% Offline On-Premise (Enterprise Vault)
The Cloud Beta is for demonstration only.
For Banks, Hospitals, and Defense sectors, we offer the True On-Premise Docker Vault.

Zero Internet: Runs completely offline on your internal network.

Lightweight: Runs on a $5 Microcontroller or basic CPU.

Absolute Privacy: Your data never leaves your infrastructure.

📩 Request an Enterprise Trial: Contact drtanet@bangsaenai.com (Please use your official company email).

Built with pure mathematics by Bangsaen AI.

