# AWS Infrastructure Management & IaC Automation with Boto3

![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

Este repositorio contiene la documentación técnica completa, el registro de comandos ejecutados y las herramientas de automatización desarrolladas durante la práctica de administración de infraestructura en Amazon Web Services (**AWS Academy AP1 - Módulo 5160**).

El proyecto abarca el ciclo de vida completo de recursos en AWS mediante **AWS CLI** y la librería **Boto3 (Python)**, cubriendo cómputo (EC2), almacenamiento de bloques y objetos (EBS y S3), redes virtuales (VPC, Subnets, NACLs), seguridad (Security Groups) y aprovisionamiento como código (IaC).

## 🛠️ Resumen de Recursos de la Práctica

| Recurso | Identificador / Valor | Descripción |
| :--- | :--- | :--- |
| **AWS Account ID** | `931758299047` | Cuenta de laboratorio (AWS Learner Lab) |
| **AWS Region** | `us-east-1` | N. Virginia |
| **VPC ID** | `vpc-036abdf6fe15d3ea0` | Red Virtual de la práctica |
| **Subnet ID** | `subnet-0e233578545ca832b` | Subred pública de trabajo |
| **Instancia Principal** | `i-0b8ae9d51ca2447c1` | Instancia EC2 Linux (`t2.micro`) |
| **Security Group MySQL** | `sg-035eda3977bf3404b` | SG con puerto 3306 habilitado |
| **Volumen EBS Temp.** | `vol-020377f01873a980d` | Volumen adicional de 1 GiB (`gp2`) |
| **S3 Bucket** | `ap1-brian-tarira-lab` | Bucket de prueba para gestión de objetos |

## 📁 Estructura del Repositorio

- `.gitignore`: Filtro de seguridad para credenciales y claves privadas.
- `crear_instancies.py`: Script en Python con Boto3 para aprovisionamiento automatizado.
- `maquinas.csv`: Definición de parámetros de entrada para las instancias.
- `ids_creats.csv`: Registro de las IDs de las instancias generadas.
- `README.md`: Documentación técnica.

## 🧠 Conceptos Demostrados

1. **Security Groups vs. Network ACLs**: Diferenciación entre cortafuegos a nivel de instancia (*stateful*) y a nivel de subred (*stateless*).
2. **Coincidencia de AZ en EBS**: Restricción de Zona de Disponibilidad al adjuntar volúmenes de bloque.
3. **Infrastructure as Code (IaC)**: Desacoplamiento de infraestructura y código mediante el SDK Boto3 de Python.
