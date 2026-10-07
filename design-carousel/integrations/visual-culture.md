# visual-culture 연동
설치된 독립 visual-culture/SKILL.md를 읽는다. 배포본에서는 이웃 ../visual-culture/SKILL.md를 사용할 수 있다.
입력: 실제 접근 레퍼런스·사용자 원본, 메시지/독자, 작업 날짜/지역, Style DNA, 텍스트 공간.
출력: culture-dna.json, asset-manifest.json, 슬라이드 자산 역할과 한국어 선정 근거.
content strategist와 layout director는 이 산출물을 함께 사용하고 본문 길이·구도를 조정한다. image director는 원본 확보와 생성 장식을 구분한다. figma-carousel에는 ready 자산만 넘긴다. pending/reference_only는 배치하지 않는다. 권리 미확인 자산은 배포 상태를 별도로 표시한다.
경로는 실제 작업 파일을 참조한다. 웹 검색이 실패하면 기존 업로드로 전환하며 최신성은 미확인으로 둔다. 스타일·문화 점수는 분리하여 평가한다.

호출 조건: visual-strategy의 culture_mode=use일 때. skip이면 문화 DNA·Culture Critic은 해당 없음으로 두고 일반 이미지 전략으로 계속 진행한다. 모든 사진의 원본/처리 provenance와 검색 상태는 유지한다.
