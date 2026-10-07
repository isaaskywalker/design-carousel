# Cultural Relevance Scorer
다섯 차원을 0..1로 기록하고 각 점수에 한국어 근거를 붙인다.
- relevance 0.35: 주제와 원문 맥락에 직접 연결되는가? 유명하다는 이유만이면 낮게.
- recognizability 0.20: 목표 독자가 알아볼 근거가 있는가? 글로벌 유명세를 한국 독자 인지로 치환하지 않는다.
- recency 0.15: 최근 사용/보도의 증거와 사건 날짜가 있는가? 게시일과 원본 발생일을 분리한다.
- composition_fit 0.20: 해상도·크롭·여백·방향·얼굴 가림·텍스트 공간이 적합한가?
- source_confidence 0.10: 원본·작성자·문맥을 실제 확인했는가? 검색 스니펫만이면 낮게.
weighted_total = Σ(weight × score). timeless 모드에서는 recency 가중치를 0으로 두고 나머지를 합계 1로 정규화한다. 미확인 점수는 null로 기록한다. null을 임의로 높이거나 0으로 바꾸지 않고 총점도 null, pending으로 둔다.
일반 후보 선택 기준은 total ≥0.70, relevance ≥0.60, source_confidence ≥0.50. latest 모드는 recency ≥0.60과 날짜 근거도 필요하다. 기준은 사용자 목표에 맞춰 명시적으로 조정 가능하다. 권리/자료 준비 상태는 별도 gate이며 점수가 사용 허가를 뜻하지 않는다. 동점은 맥락·출처 근거가 더 강한 자산을 고른다.
점수는 판단 보조이며 통계적으로 측정한 인기도가 아니다.

계산은 [score_assets.py](../scripts/score_assets.py)로 반복 가능하다. `python score_assets.py input.json scored.json`처럼 새 파일에 쓴다. 입력 점수와 근거는 실제 조사 판단을 먼저 작성한다. 스크립트는 검색·인지도 측정·권리 확인을 대신하지 않는다. timeless 모드는 recency 미확인을 총점 계산에서 제외한다. latest 모드는 날짜가 없으면 pending, restricted/reference_only/failed는 reject다. select는 후보 선정이며 ready 및 배포 허가를 뜻하지 않는다.

이 점수는 문화 후보 전용이다. 일반 장소/음식/제품 사진에는 유명세·최신성 기준을 강제하지 않고 대상 정확성·의미 적합성·화질·구도를 중심으로 비교한다.

한국 최신 모드에서는 [국내 최신성 gate](../references/korean-current-memes.md)를 총점보다 먼저 적용한다. KR 사용·국내 인지도 근거 미확인 후보는 pending이며 높은 합산 점수로 통과시키지 않는다.
