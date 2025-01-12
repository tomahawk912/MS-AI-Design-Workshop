# Use Control condition with Chat flow
### 조건문에 대한 분기를 표현하는 Flow

## 프롬프트 흐름
<img src="control-switch-flow.png" alt="Function Calling" width="600">

- 사용자의 의도에 따라 세가지 범주로 분류하여 답변하는 Flow

## 코드설명 (노드/코드)
- classify_with_llm 노드 (joke.jinja2) : 3가지 범주 분류하는 LLM 노드 (product_recommendation, order_search, product_info)
- class_check 노드 (echo.py) : llm이 판단한 3가지 범주가 정확한지 오류 체크, 오류인 경우 Else로 처리
- product_recommendation 노드 (product_recommendation.py) : 범주 별 답변 생성
- order_search 노드 (order_search.py) : 범주 별 답변 생성
- product_info 노드 (product_info.py) : 범주 별 답변 생성
- generate_response 노드 (generate_response) : 3개의 응답을 받아서 실행된 노드의 답변을 반환 (Null이 아닌)

## 테스트방법
- 입력 : 상품 좀 알아보려고 해