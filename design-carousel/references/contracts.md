# 데이터 규칙

세 스키마는 JSON Schema 2020-12다. brief_id로 문서들을 연결하고 slide_id로 슬라이드를 연결한다. 모든 객체는 정의된 필드만 허용한다. 예제는 2장으로 압축한 계획이며 실제 생성·실행 결과가 아니다.

구조 검증 후 확인: brief.slide_count = slide-plan.slides 길이 = design-plan.slides 길이, slide_id와 element_id 중복 없음, slide plan과 design plan의 장 ID 집합 동일, 캔버스와 언어 동일, 안전 영역이 캔버스보다 작음. text 요소에는 text와 typography, image 요소에는 image, shape 요소에는 fill이 필요하다.

좌표는 캔버스 기준 px이다. z 오름차순으로 배치한다. text 색은 typography.color, shape 색은 fill이다. 이미지 status는 planned/generated/provided/failed다. generated/provided에는 실제 asset_path가 필요하다. 폰트는 설치 여부를 실행 시 확인하고 대체를 보고한다.

headline/body/cta는 편집 가능한 text 요소로 반영한다. 요소 누락 여부와 사용자 필수 요소는 구조 검증만으로 보장되지 않으므로 별도로 확인한다. 계획에 적힌 aspect_ratio는 생성 요청이며 실제 결과 비율을 검사한다. 미확인 사실은 unchecked로 기록한다.


문화 확장: culture_profile_ref와 asset_manifest_ref로 DNA/manifest를 연결한다. 이미지의 asset_id는 manifest의 유일한 ID여야 한다. 실제 이미지 prompt는 선택 사항이며 generated에는 필수다. sourced에는 web_sourced provenance·source_page_url·asset_path를 요구한다. pending은 원본 미확보로 렌더 완료를 뜻하지 않는다. 기존 예시는 문화 필드 없이도 유효하다.
