# Keylogger
Malware Creation and Detection Evasion Analysis

The complete per-version breakdown TI tool's (Virustotal. Any.run, HybridAnalysis) raw output, indicators, and MITRE mappings is available in the full [report](https://medium.com/@hasanovazehra24/detection-evasion-in-malware-what-security-platforms-miss-327f09ff9d33?postPublishedType=repub) 

The lab investigates how different file transformations affect detection results, including plain Python source code, obfuscated Python code, compiled executables, compressed executables, and encrypted archives.

The keylogging module was tested by running the script inside the isolated VM while performing normal user input activity, such as typing text in different applications.

The captured keystrokes are written to a local log file. After the log file reaches the defined size 5Kb, the content is base64 encoded and transmitted to the lab listener  192.168.10.77:4444. 
Collected evidence during this stage includes:
 - Captured keystroke log output
 - Successful listener reception
 - Encoded payload transmission evidence
<img width="940" height="568" alt="image" src="https://github.com/user-attachments/assets/84545906-6a1d-4b37-b4a1-50c0ffec5017" />


The screenshot module is verified by allowing the script to run for at least 60 seconds in the VM, confirming that a desktop capture is taken, encoded, and transmitted to the listener at 192.168.10.77:5555.
Evidence collected during this stage included:
 - Screenshot capture confirmation
 - Listener receiving encoded image data
 - Successfully decoded VM desktop screenshot
<img width="940" height="441" alt="image" src="https://github.com/user-attachments/assets/b6e17ea2-0913-4299-956a-42277f088dc6" />
