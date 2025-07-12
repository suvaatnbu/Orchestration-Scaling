Orchestration-Scaling/
├── README.md
├── docs/
│   ├── architecture-diagram.png
│   ├── deployment-guide.md
│   ├── screenshots/
│   │   ├── jenkins-setup.png
│   │   ├── eks-cluster.png
│   │   └── helm-install.png
│   └── lambda-backup.md
├── helm/
├── eks-cluster.yaml
├── jenkins-boto3-scripts/
└── Jenkinsfile

# Jenkins + Boto3 Infrastructure Automation

## Build Jenkins with Python & Boto3

```bash
docker build -t custom-jenkins-boto3 .
```

## Run Jenkins

```bash
docker run -d \
  --name custom-jenkins \
  -p 8085:8080 -p 50000:50000 \
  -v jenkins_home:/var/jenkins_home \
  custom-jenkins-boto3
```

Access Jenkins at http://localhost:8085

Initial password:
```bash
docker exec custom-jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

## Jenkinsfile Pipeline

This Jenkinsfile clones your GitHub repo and runs boto3 scripts:
- vpc.py
- alb.py
- asg.py
- route53_alb.py
