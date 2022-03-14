# AWS Resource Scanner

The AWS Resource Scanner make easily to scan to all provisioned aws resources.

It scan aws resources about related with specific service and you can see that at once on one output file.

❗ It does not include all information of resources, because it made for verify tasks of [worldskills](https://worldskills.org/).

# Quick Start

1. Download script
    ```
    git clone https://github.com/wsscc2021/aws-resource-scanner
    ```

2. Create virtual environment and install python packages
    ```
    cd aws-resource-scanner/
    python3 -m venv .venv
    source .venv/bin/activate
    pip3 install -r requirements.txt
    ```

3. Setting your aws credential and config
    - please ref for aws docs
        - [configure by credential files](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) 
        - [configure by environment](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html)

    - verify credential
        ```
        aws sts get-caller-identity
        ```
    - verify configured region
        ```
        aws configure get region
        ```

4. (Optional) Check to supported service
    ```
    python3 run.py --list
    ```

5. Run script
    ```
    python3 run.py vpc
    ```