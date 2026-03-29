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

API_URL = "https://bangsaen-gateway-beta-653731256449.asia-southeast1.run.app/analyze"
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

---
(Note: The public beta key is strictly rate-limited to 5 Req/Sec. If you are running a DDoS script and receiving HTTP 429 Too Many Requests, the system is working exactly as intended. Please upgrade to an Enterprise License for load testing.)

🌌 Phase 3: The Microsecond Era (Coming Soon)
A 3ms response time over the public internet is just a proof of concept.

The final form of the Bangsaen KKS Gateway is designed for On-Premise Bare-Metal C++ and FPGA hardware. Bypassing the network layer entirely, the latency collapses to the microsecond (μs) level—making it air-gapped, zero-latency AI security for Banks, Hospitals, and Defense.

💼 Enterprise Inquiries
Traditional AI filters are architecturally obsolete. If your organization requires absolute, mathematically provable PII protection, contact us for Enterprise Licensing and On-Premise / FPGA integration.

📧 Email: drtanet@bangsaenai.com

---

## 🛑 THREAT LOG: The Saturday Assassination Attempt

On Saturday afternoon (March 28, 2026), following the release of our Public API Beta, a prominent legacy IT firm realized they couldn't bypass our mathematics with clever linguistic prompts. Frustrated, they resorted to a brute-force corporate hit job.

**The Attack Vector:**
* **The Weapon:** A low-sophistication `python-requests` loop script, firing an endless barrage of payloads automatically.
* **The Motive (Dual-Kill):** 1. **Availability Kill:** Crash the server via Out-Of-Memory (OOM).
  2. **Economic Kill (EDoS):** Spike our Google Cloud billing to infinity.

**The Result:**
* 🛡️ **The 3ms Deflection:** The KKS Gateway identified the anomaly instantly. It deployed a deterministic HTTP 429 shield, deflecting every single bullet in **3 milliseconds**. Zero CPU spike. The server didn't even flinch.
* 💸 **The $1.50 Troll (50 THB Budget):** To the attackers hoping to bankrupt us with Cloud bills—we set a hard budget limit of **50 THB (approx. $1.50 USD)** on this project. You tried to execute an enterprise-level financial assassination, and we stopped it with the price of a street-food meal. **You can't bankrupt mathematics.**

---

## 🤖 Independent AI Audit (ChatGPT's Verdict)

We refuse to use our own models to validate this paradigm shift. We asked ChatGPT to audit the KKS Architecture and the recent cyber-attack. Here is the independent verdict:

> *"Guardrails = Security as policy. **KKS = Security as physics.*** > *It shifts the problem from the unpredictable domain of language into a mathematically provable domain."*

**On the Saturday Attack:**
> *"An attack of 15 requests via `python-requests` is **'Script Kiddie'** level (low sophistication). However, surviving this is a crucial **'Proof of Life'**. It proves the architecture successfully deflects brute-force API abuse without relying on LLM moderation or causing system failure."*

---

## ⏳ THE 48-HOUR ULTIMATUM

Since the local IT industry has failed to breach this mathematical wall and resorted to script-kiddie tactics, **we are closing the Public Beta Key in 48 HOURS.** We are pivoting entirely to the International Market and an Enterprise-Only Sandbox (requiring verified corporate emails). 

If you want to test the 3ms deterministic firewall, you have **48 hours left**. 
*(Note: Do not bother writing loop scripts to brute-force this endpoint. The HTTP 429 shield is active. You will only waste your own CPU).*

### Try It Now (Before it's gone)

🌐 Website: bangsaenai.com

Bangsaen AI Research Laboratory © 2026. All Rights Reserved.

