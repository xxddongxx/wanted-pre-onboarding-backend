# wanted_pre_onboarding_backend

## 요구사항 목록
> 1. 채용공고 등록
> 2. 채용공고 수정
> 3. 채용공고 삭제
> 4. 채용공고 목록
>   * 채용공고 검색 기능
> 5. 채용상세 페이지(해당 회사가 올리 다른 공고)
> 6. 사용자 채용공고 지원(사용자는 1회지원 가능)

## DB Table 구성

## 요구사항 API
### 채용공고 API
|Mtehod|API|Action|
|:---:|---:|---:|
|GET|/api/job_posting/|모든 채용공고 조회|
|GET|/api/job_posting/ID/|특정 채용공고 조회|
|POST|/api/job_posting/|새 채용공고 추가|
|PUT|/api/job_posting/ID/|특정 채용공고 갱신|
|DELETE|/api/job_posting/ID/|특정 채용공고 삭제|
###1. 채용공고 등록
> POST /api/company/
<details>
<summary>채용공고 등록</summary>

</details>

###2. 채용공고 수정
> PUT /api/company/id/
<details>
<summary>채용공고 수정</summary>

</details>

###3. 채용공고 삭제
> DELETE /api/company/id
<details>
<summary>채용공고 삭제</summary>

</details>

###4. 채용공고 목록
> GET /api/company
<details>
<summary>채용공고 목록</summary>

</details>

###4.1 채용공고 검색
> GET /api/search?search=keyowrd
<details>
<summary>채용공고 검색</summary>

</details>

###5. 채용공고 상세 페이지(해당 회사가 올린 다른 공고)
> GET /api/company/id/
<details>
<summary>채용공고 상세 페이지</summary>

</details>

###6. 사용자 채용공고 지원(사용자는 1회 지원 가능)
> POST /api/application/
<details>
<summary>사용자 채용공고 지원</summary>

</details>



#### 사용자 채용공고 지원 API
|Mtehod|API|Action|
|:---:|:---:|:---:|
|GET|/api/application/|모든 지원 조회|
|GET|/api/application/ID/|특정 지원 조회|
|POST|/api/application/|새 지원 추가|
|PUT|/api/application/ID/|특정 지원 갱신|
|DELETE|/api/application/ID/|특정 지원 삭제|

## 사용자 CRUD
|Mtehod|API|Action|
|:---:|---:|---:|
|GET|/api/user/|모든 사용자 조회|
|GET|/api/user/ID/|특정 사용자 조회|
|POST|/api/user/|새 사용자 추가|
|PUT|/api/user/ID/|특정 사용자 갱신|
|DELETE|/api/user/ID/|특정 사용자 삭제|