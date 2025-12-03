# Cloud Security Posture Management (CSPM) Tool

A Python-based tool to **scan AWS cloud resources** for security misconfigurations, detect risks, and generate actionable findings. Designed to help security engineers, DevOps teams, and developers ensure their cloud infrastructure follows **best practices and least privilege principles**.

---

## Table of Contents

- [Features](#features)  
- [Supported Resources](#supported-resources)  
- [Getting Started](#getting-started)  
- [Usage](#usage)  
- [Scan Rules](#scan-rules)  
- [Sample Output](#sample-output)  


---

## Features

- ✅ Scan **EC2 instances** for public exposure and risky security groups  
- ✅ Detect **S3 buckets** with public access or missing encryption  
- ✅ Audit **IAM users** for missing MFA and active keys  
- ✅ Check **RDS databases** for public accessibility and encryption  
- ✅ Generate **human-readable findings** with recommended actions  
- ✅ Fully **JSON compatible** with AWS-style resource exports  

---

## Supported Resources

- **EC2** – Public IP detection, Security Group analysis, IAM roles  
- **S3** – Public ACLs, encryption status  
- **IAM** – MFA status, active/inactive keys  
- **RDS** – Public accessibility, storage encryption, backup retention  
- **Security Groups** – Open ports to `0.0.0.0/0`  

---

## Getting Started

### Prerequisites

- Python 3.8+  
- `json` module (built-in)  

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/cspm-tool.git
cd cspm-tool```

2. (Optional) Create a virtual environment:

```
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

### Usage

1. Place your AWS resource JSON export (mock or real) in the project folder, e.g., mock_aws_data.json.
2. Run the scanner:

```
from scanners.ec2_scanner import scan_ec2_public_access, scan_ec2_security_groups
import json

with open("mock_aws_data.json") as f:
    data = json.load(f)

# Scan for public EC2 instances
public_findings = scan_ec2_public_access(data)
for f in public_findings:
    print(f)

# Scan EC2 Security Groups
sg_findings = scan_ec2_security_groups(data)
for f in sg_findings:
    print(f)
```

### Scan Rules

- EC2 Public IP: Detect instances exposed to the internet
- EC2 Security Groups: Detect open ports to 0.0.0.0/0, especially SSH (22), RDP (3389), HTTP (80), DB ports
- S3 Buckets: Detect public ACLs and missing encryption
- IAM Users: Detect missing MFA and long-lived active access keys
- RDS Databases: Detect publicly accessible instances and missing storage encryption

### Sample Output

```
EC2 instance i-02eaee68 is publicly accessible. Please review and configure the security groups carefully to avoid unintended exposure.
EC2 instance i-02eaee68 has security group sg-5730 exposing port 80-80 to the entire internet (0.0.0.0/0). Please restrict the CIDR range.
S3 bucket bucket-12 is publicly readable. Enable encryption and review ACL settings.
IAM user user-5 does not have MFA enabled. Please enable MFA for enhanced security.
RDS instance db-2 is publicly accessible. Restrict access to VPC or trusted CIDRs.
```




