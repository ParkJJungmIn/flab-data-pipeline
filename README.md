# 이벤트심 로그 분석 파이프라인


이벤트심이라는 오픈소스를 활용해, 대용량 로그를 생성하여 발생한 로그를 가지고 데이터 파이프라인을 구축한 프로젝트

---

## 프로젝트 설명

이 프로젝트는 대용량 로그 데이터를 생성한 후, 데이터 레이크에 적재하여 메달리언 아키텍처를 이용합니다. 메달리언 아키텍처를 활용함으로써 원시 데이터와 가공된 데이터를 효율적으로 분리하여 관리하여, 데이터 처리 과정에서의 유연성을 높이는 것을 기대하였습니다.

데이터 프로세싱 과정이 완료된 후에는, 결과 데이터를 OLAP(Online Analytical Processing) 시스템인 드루이드에 적재합니다. 드루이드를 사용함으로써 실시간 데이터 분석과 대규모 데이터셋에서도 빠른 쿼리 응답 시간을 제공됨으로써 사용자에게 대용량 데이터에 대해 실시간 분석을 수행할 수 있게 됩니다.

이러한 데이터 파이프라인은 데이터 오케스트레이션 도구인 에어플로우를 통해 구축되었습니다.

최종적으로, 슈퍼셋을 이용하여 완성된 데이터를 시각화하고 분석 결과를 이해하기 쉽게 표현하였습니다.

이 프로젝트는 대용량 로그 데이터를 효과적으로 처리하고 분석하여, 실시간 데이터 분석의 가능성을 확장하며, 복잡한 데이터 오케스트레이션과 시각화를 통해 깊이 있는 인사이트를 제공하는 과정을 구축해보았습니다.

### 아키텍쳐

<img width="738" alt="image" src="https://github.com/ParkJJungmIn/flab-data-pipeline/img/ar.png">


### 사용기술 및 툴

- Cloud - [**AWS**](https://aws.amazon.com/)
- Containerization - [**Docker**](https://www.docker.com),
- Data Processing - [**Spark**](https://spark.apache.org/)
- Orchestration - [**Airflow**](https://airflow.apache.org)
- Data Lake - [**AWS**](https://aws.amazon.com/)
- Data Serving - [**Druid**](https://druid.apache.org/)
- Data Visualization - [**SuperSet**](https://superset.apache.org/)
- Language - [**Python**](https://www.python.org)
- Infrastructure as Code [**Terraform**](https://www.terraform.io/)

### 대쉬보드

![streamify-2023-09-20T17-06-21 303Z](https://github.com/ParkJJungmIn/flab-data-pipeline/img/dashboard.png)

---

## 블로그



---

### etc

- [Eventsim](https://github.com/Interana/eventsim)