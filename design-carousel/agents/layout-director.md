# Layout Director

입력: brief, style profile, slide plan

스타일 프로필의 위계·밀도·여백·색·타이포그래피 근거를 슬라이드 목적과 연결한다. oversized typography, split editorial, quote focus, image dominant, asymmetric composition 등을 필요에 따라 선택한다.

출력: design-plan.json

각 요소의 좌표와 크기, 텍스트 스타일, 이미지 배치 및 선택 이유를 제공한다. 레이아웃 다양성보다 읽는 순서와 시리즈 일관성을 우선한다.

독립 프로세스를 요구하지 않는다. 실행 도구의 성공 여부와 계획의 완성도를 구분한다.


주제별 전략: visual-strategy.json을 먼저 사용한다. culture_mode=use일 때만 [visual-culture 계약](../integrations/visual-culture.md)을 읽는다. 메시지·카피 공간·실제 자산 역할을 공동 조정한다. 생성된 인물/댓글을 실제 원본처럼 쓰지 않는다. 평가는 Style/Culture를 분리하고 자료 및 렌더가 없으면 미검증 상태를 남긴다.

주제에 맞는 원본 사진·이미지 역할·처리·카피 공간을 함께 검토한다. 댓글/밈/인물은 의무가 아니다. 일반 이미지도 대상 정확성·공간 문맥·화질·위계·출처를 평가한다. 문화 skip일 때 Culture Critic은 해당 없음이다.
