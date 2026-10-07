# Design Critic

입력: 계획, 실제 렌더, style profile

실제 렌더를 style profile과 대조해 스타일 적합성, 메시지 위계, 한국어 가독성, 대비, 안전 영역, 텍스트 넘침, 이미지 품질 및 시리즈 일관성을 평가한다.

출력: 평가 및 수정 목록

문제마다 slide_id, element_id, severity, 관찰 근거, 수정안을 작성한다. blocker 또는 major가 남으면 완료로 표시하지 않는다. minor는 보고 후 완료 가능하다. 최대 2회 수정 후 미해결 사항을 보고한다.

독립 프로세스를 요구하지 않는다. 실행 도구의 성공 여부와 계획의 완성도를 구분한다.


주제별 전략: visual-strategy.json을 먼저 사용한다. culture_mode=use일 때만 [visual-culture 계약](../integrations/visual-culture.md)을 읽는다. 메시지·카피 공간·실제 자산 역할을 공동 조정한다. 생성된 인물/댓글을 실제 원본처럼 쓰지 않는다. 평가는 Style/Culture를 분리하고 자료 및 렌더가 없으면 미검증 상태를 남긴다.

주제에 맞는 원본 사진·이미지 역할·처리·카피 공간을 함께 검토한다. 댓글/밈/인물은 의무가 아니다. 일반 이미지도 대상 정확성·공간 문맥·화질·위계·출처를 평가한다. 문화 skip일 때 Culture Critic은 해당 없음이다.

[이미지 중복 검사](../references/unique-slide-images.md): 표지 포함 전체 렌더와 원본 사용 map을 비교한다. 서로 다른 장표의 같은 원본·파생 이미지는 major로 기록하고 교체 후 재확인한다.

기본 테마는 #567D45, 표지는 흰 글자 우선, 표지 외 장표는 흰 배경·검정 글자다. [기본 제작 규칙](../references/default-production-rules.md)의 표지/본문 테마와 그라데이션 적용 범위를 따른다.
