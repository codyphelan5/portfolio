import pywebio
import builtins


class Terminal:
    @staticmethod
    def cprint(message):
        builtins.print(message)

    @staticmethod
    def cinput(message):
        return builtins.input(message)


class Web:
    @staticmethod
    def cprint(message):
        pywebio.output.put_markdown(message)

    @staticmethod
    def cinput(message):
        return pywebio.input.input(message)


quiz = {
    1: {
        "question": "Your organization hosts an e-commerce web server. The server randomly\nexperiences a high volume of sales and usage from mid-November to the end of\nDecember, causing spikes in resource usage. These spikes have resulted in outages\nduring the past year.\n\nWhich of the following should be implemented to prevent these outages?",
        "choices": ("Stored procedures", "Scalability", "Version control", "Memory management"),
        "correct_answer": "B",
        "answer": "",
    },
    2: {
        "question": "Employees currently log in with their username and a password but management wants to increase\nlogin security by implementing smart cards. However, the IT department anticipates it will take a long time to purchase the necessary equipment and issue smart cards for everyone. You need to identify a solution that will provide comparable security until smart cards are implemented.\n\nWhich of the following is a compensating control that will meet these needs?",
        "choices": ("Implement an account lockout policy", "Increase password policy requirements", "Implement a TOTP solution", "Require users to change their passwords more often"),
        "correct_answer": "C",
        "answer": "",
    },
    3: {
        "question": "You have configured a firewall in your network to block ICMP traffic. You want to verify that it is working as expected.\n\nWhich of the following commands would you use?",
        "choices": ("arp", "ipconfig", "route", "ping"),
        "correct_answer": "D",
        "answer": "",
    },
    4: {
        "question": "You need to reboot a database server. Before doing so, you need to verify it doesn't have any active network connections.\n\nWhich of the following commands will BEST meet your needs?",
        "choices": ("arp", "ipconfig", "hping3", "netstat"),
        "correct_answer": "D",
        "answer": "",
    },
    5: {
        "question": "You are troubleshooting an issue with the *ycda* application hosted on a Linux system. You suspect that the issue is caused when performing a specific function. You execute the function and see a generic error message. You now want to view the detailed error logged in the messages file.\n\nWhich of the following commands would be the BEST choice to use?",
        "choices": ("head", "tail", "chmod", "logger"),
        "correct_answer": "B",
        "answer": "",
    },
    6: {
        "question": "Lisa is installing an application named *gcga.exe* on a Linux server. The documentation indicates \nthat the application should be installed with the following permissions:\n1.) The owner of the application should have read, write, and execute permissions.\n2.) The owner group of the application should have read and execute permissions.\n3.) All other users should not have any permissions for the application.\n\nWhich of the following commands should be used to meet these requirements?",
        "choices": ("chmod 067 gcga.exe", "chmod 661 gcga.exe", "chmod 760 gcga.exe", "chmod 770 gcga.exe"),
        "correct_answer": "C",
        "answer": "",
    },
    7: {
        "question": "Homer is not able to access any network resources from his Linux-based computer.\n\nWhich of the following commands would he use to view the network configuration of his system?",
        "choices": ("ifconfig", "ipconfig", "netstat", "tracert"),
        "correct_answer": "A",
        "answer": "",
    },
    8: {
        "question": "Management wants to increase security for any users accessing the network with a VPN. They plan to implement a method that will require users to install an application on their smartphones. This application will generate a key that they'll have to enter in addition to their username and password.\n\nWhat is the BEST description of this added authentication method?",
        "choices": ("Something you know", "Something you have", "Something you are", "Something you can do"),
        "correct_answer": "B",
        "answer": "",
    },
    9: {
        "question": "Users normally log on using a smart card, a username, and a password. Management wants administrators to use a third factor authentication.\n\nWhich of the following will meet this need?",
        "choices": ("Pin", "Token", "Fingerprints", "Push notification"),
        "correct_answer": "C",
        "answer": "",
    },
    10: {
        "question": "Developers are planning to develop an application using role-based access control.\n\nWhich of the following would they MOST likely include in their planning?",
        "choices": ("A listing of labels reflecting classification levels", "A listing of rules that the application must be able to trigger", "A listing of owners", "A matrix of functions matched with required privileges"),
        "correct_answer": "D",
        "answer": "",
    },
    11: {
        "question": "Your organization has implemented a system that stores user credentials in a central database. Users log on once with their credentials. They can access other systems in the organization without logging on again.\n\nWhich of the following does this describe?",
        "choices": ("Federation", "SAML", "SSO", "OAuth"),
        "correct_answer": "C",
        "answer": "",
    },
    12: {
        "question": "The Mapple organization is creating a help-desk team to assist employees with account issues. Members of this team need to create and modify user accounts and occasionally reset user passwords.\n\nWhich of the following is the BEST way to accomplish this goal?",
        "choices": ("Give each help-desk employee appropriate privileges individually.", "Add each member of the help-desk team to the administrator group within the domain.", "Add members of the help-desk team to a security group that has the appropriate privileges.", "Assign attributes to members of the help-desk team and give these attributes appropriate privileges."),
        "correct_answer": "C",
        "answer": "",
    },
    13: {
        "question": "Your organizations security policy states that administrators should follow the principle of least privilege.\n\nWhich of the following tools can ensure that administrators are following the policy?",
        "choices": ("Account audits", "Risk assessment", "Vulnerability assessment", "Threat assessment"),
        "correct_answer": "A",
        "answer": "",
    },
    14: {
        "question": "Lisa is responsible for managing and monitoring network devices, such as routers and switches, in your network.\n\nWhich of the following protocols is she MOST likely to use?",
        "choices": ("NAT", "SRTP", "SNMPv3", "DNSSEC"),
        "correct_answer": "C",
        "answer": "",
    },
    15: {
        "question": "Your organization recently landed a contract with the federal government. Developers are fine-tuning an application that will process sensitive data. The contract mandates that all computers using this application must be isolated.\n\nWhich of the following would BEST meet this need?",
        "choices": ("Create a bastion host in a screened subnet.", "Implement a boundary firewall.", "Create an air-gapped network.", "Implement an IPS"),
        "correct_answer": "C",
        "answer": "",
    },
    16: {
        "question": "Your organization wants to increase security for VoIP and video teleconferencing applications used within the network.\n\nWhich of the following protocols will BEST support this goal?",
        "choices": ("S/MIME", "TLS", "SFTP", "SRTP"),
        "correct_answer": "D",
        "answer": "",
    },
    17: {
        "question": "Your organization hosts a web server accessed from employees within the network, and via the internet. Management wants to increase its security. You are tasked with separating all web-facing traffic from internal network traffic.\n\nWhich of the following provides the BEST solution?",
        "choices": ("Screened subnet", "VLAN", "Firewall", "WAF"),
        "correct_answer": "A",
        "answer": "",
    },
    18: {
        "question": "Developers recently configured a new service on a server called GCGA1. GCGA1 is in a screened subnet and accessed by employees in the internal network, and by others via the internet. Network administrators modified firewall rules to access the service. Testing shows the service works when accessed from internal systems. However, it does not work when accessed from the internet.\n\nWhich of the following is MOST likely configured incorrectly?",
        "choices": ("The new service", "An ACL", "The GCGA1 server", "A VLAN"),
        "correct_answer": "B",
        "answer": "",
    },
    19: {
        "question": "Bart recently hooked up with a switch incorrectly causing a switching loop problem, which took down part of an organization's network. Management wants to implement a solution that will prevent this from occurring in the future.\n\nWhich of the following is the BEST choice to meet this need?",
        "choices": ("Flood guard", "SNMPv3", "SRTP", "RSTP"),
        "correct_answer": "D",
        "answer": "",
    },
    20: {
        "question": "A penetration tester has been hired to perform an assessment on the *greatadministrator.com* site. He used the nslookup command to perform some reconnaissance and received the following output:\nC: \\>nslookup -querytype=mx greatadministrator.com\nServer: Unknown\nAddress: 192.168.1.1\nNon-authoritative answer:\ngcgapremium.com MX preference = 20, mail exchanger = mk1.emailsrvr.com\ngcgapremium.com MX preference = 90, mail exchanger = mx2.emailsrvr.com\n\nOf the following choices, what BEST describes this output?",
        "choices": ("The server named *mx2.emailsrvr.com* is the primary email server for this domain.", "The server named *mx1.emailsrvr.com* is the primary email server for this domain.", "The AAAA record is misconfigured for this domain.", "The SOA record is hiding the IP address of the domain."),
        "correct_answer": "B",
        "answer": "",
    },
    21: {
        "question": "Which of the following is an example of a detective control?",
        "choices": ("An IPS reconfigured to monitor traffic instead of blocking it.", "A backup solution that includes off-site backups.", "Security guards", "A cable lock"),
        "correct_answer": "A",
        "answer": "",
    },
    22: {
        "question": "Your organization is planning to implement a wireless network using WPA2 Enterprise.\n\nOf the following choices, what is required?",
        "choices": ("An authentication server with a digital certificate installed on the authentication server.", "An authentication server with DHCP installed on the authentication server.", "An authentication server with DNS installed on the authentication server.", "An authentication server with WPS running on the access point."),
        "correct_answer": "A",
        "answer": "",
    },
    23: {
        "question": "Bart was in a coffee shop going through emails and messages on his smartphone. He then started receiving serval text messages promoting a political party and encouraging him to visit websites. After he left the coffee shop, he didn't receive any more messages.\n\nWhat does this describe?",
        "choices": ("Bluesnarfing", "Bluejacking", "Malware", "WPS attack"),
        "correct_answer": "B",
        "answer": "",
    },
    24: {
        "question": "Management within your organization wants employees to be able to access internal network resources from remote locations, including from their homes.\n\nWhich of the following is the BEST choice to meet this need?",
        "choices": ("NAC", "VPN", "IDS", "IPS"),
        "correct_answer": "B",
        "answer": "",
    },
    25: {
        "question": "Security experts want to reduce risks associated with updating critical operating systems.\n\nWhich of the following will BEST meet this goal?",
        "choices": ("Implement patches when they are released.", "Implement a change management policy.", "Use only trusted operating systems.", "Implement operating systems with secure configurations."),
        "correct_answer": "B",
        "answer": "",
    },
    26: {
        "question": "Your organization has a segmented network used to process highly classified material. Management wants to prevent users from copying documents to USB flash drives from any computer in this network.\n\nWhich of the following can be used to meet this goal?",
        "choices": ("DLP", "HSM", "COPE", "SED"),
        "correct_answer": "A",
        "answer": "",
    },
    27: {
        "question": "Your organization hosts an e-commerce website using a back-end database. The database stores product data and customer data, including credit card numbers.\n\nWhich of the following is the BEST way to protect the credit card data?",
        "choices": ("Full database encryption", "Full disk encryption", "Database column encryption", "File-level encryption"),
        "correct_answer": "C",
        "answer": "",
    },
    28: {
        "question": "The Springfield Nuclear Power Plant has created and maintains an online application used to teach the basics of nuclear physics. Only students and teachers in Springfield Elementary School can access this application via the cloud.\n\nWhat type of cloud service model is this?",
        "choices": ("IaaS", "PaaS", "SaaS", "XaaS"),
        "correct_answer": "C",
        "answer": "",
    },
    29: {
        "question": "Your organization has implemented a CYOD security policy. The policy mandates the use of security controls to protect the devices, and any data on them if they are lost or stolen.\n\nWhich of the following would BEST meet this goal?",
        "choices": ("Screen locks and GPS tagging", "Patch management and change management", "Screen locks and device encryption", "Full device encryption and XaaS"),
        "correct_answer": "C",
        "answer": "",
    },
    30: {
        "question": "Management within your company wants to implement a method that will authorize employee access to the network based on several elements. These elements include the employee's identity, location, the time of day, and the type of device used by the employee.\n\nWhich of the following will BEST meet this need?",
        "choices": ("Geofencing", "Containerization", "Tethering", "Context-aware authentication"),
        "correct_answer": "D",
        "answer": "",
    },
    31: {
        "question": "Personnel should be able to run the BizzFadd app from their mobile devices. However, certain features should only be operational when employees are within the company's property. When an employees leaves the property, access to these features should be blocked.\n\nWhich of the following answers provides the BEST solution to meet this goal?",
        "choices": ("Geofencing", "Geolocation", "GPS tagging", "Containerization"),
        "correct_answer": "A",
        "answer": "",
    },
    32: {
        "question": "A large city is using a SCADA system to manage a water treatment plant. City managers have asked IT personnel to implement security controls to reduce the risk of cybersecurity attacks against ICS's controlled by the SCADA system.\n\nWhich of the following security controls would be MOST relevant to protect this system?",
        "choices": ("DLP", "TPM", "FPGA", "NIPS"),
        "correct_answer": "D",
        "answer": "",
    },
    33: {
        "question": "IT auditors have found several unmanaged VMs in a network. They discovered that these were created by administrators for testing but weren't removed after testing was completed.\n\nWhich of the following should be implemented to prevent this in the future?",
        "choices": ("A policy related to VMs.", "A policy related to VM escape protection.", "A policy related to XaaS.", "A policy related to SDNs."),
        "correct_answer": "A",
        "answer": "",
    },
    34: {
        "question": "Jake recently launched an attack on a company website using scripts he found on the internet.\n\nWhich of the following BEST describes Jake as a threat actor?",
        "choices": ("Insider", "Hacktivist", "Script kiddie", "Shadow IT"),
        "correct_answer": "C",
        "answer": "",
    },
    35: {
        "question": "The Marvin Monroe Memorial Hospital recently suffered a serious attack preventing employees from accessing any computer data. The attackers scattered ReadMe files throughout the network that appeared on user screens. They indicated that the attackers encrypted all of the data, and it would remain encrypted until the attackers received a hefty sum as payment.\n\nWhich of the following identifies the MOST likely threat actor in this attack?",
        "choices": ("Criminal syndicate", "Ransomware", "Competitors", "Hacktivist"),
        "correct_answer": "A",
        "answer": "",
    },
    36: {
        "question": "Gil Gunderson, a salesperson in your organization, received an email on his work computer that included a malicious link. After clicking the link, his computer was infected with malware. The malware was not detected by antivirus software installed on his computer, the organization's email server, or the organization's UTM appliance. After infecting his computer, the malware then searched the network and encrypted data in all the network shares that Gil could access.\n\nWhich of the following BEST describes how this occurred?",
        "choices": ("The malware represents a zero-day exploit.", "The antivirus software indicated false positives.", "The malware infection was the result of a backdoor.", "The principle of least privilege was not implemented."),
        "correct_answer": "A",
        "answer": "",
    },
    37: {
        "question": "Logs on a web server show that it is receiving a significant number of SYN packets from multiple sources on the internet, but it isn't receiving the corresponding ACK packets.\n\nOf the following choices, what is the MOST likely source of these packets?",
        "choices": ("DDoS", "Ransomware", "Worm", "Bots"),
        "correct_answer": "D",
        "answer": "",
    },
    38: {
        "question": "Management recently mandated that computer monitors be repositioned to ensure they cannot be viewed from outside any windows. Additionally, users are directed to place screen filters over their monitors.\n\nWhat is the purpose of this policy?",
        "choices": ("Reduce success of phishing.", "Reduce success of shoulder surfing.", "Reduce success of dumpster diving.", "Reduce success of prepending."),
        "correct_answer": "B",
        "answer": "",
    },
    39: {
        "question": "Cody's supervisor told him to clean his desk to comply with the organization's clean desk space policy. While doing so, he threw several papers containing PII into the recycle bin.\n\nWhich type of attack can exploit this action?",
        "choices": ("SPIM", "Dumpster diving", "Shoulder surfing", "Tailgating"),
        "correct_answer": "B",
        "answer": "",
    },
    40: {
        "question": "Your organization's CFO recently received an email indicating the organization is being sued. More, the email names her specifically as a defendant in the lawsuit. It includes, an attachment described as a subpoena and encourages her to open it for more information.\n\nWhich of the following BEST describes the social engineering principle used by the sender in this scenario?",
        "choices": ("Whaling", "Phishing", "Authority", "Consensus"),
        "correct_answer": "C",
        "answer": "",
    },
    41: {
        "question": "Users are complaining about intermittent connectivity with a web server. After examining the logs, you identify a large volume of connection attempts from public IP addresses. You realize these connection attempts are overloading the server, preventing it from responding to other connections.\n\nWhich of the following is MOST likely occurring?",
        "choices": ("DDoS attack", "DNS poisoning attack", "Replay attack", "ARP poisoning attack"),
        "correct_answer": "A",
        "answer": "",
    },
    42: {
        "question": "An application on one of your database servers has crashed several times recently. Examining detailed debugging logs, you discover that just prior to crashing, the database application is receiving a long series of x90 characters.\n\nWhat is MOST likely occurring?",
        "choices": ("SQL injection", "Buffer overflow", "XML injection", "Zero-day"),
        "correct_answer": "B",
        "answer": "",
    },
    43: {
        "question": "Your organization recently experienced a significant data breach. After an investigation, cybersecurity professionals found that the initial attack originated from an internally developed application. Normally users can only access the application by logging on. However, the application allowed the attacker access to the application without requiring the attacker to log on.\n\nWhich of the following would have the BEST chance of preventing this attack?",
        "choices": ("Code review", "Backdoor", "DDoS protection", "Keylogger"),
        "correct_answer": "A",
        "answer": "",
    },
    44: {
        "question": "A software development process merges code changes from developers working on a project several times a day. It uses automation to validate the code and tracks changes using version control processes.\n\nWhich of the following BEST describes this process?",
        "choices": ("Continuous integration", "Continuous validation", "Continuous delivery", "Continuous monitoring"),
        "correct_answer": "A",
        "answer": "",
    },
    45: {
        "question": "Martin is performing a risk assessment. He is trying to identify the number of times a specific type of incident occurred in the previous year.\n\nWhich of the following BEST identifies this?",
        "choices": ("ALE", "ARO", "SLE", "RPO"),
        "correct_answer": "B",
        "answer": "",
    },
    46: {
        "question": "Lisa recently reviewed a security advisory. She's using it to review logs and looking for activity mentioned in the security advisory.\n\nWhich of the following BEST describes what she is doing?",
        "choices": ("Creating OSINT", "Threat hunting", "Penetration testing", "Performing reconnaissance"),
        "correct_answer": "B",
        "answer": "",
    },
    47: {
        "question": "You recently completed a vulnerability scan on your network. It reported that several servers are missing key operating system patches. However, after checking the servers, you've verified that the servers have these patches installed.\n\nWhich of the following BEST describes this?",
        "choices": ("False negative", "Misconfiguration on servers", "False positive", "Non-credentialed scan"),
        "correct_answer": "C",
        "answer": "",
    },
    48: {
        "question": "An external security auditor recently completed a security assessment. He discovered that a system has a vulnerability that two previous security assessments detected.\n\nWhich of the following BEST explains this?",
        "choices": ("The scanner is reporting a false negative.", "The vendor has not created a security patch.", "The scans ran as credentialed scans.", "The system is misconfigured."),
        "correct_answer": "B",
        "answer": "",
    },
    49: {
        "question": "Your organization regularly performs training in the form of a game mimicking an exercise. One team oversees the exercise, sets the rules, and identifies the rules of engagement. Another team uses known TTPs to exploit vulnerabilities within the rules of engagement. You are on a team dedicated to defending resources.\n\nWhich of the following BEST describes your role?",
        "choices": ("A member of the red team.", "A member of the blue team.", "A member of the purple team.", "A member of the white team."),
        "correct_answer": "b",
        "answer": "",
    },
    50: {
        "question": "You are running a vulnerability scanner with an access level that gives it the best chance of detecting vulnerabilities.\n\nWhich of the following BEST describes the type of scan you are running?",
        "choices": ("Non-credentialed scan", "A port scan", "A non-intrusive scan", "Credentialed scan"),
        "correct_answer": "D",
        "answer": "",
    },
    51: {
        "question": "You suspect that an attacker has been sending specially crafted TCP packets to a server trying to exploit a vulnerability. You decide to capture TCP packets being sent to this server for later analysis and you want to use a command-line tool to do so.\n\nWhich of the following tools will BEST meet your need?",
        "choices": ("TCPreplay", "TCPdump", "Netcat", "Wiredump"),
        "correct_answer": "B",
        "answer": "",
    },
    52: {
        "question": "Your company wants to control access to a restricted area of the building by adding an additional physical security control that includes facial recognition.\n\nWhich of the following provides the BEST solution?",
        "choices": ("Bollards", "Guards", "Retina scanners", "Cameras"),
        "correct_answer": "B",
        "answer": "",
    },
    53: {
        "question": "Thieves recently rammed a truck through the entrance of one of your organization's buildings in the middle of the night. They then proceeded to steal a significant amount of IT equipment.\n\nWhich of the following choices can prevent this from happening again?",
        "choices": ("Bollards", "Guards", "CCTV", "Alarms"),
        "correct_answer": "A",
        "answer": "",
    },
    54: {
        "question": "*Fileserver1* hosts several files accessed by users in your organization, and it's important that they can always access these files. Management wants to implement a solution to increase cybersecurity resilience.\n\nWhich of the following is the LOWEST cost solution to meet this requirement?",
        "choices": ("Active/active load balancing", "Active/passive load balancing", "RAID", "Warm site"),
        "correct_answer": "C",
        "answer": "",
    },
    55: {
        "question": "You need to identify and mitigate potential single points of failure in your organization's security operations.\n\nWhich of the following policies would be the BEST choice to help you find them?",
        "choices": ("A disaster recovery plan", "A business impact analysis", "Annualized loss expectancy", "Separation of duties"),
        "correct_answer": "D",
        "answer": "",
    },
    56: {
        "question": "Compu-Global-Hyper-Mega-Net hosts a website selling digital products. Marketing personnel have launched several successful sales. The server has been overwhelmed, resulting in slow responses from the server, and lost sales. Management wants to implement a solution that will provide cybersecurity resilience.\n\nWhich of the following is the BEST choice?",
        "choices": ("Managed PDUs", "Certificates", "Web application firewall", "Load balancing"),
        "correct_answer": "D",
        "answer": "",
    },
    57: {
        "question": "The backup policy for a database server states that the amount of time needed to perform backups should be minimized.\n\nWhich of the following backup plans would BEST meet this need?",
        "choices": ("Full backups on Sunday and full backups on the other six days of the week.", "Full backups on Sunday and differential backups on the other six days of the week.", "Full backups on Sunday and incremental backups on the other six days of the week.", "Differential backups on Sunday and incremental backups on the other six days of the week."),
        "correct_answer": "C",
        "answer": "",
    },
    58: {
        "question": "A security analyst is creating a document that includes the expected monetary loss from a major outage. She is calculating the potential impact on life, property, finances, and the organization's reputation.\n\nWhich of the following documents is she MOST likely creating?",
        "choices": ("BCP", "BIA", "MTBF", "RPO"),
        "correct_answer": "B",
        "answer": "",
    },
    59: {
        "question": "You are helping a risk management team update the business impact analysis for your organization. For one system, the plan requires an RTO of five hours and an RPO of one day.\n\nWhich of the following would meet this requirement?",
        "choices": ("Ensure the system can be restored within five hours and ensure it does not lose more than one day of data.", "Ensure the system can be restored within one day and ensure it does not lose more than five hours of data.", "Ensure the system can be restored between five hours and one day after an outage.", "Ensure critical systems can be restored within five hours and noncritical systems can be restored within one day."),
        "correct_answer": "A",
        "answer": "",
    },
    60: {
        "question": "Henry is updating the Business Impact Analysis (BIA) for your organization. He needs to document the time needed to return a database server to an operational state after a failure.\n\nWhich of the following terms would he use?",
        "choices": ("MTTR", "MTBF", "SLE", "ARO"),
        "correct_answer": "A",
        "answer": "",
    },
    61: {
        "question": "Lisa needs to transmit PII via email and she wants to maintain its confidentiality.\n\nWhich of the following choices is the BEST solution?",
        "choices": ("Use hashes.", "Encrypt it before sending.", "Protect it with a digital signature.", "Use RAID."),
        "correct_answer": "B",
        "answer": "",
    },
    62: {
        "question": "Employees in your organization recently received an email that appeared to come from your organization's CEO. The email mentioned that IT personnel were troubleshooting an authentication issue and needed employees to reply to the email with their credentials. Several employees responded with their credentials. This was a phishing campaign created for user training, and it spoofed the CEO's email. Executives want to ensure that employees have proof that any emails that appear to be coming from the executives, did come from them.\n\nWhich of the following should be implemented?",
        "choices": ("Digital signatures", "Spam filter", "Role-based training", "Heuristic-based detection"),
        "correct_answer": "A",
        "answer": "",
    },
    63: {
        "question": "As an administrator, you receive an antivirus alert from a server in your network indicating one of the files has a hash of known malware. The file was pushed to the server from the organization's patch management system and is scheduled to be applied to the server early the next morning. The antivirus software indicates that the file and hash of the malware on the server are:\n- File: gcga__upgrade.exe\n- Hash: bd64571e26035d95e5e9232b4aff b915\n\nChecking the logs of the patch management system, you see the following information:\nStatus: Update Name     Hash\nPushed: gcga_upgrade.exe      b815571e26035d95e5e9232b4aff48db\n\nWhich of the following indicates what MOST likely occurred?",
        "choices": ("The file was infected after it was pushed out to the server.", "The file was embedded with crypto-malware before it was pushed to the server.", "The file was listed in the patch management system's blacklist.", "The file was infected when the patch management system downloaded it."),
        "correct_answer": "A",
        "answer": "",
    },
    64: {
        "question": "Tony hid several plaintext documents within an image file. He then sent the image file to Louie.\n\nWhich of the following BEST describes the purpose of his actions?",
        "choices": ("To support steganography.", "To support integrity.", "To support resilience.", "To support obfuscation."),
        "correct_answer": "D",
        "answer": "",
    },
    65: {
        "question": "Cody and Jake need to exchange emails over the internet using a non-secure channel. These emails need to provide non-reputation. They decide to use certificates on each of their computers.\n\nWhat would they use to sign their emails?",
        "choices": ("CRL", "OCSP", "CSR", "DSA"),
        "correct_answer": "D",
        "answer": "",
    },
    66: {
        "question": "Administrators have noticed a significant amount of OCSP traffic sent to an intermediate CA. They want to reduce this traffic.\n\nWhich of the following is the BEST choice to meet this need?",
        "choices": ("Pinning", "Digital signatures", "Stapling", "Hashing"),
        "correct_answer": "C",
        "answer": "",
    },
    67: {
        "question": "A company is hosting an e-commerce site that uses certificates for HTTPS. Management wants to ensure that users can verify the validity of these certificates even if elements of the internet suffer an extended outage.\n\nWhich of the following provides the BEST solution?",
        "choices": ("OCSP", "PEM", "SAN", "CRL"),
        "correct_answer": "D",
        "answer": "",
    },
    68: {
        "question": "A security auditor discovered that several employees in the Accounting department can print and sign checks. In her final report, she recommended restricting the number of people who can print checks and the number of people who can sign them. She also recommended that no one should be authorized to both print and sign checks.\n\nWhich security policy does this describe?",
        "choices": ("Discretionary access control", "Rule-based access control", "Separation of duties", "Job rotation"),
        "correct_answer": "C",
        "answer": "",
    },
    69: {
        "question": "Bob recently resigned and left your organization. Later, IT personnel determined that he deleted several files and folders on a server share after he left the organization. Further, they determined that he did so during the weekend while the organization was closed.\n\nWhich of the following account management practices would have prevented his actions?",
        "choices": ("Onboarding", "Time-of-day restrictions", "Account audit", "Offboarding"),
        "correct_answer": "D",
        "answer": "",
    },
    70: {
        "question": "Your organization hired a third-party security professional to assess vulnerabilities. The security professional discovered a server was running an application that hasn't been updated for eight years. Management decided to keep the application online because there isn't a newer version from the vendor.\n\nWhich of the following BEST describes why the application doesn't have a newer version?",
        "choices": ("MSA", "AUP", "MSSP", "EOL"),
        "correct_answer": "D",
        "answer": "",
    },
    71: {
        "question": "A help-desk professional has begun to receive several calls from employees related to malware.\n\nUsing common incident response procedures, which of the following should be her FIRST response to these calls?",
        "choices": ("Preparation", "Identification", "Eradication", "Recovery"),
        "correct_answer": "B",
        "answer": "",
    },
    72: {
        "question": "Homer reported suspicious activity on his computer. After investigating, you verify that his computer is infected with malware.\n\nWhich of the following steps should you take NEXT?",
        "choices": ("Identification", "Preparation", "Containment", "Eradication"),
        "correct_answer": "C",
        "answer": "",
    },
    73: {
        "question": "Security personnel confiscated Louis's workstation after a security incident. Administrators removed the hard drive for forensic analysis but were called away to troubleshoot an outage before capturing an image of the drive. They left it unattended for several hours before returning to begin their analysis. Later, legal personnel stated that the analysis results would not be admissible in a court of low.\n\nWhat is the MOST likely reason for the lack fo admissibility?",
        "choices": ("Witnesses were not identified.", "A chain of custody was not maintained.", "An order of volatility was not maintained.", "A hard drive analysis was not complete."),
        "correct_answer": "B",
        "answer": "",
    },
    74: {
        "question": "Your organization is involved in a lawsuit, and a judge issue a court order requiring your organization to keep all emails from the last three years. Your data retention policy states that email should only be maintained from the previous 12 months. After investigating, administrators realize that backups contain emails from the last three years.\n\nWhat should they do with these backups?",
        "choices": ("Backups older than 12 months should be deleted to comply with the data retention policy.", "Backups for the last 12 months should be protected to comply with the legal hold.", "Backups for the last two years should be protected to comply with the legal hold.", "Backups for the last three years should be protected to comply with the legal hold."),
        "correct_answer": "D",
        "answer": "",
    },
    75: {
        "question": "Your database backup strategy includes full backups performed on Saturdays at 12:01 A.M. and differential backups performed daily at 12:01 A.M.\n\nIf they database fails on Thursday afternoon, how many backups are required to restore it?",
        "choices": ("1", "2", "3", "5"),
        "correct_answer": "B",
        "answer": "",
    },


}


score = 0
io = Web()
print = io.cprint
input = io.cinput


for question_number, question_data in quiz.items():
    print(f"{question_number}: {question_data['question']}")
    if isinstance(question_data["choices"], tuple):
        print("Chose from:")
        choice_number = 0
        for choice in question_data["choices"]:
            print(f"{chr(choice_number + 65)} : {choice}")
            choice_number += 1
    question_data["answer"] = input("Your answer: ")
    if question_data["answer"] == question_data["correct_answer"]:
        score += 1
        print("Correct")
    else:
        print("Incorrect")
    print("\n")

print(f"You scored {score}/75")
