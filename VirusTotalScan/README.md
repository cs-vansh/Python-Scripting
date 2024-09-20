# VirusTotalScan

**Note : Do not solely rely on this tool for security assessments. Check the GUI for the community page and consult other sources to ensure safety.**

This Python script utilizes the VirusTotal API to perform scans on a list of IP addresses. The goal is to detect and analyze potential security threats associated with these IPs. The script retrieves information such as the number of detections and scan dates, and outputs the results to a CSV file for any further analysis.

## Prerequisites

1. **VirusTotal API Key:**
   - Obtain a VirusTotal API key by signing up on the [VirusTotal website](https://www.virustotal.com/).
   - Put your API key in the script:
        ```python
        API_KEY='...'		#Set up an api_key to get results.

        ``` 

2. **Dependencies:**
   - Install the required Python libraries using the following:
     ```bash
     pip install requests
     pip install beautifulsoup4
     ```

## Usage

1. Update the `API_Key` and the `ips_to_scan` list with the IP addresses to investigate.
   ```python
   ips_to_scan = ['zzz.zzz.zzz.zzz','yyy.yyy.yyy.yyy'] 	# IPs to scan 
   ```

3. Run the script:
    ```bash
    python ip_scan.py
    ```

4. The script will output the results to a CSV file named `ip_scan_results.csv`.

## Output Format

The CSV file contains the following columns:

- `IP`: The IP address under investigation.
- `Detection Count`: Total number of detections associated with the IP.

The `Detection Count` is represented as a list of dictionaries, where each dictionary includes:
- `date`: The date and time of the scan result.
- `positives`: The number of antivirus engines that detected a positive (malicious) result.
- `total`: The total number of antivirus engines used in the scan.
- `sha256`: The SHA256 hash associated with the specific scan result.

Each row in the CSV file corresponds to a specific IP address, providing a summary of the detection count and scan date.

A sample CSV file showing results:
![Screenshot 2023-11-12 213527](https://github.com/cs-vansh/VirusTotalScan/assets/104628209/fc03b942-8754-4048-b1bf-8b1c34e93594)

