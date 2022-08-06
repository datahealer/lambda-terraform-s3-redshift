# Python, Pandas, Lambda, Terraform, S3, Parquet, Redshift

This example demonstrates creating a Lambda function in Python language and deploy it using Terraform. The example also demonstrates the use of Pandas, S3, Parquet & Redshift.

<table>
  <tr>
    <td>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png" width="30"/>
    </td>
    <td>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT01Ctpf3nRjz7b9l-om2h2llNA0jL4d_MVtXXXHVF5mWIn5nyMXLgzYscFGZdbhf_LN8M&usqp=CAU" width="30"/>
    </td>
    <td>
    <img src="https://upload.wikimedia.org/wikipedia/commons/8/89/Half-Life_lambda_logo.svg" width="30"/>
    </td>
    <td>
    <img src="https://www.terraform.io/img/docs/tfe_logo.png" width="30"/>
    </td>
    <td>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Amazon-S3-Logo.svg/1200px-Amazon-S3-Logo.svg.png" width="30"/>
    </td>
    <td>
    <img src="https://i0.wp.com/blog.contactsunny.com/wp-content/uploads/2020/04/parquet_logo.jpeg" width="30"/>
    </td>
    <td>
    <img src="https://www.clipartmax.com/png/middle/200-2001778_redshift-amazon-redshift-logo.png" width="30"/>
    </td>
  </tr>
</table>

## Requirements

- AWS Account : To create and use AWS services, you need to create an AWS account.
- AWS CLI : The AWS Command Line Interface (CLI) is a unified tool to manage your AWS services. With terminal commands, you can manage your AWS services. To install aws-cli, see [installing or updating the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).
- AWS Credentials : In order to manage your services from command line tools, you need an **aws_access_key_id** and **an aws_secret_access_key**. Creating a new user for IaC purposes is recommended. For this, you can create a new user with **IAM**. For this;

  1. Go to IAM
  2. Under Users click 'Add User'
  3. Give a. username (like terraform_user)
  4. For credential type select 'Access key - Programmatic access' and click next
  5. Click 'Create Group', specify a group name and select 'AdministratorAccess' policy.
  6. Click Review and create user. This user has a programmatic access and admin permissions.

  After you create the user, go to Users and select the user you have created. Go to 'Security Credentials' and click 'Create access key'. This will give an access key id and a secret access key. Save and dont share these credentials. You can not see access key again after you close this window.

  Once you have your credentials, open terminal and type:

  ```
  aws credentials
  ```

  Paste yur access key id, secret access key id. You can select a default region either.

- Terraform : For this project, you need to have Hashicorp Terraform, see [Download Terraform](https://www.terraform.io/downloads).On Mac, you can download with:
  ```
  brew tap hashicorp/tap
  brew install hashicorp/tap/terraform
  ```

## Project

- After you deploy this project, a Lambda function and an IAM role will be created in us-east-1 region. You can change AWS_REGION variable under **variables.tf** file. Under **provider.tf** file, you can see the AWS as provider.
- In **iam.tf**, 'lambda_role_s3' and 'lambda_policy' for Lambda function will be created. This is like creating a user and attach a policy with management console. lambda_role_s3 has full access for S3 and CloudWatch. You may wanna change this permissions under Statement for security purposes. You can check out [this site](https://awspolicygen.s3.amazonaws.com/policygen.html) to create AWS policies.
- **lambda.tf** file will create firstly a zip for .py file. Then it will create a Lambda function. Lambda function will have:
  - IAM role which is created from **iam.tf**
  - Project name which is defined in **variables.tf**
  - Script zip which is created **lambda.tf**
  - Runtime of Python 3.8
- After you set up credentials, go to terminal and start terraform with:
  ```
  terraform init
  ```
  This will install hashicorp/aws v3.74.1 and create a file called .terraform. You need to have ''Terraform has been successfully initialized!'' message.
  Before deployment, you can view the services which will be created with:
  ```
  terraform plan
  ```
  If everyting seems OK, start deployment. This will take apprx. 20 seconds.
  ```
  terraform apply
  ```
  Check the Lambda function from AWS management console.
