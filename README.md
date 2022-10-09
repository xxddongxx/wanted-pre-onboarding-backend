# wanted_pre_onboarding_backend

## 요구사항 목록
> 1. 채용공고 등록
> 2. 채용공고 수정
> 3. 채용공고 삭제
> 4. 채용공고 목록(채용공고 검색 기능)
> 5. 채용상세 페이지(해당 회사가 올리 다른 공고)
> 6. 사용자 채용공고 지원(사용자는 1회지원 가능)

## DB Table 구성
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194763208-7b5f7941-dbd0-4b3c-b21e-52d5caf0fd31.png" width="70%" height="auto"/></p>


## 요구사항 API
### 채용공고 API
|Mtehod|API|Action|
|:---:|---:|---:|
|GET|/api/jobpost/|모든 채용공고 조회|
|GET|/api/jobpost/ID/|특정 채용공고 조회|
|POST|/api/jobpost/|새 채용공고 추가|
|PUT|/api/jobpost/ID/|특정 채용공고 갱신|
|DELETE|/api/jobpost/ID/|특정 채용공고 삭제|

### 1. 채용공고 등록
> POST /api/company/
<details>
<summary>채용공고 등록</summary>
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194767953-7250cad9-7dcc-48dd-996b-cc0c17af1476.png" width="70%" height="auto"/></p>
</details>

### 2. 채용공고 수정
> PUT /api/company/id/
<details>
<summary>채용공고 수정</summary>
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194768077-802e5470-c13f-44c8-8893-aa5f1ae86601.png" width="70%" height="auto"/></p>
</details>

### 3. 채용공고 삭제
> DELETE /api/company/id
<details>
<summary>채용공고 삭제</summary>
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194768122-6191e769-8715-422d-bb27-656be8b7009b.png" width="70%" height="auto"/></p>
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194768126-6149182c-9c04-42bb-9bad-94a011215c3b.png" width="70%" height="auto"/></p>

</details>

### 4. 채용공고 목록
> GET /api/company
<details>
<summary>채용공고 목록</summary>
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194767904-65203b32-d559-4604-8a65-089ec3f1944c.png" width="70%" height="auto"/></p>
</details>

### 4.1 채용공고 검색
> GET /api/search/?search=keyowrd
<details>
<summary>채용공고 검색</summary>
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194768293-f3cbd6af-8455-4e03-8ecd-e674e866c9ed.png" width="70%" height="auto"/></p>
</details>

### 5. 채용공고 상세 페이지(해당 회사가 올린 다른 공고)
> GET /api/company/id/
<details>
<summary>채용공고 상세 페이지</summary>
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194768489-94d0bb10-a55c-4d70-a2f9-0afbe128f058.png" width="70%" height="auto"/></p>
</details>

### 6. 사용자 채용공고 지원(사용자는 1회 지원 가능)
> GET api/application/id/
<details>
<summary>사용자 채용공고 지원</summary>
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194769847-438a67a6-8cc6-45f9-89fd-db61cdfd24ac.png" width="70%" height="auto"/></p>

</details>



#### 사용자 채용공고 지원 API
|Mtehod|API|Action|
|:---:|:---:|:---:|
|GET|/api/application/|모든 지원 조회|
|GET|/api/application/ID/|특정 지원 조회|
|POST|/api/application/|새 지원 추가|
|PUT|/api/application/ID/|특정 지원 갱신|
|DELETE|/api/application/ID/|특정 지원 삭제|

<details>
<summary>사용자 채용공고 지원 CURD</summary>

> POST api/application/
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194769791-df87f9aa-a348-4381-8d6e-8bf8bbc05b8e.png" width="70%" height="auto"/></p>

> GET api/application/
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194769817-089416eb-df8a-43da-b237-0c00db484823.png" width="70%" height="auto"/></p>

> GET api/application/id/
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194769847-438a67a6-8cc6-45f9-89fd-db61cdfd24ac.png" width="70%" height="auto"/></p>

> PUT api/application/id/
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194769875-52aad8cc-dc9e-4ab4-81a6-a541dca696f4.png" width="70%" height="auto"/></p>

> DELETE api/application/id/
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194769903-b1c267b6-148d-46e4-a1cb-2b8309a7df79.png" width="70%" height="auto"/></p>

</details>

## 사용자 CRUD
|Mtehod|API|Action|
|:---:|---:|---:|
|GET|/api/user/|모든 사용자 조회|
|GET|/api/user/ID/|특정 사용자 조회|
|POST|/api/user/|새 사용자 추가|
|PUT|/api/user/ID/|특정 사용자 갱신|
|DELETE|/api/user/ID/|특정 사용자 삭제|

<details>
<summary>사용자 CRUD</summary>

> POST /api/user/
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194768696-0efbab9d-eab0-4e68-b93f-eaaba6d7630f.png" width="70%" height="auto"/></p>

> GET /api/user/
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194768922-8be51f80-66c6-4836-a0ea-e529f454d752.png" width="70%" height="auto"/></p>

> PUT /api/user/id/
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194769047-c840d67b-3fef-4ce7-98ba-49e0ab11a083.png" width="70%" height="auto"/></p>

> GET /api/user/id/
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194769157-ea186cd1-425d-4571-87ab-9fc1e977609c.png" width="70%" height="auto"/></p>

> DELETE /api/user/id/
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194769219-897d8386-19d1-4697-8a5d-8d697ed0a15b.png" width="70%" height="auto"/></p>

</details>

### 채용 회사 CRUD
|Mtehod|API|Action|
|:---:|---:|---:|
|GET|/api/company/|모든 회사 조회|
|GET|/api/company/ID/|특정 회사 조회|
|POST|/api/company/|새 회사 추가|
|PUT|/api/company/ID/|특정 회사 갱신|
|DELETE|/api/company/ID/|특정 회사 정보 삭제|

<details>
<summary>채용 회사 CRUD</summary>

> GET /api/company/
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194766347-33c9b1b0-1160-4ceb-9f84-ead3d7987971.png" width="70%" height="auto"/></p>

> POST /api/company/
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194766285-72cd4e51-e96b-449c-9f58-7bcc1be33720.png" width="70%" height="auto"/></p>

> PUT /api/company/id/
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194766305-b2df4c31-8caf-4685-a8dc-d29c0f803773.png" width="70%" height="auto"/></p>
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194766315-e14b6e94-e061-4e90-b23c-69f2b1f44b6f.png" width="70%" height="auto"/></p>

> GET /api/company/id/
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194766328-38d8eb96-cff0-4f84-9501-0c9a555c09d6.png" width="70%" height="auto"/></p>

> DELETE /api/company/id/
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194766363-3437bf3f-71b0-42bb-a9d4-19182331dfa8.png" width="70%" height="auto"/></p>
<p align="center"><img src="https://user-images.githubusercontent.com/104122924/194766370-ac338ced-429d-4d77-8999-34cb8f67eb03.png" width="70%" height="auto"/></p>

</details>


