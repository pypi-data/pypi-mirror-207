# **DNA AUDIT TOOL** #

DNA Audit tool helps you to check whether the application built on AWS is following the AWS Well-Architected framework by validating it against
various AWS services security requirements and the best practices. Generates report to validate the security requirements and security best practices.

# **AWS Hardening Standards & Best Practices** #

https://codaglobal.atlassian.net/l/cp/UP1BxJTr

# **AWS Tagging Standards** #

https://codaglobal.atlassian.net/l/cp/oj0Ngsdb

# **AWS Naming Standards** #

https://codaglobal.atlassian.net/l/cp/s99nYLEC

# **Audit tool setup** #

**The project basically uses boto client to connect to the aws services.**

1. Update the session credentials in the terminal.

2. Specify the region name if you need to perform the audit for services in a specific region by mentioning the region name as argument while running the program.

3. If no region is specified us-east-1 is taken as default region and audit checks are performed for the services in us-east-1.

4. If you need to check tags. Update the Config.Json file by mentioning the tags in the account tags provided.


# **Audit Tool Execution** #

Creating Virtual Environment
```
python3 -m venv venv
```

Activating the virtual environment
```
source venv/bin/activate
```

Installing the dependencies in the virtual environment
```
pip install -r requirements.txt
```
Run the following command
```
python3 src/main.py --region {region_name}
```

# **Test Cases Execution** #

```
nosetests
```

# **Final Report** #

The overall report is provided as a HTML document.

## sample report ##
![Scheme](assets/sample_report_base.png)
![Scheme](assets/sample_report.png)
