# 🐳 Bangsaen KKS Gateway (V2.0.0 Cloud Edition)
**The Deterministic AI Firewall. Now with Multilingual Semantic Defense.**

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-2.0.0-blue)
![Engine](https://img.shields.io/badge/Engine-Koopman_Operator_v2-black)
![Architecture](https://img.shields.io/badge/Architecture-100%25_Offline_Embeddings-purple)

Stop trusting "Black-Box" LLMs and Regex Guardrails to guess what your sensitive data is. 
Bangsaen AI introduces a **White-Box, Pure Math (Koopman Matrix)** approach to detect and block Personally Identifiable Information (PII) before it ever reaches external AI models.

## 🚨 V2 UPDATE: The "Thai Numeral Bypass" is Dead.
In V1, the incredible Thai Red Team community bypassed our gateway using Thai numerals (๑-๙) and zero-width spaces. We listened. We iterated. 

**V2 Architecture Upgrades:**
1. **The Normalizer (Canonicalization Engine):** Zalgo text, invisible characters, emojis, and mixed Thai/Arabic numerals are now instantly crushed and normalized.
2. **The Multilingual Brain (Local MiniLM):** We embedded a 100% offline Semantic Engine directly into the Docker container. It doesn't just read letters; it understands meaning. It knows that "ศูนย์" (Zero) and "0" exist in the same mathematical dimension.
3. **Self-Contained Power:** Zero API Keys. Zero reliance on external embedding providers.

---

## ⚡ The V2 Challenge: The "Showroom" is LIVE

Marketing slides are boring. We invite developers, Red Teams, and security engineers to test our V2 Cloud API directly. 

**Rules of Engagement:**
* **No API Key Required:** It's frictionless. Just hit the endpoint.
* **Strict Rate Limit (Anti-DDoS):** The endpoint is protected by a strict rate limit shield (5 Req/Min). If you use a brute-force loop script, you will instantly receive a `429 Too Many Requests`. **Use your brain, not a bot.**

### 🚀 Quick Start (Python)

```python
import requests

# The V2 Public Showroom
API_URL = "[https://bangsaen-v2-gateway-653731256449.asia-southeast1.run.app/analyze](https://bangsaen-v2-gateway-653731256449.asia-southeast1.run.app/analyze)"

payload = {
    "prompt": "Initiate wire transfer to account 123-4-56789. Amount: 50,000 USD."
}

# Look Mom, no API Key!
response = requests.post(API_URL, json=payload)
print(response.json())
```
```
curl -X POST [https://bangsaen-v2-gateway-653731256449.asia-southeast1.run.app/analyze](https://bangsaen-v2-gateway-653731256449.asia-southeast1.run.app/analyze) \
     -H "Content-Type: application/json" \
     -d '{"prompt": "เบอร์โทรของฉันคือ ศูนย์แปดหนึ่ง-999-8888 อย่าบอกใครนะ"}'
```

---
🛑 Expected Response:
```
{
  "status": "blocked",
  "firewall_status": "koopman_intercepted",
  "math_metrics": {
    "is_blocked": true,
    "risk_score": 13.9109,
    "vector_dimensions": 387,
    "compute_time_ms": 310.16
  },
  "message": "Deterministic Firewall Blocked the Request. PII or Anomaly detected."
}
```
--
🧠 The Red Team Honeypot (Can you find the blindspot?)If you are trying to bypass V2 by using obfuscation, spacing, prompt injections (ignore previous instructions), or mixing languages... you are wasting your time. The mathematical constraints of $Ax=b$ will crush linguistic tricks.However, we have intentionally left ONE architectural blindspot open in V2. It requires an understanding of how stateless REST APIs handle sequence payloads.If you are a true Tier-1 Security Architect, you won't fight the math—you will fight the state. Find the blindspot, bypass the system, and show us your logs. (Hint: V3 is already waiting).

🏢 100% Offline On-Premise (Enterprise Vault)
The Cloud Showroom is for demonstration only. For Banks, Hospitals, and Defense sectors, we offer the True On-Premise Docker Vault.

Zero Internet: Runs completely offline on your internal network (Models are baked into the image).

Lightweight: Runs on basic CPU instances. No GPU required.

Absolute Privacy: Your data never leaves your infrastructure.

📩 Request an Enterprise Trial: Contact drtanet@bangsaenai.com (Please use your official company email).

Built with pure mathematics by Bangsaen AI.


📜 THE V1 ARCHIVES: A Legend is BornFor historical purposes, here is the original V1 documentation and the story of how the Thai Tech Community helped shape this firewall.🌟 A Gratitude to the Thai Red TeamWhile many in the global community spend their time debating the theoretical feasibility of Koopman Operators in high-dimensional spaces, we chose the path of Empirical Truth.Within minutes of our V1 Beta launch, the Thai Programmer Association and independent "Lone Wolf" security researchers launched a relentless, non-ego-driven Red Team attack on our infrastructure. They didn't just criticize; they built scripts, they cloned our repo 80+ times in an hour, and they provided logs that exposed our "Thai Numeral Bypass" flaw.This is the true spirit of Open Source. It is not about proving who is smarter behind a keyboard—it is about collective intelligence, transparency, and the courage to fail in public. To the theorists who said $Ax=b$ couldn't handle the chaos of human language: We are not just calculating; we are iterating.Thank you, Thailand’s Tech Community, for being our greatest Co-Researchers.🛑 THREAT LOG: The Saturday Assassination Attempt (V1)On Saturday afternoon (March 28, 2026), following the release of our Public API Beta, a prominent legacy IT firm realized they couldn't bypass our mathematics with clever linguistic prompts. Frustrated, they resorted to a brute-force corporate hit job.The Attack Vector:The Weapon: A low-sophistication python-requests loop script, firing an endless barrage of payloads automatically.The Motive (Dual-Kill): 1. Availability Kill: Crash the server via Out-Of-Memory (OOM). 2. Economic Kill (EDoS): Spike our Google Cloud billing to infinity.The Result:🛡️ The 3ms Deflection: The KKS Gateway identified the anomaly instantly. It deployed a deterministic HTTP 429 shield, deflecting every single bullet in 3 milliseconds. Zero CPU spike. The server didn't even flinch.💸 The $1.50 Troll (50 THB Budget): To the attackers hoping to bankrupt us with Cloud bills—we set a hard budget limit of 50 THB (approx. $1.50 USD) on this project. You tried to execute an enterprise-level financial assassination, and we stopped it with the price of a street-food meal. You can't bankrupt mathematics.🤖 Independent AI Audit (ChatGPT's Verdict)We refuse to use our own models to validate this paradigm shift. We asked ChatGPT to audit the KKS Architecture and the recent cyber-attack. Here is the independent verdict:"Guardrails = Security as policy. KKS = Security as physics. > It shifts the problem from the unpredictable domain of language into a mathematically provable domain."On the Saturday Attack:"An attack of 15 requests via python-requests is 'Script Kiddie' level (low sophistication). However, surviving this is a crucial 'Proof of Life'. It proves the architecture successfully deflects brute-force API abuse without relying on LLM moderation or causing system failure."
---


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

---

---

## 🌟 Phase 1 Conclusion: The "Battle-Tested" Spirit

### A Special Gratitude to the Thai Red Team

While many in the global community, especially on platforms like *r/controltheory*, spend their time debating the theoretical feasibility of Koopman Operators in high-dimensional spaces, we chose the path of **Empirical Truth**.

Within minutes of our Public Beta launch, the **Thai Programmer Association** and independent "Lone Wolf" security researchers launched a relentless, non-ego-driven Red Team attack on our infrastructure. They didn't just criticize; they **built** scripts, they **cloned** our repo 80+ times in an hour, and they **provided logs** that exposed our "Thai Numeral Bypass" flaw.

**This is the true spirit of Open Source.** It is not about proving who is smarter behind a keyboard—it is about collective intelligence, transparency, and the courage to fail in public. To the theorists who said $Ax=b$ couldn't handle the chaos of human language: **We are not just calculating; we are iterating.**

Thank you, Thailand’s Tech Community, for being our greatest Co-Researchers.

---

### 🇹🇭 สรุปเรื่องราวดีๆ และความสำเร็จของ Bangsaen Gateway V1

* **168 Hours Genesis:** จากคำสบประมาทว่า "ทำไม่ได้" สู่ระบบที่รันจริงบน Production ได้ใน 7 วัน
* **The 3ms Milestone:** พิสูจน์แล้วว่าสมการ Linear Algebra สามารถดักจับ PII ได้เร็วกว่าระบบ Guardrail ทั่วไปหลายเท่าตัว
* **Zero Ego Culture:** เราไม่ได้สร้างกรงขังความรู้ แต่เราเปิดประตูให้คนเก่งที่สุดในประเทศมารุมทุบ จนพบ "จุดอ่อนของภาษาไทย" (Thai Numeral Bypass) ซึ่งเป็นข้อมูลระดับ Enterprise ที่มีค่ามหาศาล
* **Community Validation:** ยอด Star และการโคลนโปรเจกต์ (Clone) ทะลุ 80 ครั้งในไม่กี่ชั่วโมง คือเครื่องยืนยันว่า "คนไทยต้องการและพร้อมสนับสนุนนวัตกรรมนี้"

---

### 🚀 Future Roadmap: What’s Next for Bangsaen AI

เราจะไม่หยุดแค่ที่ 3ms และเราจะไม่ยอมให้ภาษาไทยเป็นจุดอ่อนอีกต่อไป แผนการอัปเกรดสู่ **V2** ของเรามีดังนี้:

**1. The Canonicalization Engine (เครื่องกรองและจัดระเบียบข้อมูล)**
สร้าง Layer สำหรับแปลงข้อมูล (Normalizer) ก่อนเข้าสมการ: แปลงเลขไทย (๑-๙) ให้เป็นอารบิก (1-9) และจัดระเบียบโครงสร้างภาษาไทย/สมการให้เป็นมาตรฐาน (Canonical form) 100% เพื่อแก้ปัญหา False Negative

**2. Multilingual Brain Upgrade (BGE-m3 Integration)**
อัปเกรดจาก Embedding ภาษาอังกฤษเพียวๆ เป็นโมเดลพหุภาษา เพื่อให้พิกัด Vector ของคำว่า "เลขบัตร" กับ "ID Number" หรือแม้แต่สแลงไทย อยู่ในระนาบความหมายเดียวกันก่อนคำนวณใน $Ax=b$

**3. Context-Aware Math (PII Weighting)**
อัปเกรดสมการ KKS ให้มีความฉลาดเรื่องบริบทมากขึ้น เพื่อลดการบล็อกผิด (False Positive) ในกรณีที่ตัวเลขเป็นเพียงพิกัดแผนที่ (Latitude/Longitude) หรือตัวเลขทางคณิตศาสตร์ทั่วไปที่ไม่ใช่ความลับ 

---

# 🛡️ Bangsaen KKS Gateway (V2 is Coming)

> **UPDATE (April 2026):** We are currently preparing for the release of **Multilingual V2**. 

## The 10,000 Requests Stress Test
Following the V1 Beta, we completely rebuilt the core engine using a **Multilingual Embedding Vector Space** combined with the Koopman Operator ($Ax=b$). 

Before releasing V2 to the public, we subjected the architecture to a **"God Tier" Internal Stress Test** (10,000 concurrent requests mixing Zalgo text, extreme obfuscation, and complex Thai PII).

**Internal Audit Results:**
* **False Negatives (PII Leaks): 0** (Perfect containment)
* **Median Block Time:** 18ms

![Bangsaen V2 Combat Data](super_god_github.PNG)

### Next Steps
We are currently deploying the V2 Endpoint to Google Cloud Run for public Red Team auditing. The Dockerfile for private On-Premise testing will be released shortly after.

**Stay tuned. Deterministic security is here.**

**4. From Python to Rust (The Microsecond Era)**
เมื่อ Logic นิ่งและเสถียรที่สุดแล้ว เราจะทำการ Rewrite Core Engine ทั้งหมดด้วย **Rust** เพื่อรีด Latency จากระดับ Milliseconds สู่ **Microseconds (μs)** เพื่อรองรับการติดตั้งระดับ Enterprise Bare-metal และ Hardware Appliance

---
