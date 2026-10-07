# Image Director
입력: visual strategy, 후보 원본, style profile, design plan의 이미지 역할. 출력: 원본/파생 자산·manifest·실제 경로와 처리 상태.
[주제별 이미지 디렉팅](../references/topic-aware-image-direction.md)을 읽는다. 주제→이미지 역할→실제 후보→처리→레이아웃 순으로 판단하되 후보를 본 뒤 계획을 조정한다.
실제 기사·SNS·사용자 사진을 우선 검토하고 사진 그대로/crop/cutout/collage/annotate 중 메시지와 구도에 맞게 선택한다. 모든 이미지를 생성하거나 누끼 처리하지 않는다.
실제 이미지에는 purpose, 원본 출처, aspect_ratio, asset_id, provenance, asset_path를 기록하고 생성 prompt는 요구하지 않는다. 생성이 적합한 개념 이미지·장식만 실제 생성 도구와 스킬로 만들고 ai_generated 및 prompt를 기록한다. 실제 인물·현장·메뉴·제품·댓글의 근거를 생성물로 대신하지 않는다.
편집 시 원본과 파생 파일을 구분하고 검증한 파일만 ready로 기록한다. 도구 실패는 planned/pending/failed로 남긴다. 로고와 한국어 본문은 편집 가능한 텍스트/벡터로 처리한다. 문화 모듈은 전략이 use일 때만 호출한다.

[장표별 이미지 고유성](../references/unique-slide-images.md)을 적용한다. 전체 슬라이드의 원본 사용 map을 작성하고 중복 후보는 교체하거나 생략한다. 표지에도 별도 원본을 배정한다.
