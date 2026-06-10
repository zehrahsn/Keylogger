# Keylogger
Malware Creation and Detection Evasion Analysis 

The complete per-version breakdown TI tool's (Virustotal. Any.run, HybridAnalysis) raw output, indicators, and MITRE mappings is available in the full [report](https://medium.com/@hasanovazehra24/detection-evasion-in-malware-what-security-platforms-miss-327f09ff9d33?postPublishedType=repub) 
###PASSWORD to extract 7zip file: **Cyberslayers**

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

##Ethical Disclaimer
This project is for educational and defensive cybersecurity research only.
All testing was performed in a controlled and isolated virtual machine environment. The purpose of this work is to understand malware detection, sandbox analysis, and defensive security techniques.
This project must not be used to attack, monitor, infect, or collect data from any real user, system, or network without explicit authorization.


| File Name | Type | Description |
|---|---|---|
| plain.py | Plain Python Source Code | Original human-readable Python script generated for the lab |
| obfuscated.py | Obfuscated Python Source Code | Python script with the same functionality, but with encoded or restructured logic |
| compiled.exe | Windows Executable | Python source code compiled into a PE executable using PyInstaller |
| compressed.exe | Compressed Windows Executable | Compiled executable compressed with UPX |
| enc.exe | Encrypted Archive | Password-protected archive containing the executable |

The project started with a file called `plain.py`. This was the original Python source code generated for the lab. It was the simplest and most readable version because it was not hidden, packed, compressed, or converted into another format. Since it was a normal `.py` file, the code could be opened in a text editor and reviewed directly. This version was used as the baseline sample for comparing how later changes affected detection.

The second version was `obfuscated.py`. This was still a Python script, but the code was changed to make it harder to read and understand. For example, the readable logic could be hidden using encoding techniques such as Base64 or by restructuring the code. The file still worked like a Python script, but a person or scanner looking at it would not immediately see the clear logic. This version was used to test whether basic AI-assisted obfuscation changes how security tools detect the sample.

The third version was `compiled.exe`. In this stage, the Python script was converted into a Windows executable file using **PyInstaller**. Instead of running the file as a `.py` script through Python, it became a normal Windows `.exe` program. PyInstaller packages the Python code together with the required Python runtime and dependencies, so the file can run on Windows like a regular application. This version was useful because security tools often analyze executable files differently from plain source code.

The fourth version was `compressed.exe`. This version was created by taking the compiled `.exe` file and compressing it with **UPX**, which stands for Ultimate Packer for eXecutables. UPX reduces the file size and wraps the executable in a packed format. In simple terms, the program is still an executable, but its internal structure is compressed. This can make static analysis harder because security tools may need to unpack the file before they can properly inspect it. This version was used to see how packing and compression affect malware detection results.

The final version was `enc.7z`. This version placed the executable inside a password-protected encrypted archive using 7-Zip. In simple words, the file was locked inside an archive, and the content could not be fully inspected without the correct password. Because of this, security platforms may only see the outer archive instead of the actual executable inside it. This version was used to test how encryption affects static and dynamic analysis, especially when analysis tools cannot automatically extract the protected file. 

Overall, the lab compared five stages of the same sample: plain Python source code, obfuscated Python source code, PyInstaller-compiled executable, UPX-compressed executable, and password-protected 7-Zip archive. This helped show how each transformation changes what security tools can see and how confidently they can detect suspicious behavior.

##Ethical Disclaimer
This project is for educational and defensive cybersecurity research only.
All testing was performed in a controlled and isolated virtual machine environment. The purpose of this work is to understand malware detection, sandbox analysis, and defensive security techniques.
This project must not be used to attack, monitor, infect, or collect data from any real user, system, or network without explicit authorization.
